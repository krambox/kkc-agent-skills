#!/usr/bin/env python3
"""E-Rechnung pruefen mit der gebuendelten eRechnung-CLI (Mustang + KoSIT).

    erechnung.py validate [--out AUSGABEVERZEICHNIS] RECHNUNG [RECHNUNG ...]

Ruft ``erechnung.jar`` neben diesem Skript auf, ein JVM-Start fuer alle
Rechnungen. Schreibt je Rechnung den deutschen Pruefbericht (Markdown), das
volle CLI-JSON und das E-Rechnung-XML ins Ausgabeverzeichnis und gibt
``verdict``, ``version``, ``summary`` und die Artefaktpfade als JSON auf
stdout aus: bei einer Rechnung ein JSON-Objekt, bei mehreren JSON Lines (eine
Zeile je Rechnung, in Eingabereihenfolge). Exit wie die CLI: 0 conformant,
1 nonconformant, 2 not_erechnung, 3 tool_error; bei mehreren der hoechste.

Java-Kaskade: vorhandenes Java >= 11, sonst apt-get-Installation, sonst
Verdict ``tool_error`` mit Grund und Handlungshinweis.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from typing import Optional

HERE = pathlib.Path(__file__).resolve().parent
JAR = HERE / "erechnung.jar"
MIN_JAVA = 11
APT_PACKAGE = "openjdk-17-jre-headless"
# ponytail: generous; huge PEPPOL files take minutes (the corpus skips them). A batch gets
# CLI_TIMEOUT_S plus BATCH_TIMEOUT_S per further invoice (whole Corpus ~4 h ceiling, runs in ~1 min).
CLI_TIMEOUT_S = 900
BATCH_TIMEOUT_S = 60
EXIT = {"conformant": 0, "nonconformant": 1, "not_erechnung": 2, "tool_error": 3}

VERDICT_DE = {
    "conformant": "E-Rechnung ohne Fehler; geeignet für das B2B-Mandat",
    "nonconformant": "E-Rechnung erkannt, aber mit Fehlern",
    "not_erechnung": "keine E-Rechnung im Sinne des B2B-Mandats",
    "tool_error": "Prüfung nicht durchgeführt (Werkzeug- oder Dateifehler)",
}
BUCKETS = (("errors", "Fehler"), ("warnings", "Warnungen"), ("notices", "Hinweise"))
SECTIONS = ("schema", "schematron", "pdfa", "embedded_xml", "metadata_embedding")


def package_version() -> str:
    try:
        with zipfile.ZipFile(JAR) as z:
            manifest = z.read("META-INF/MANIFEST.MF").decode("utf-8", "replace")
        m = re.search(r"^Implementation-Version:\s*(\S+)", manifest, re.M)
        return m.group(1) if m else "?"
    except (OSError, KeyError, zipfile.BadZipFile):
        return "?"


def java_major(java: str) -> int:
    try:
        proc = subprocess.run([java, "-version"], capture_output=True, text=True,
                              errors="replace", timeout=60)
    except (OSError, subprocess.SubprocessError):
        return 0
    m = re.search(r'version "(\d+)(?:\.(\d+))?', proc.stderr + proc.stdout)
    if not m:
        return 0
    major = int(m.group(1))
    return int(m.group(2) or 0) if major == 1 else major  # "1.8.0" -> 8


def usable_java() -> Optional[str]:
    java = shutil.which("java")
    return java if java and java_major(java) >= MIN_JAVA else None


def install_java() -> str:
    """apt-get install; gibt bei Misserfolg den Grund zurueck, sonst ''."""
    apt = shutil.which("apt-get")
    if not apt:
        return "apt-get nicht vorhanden"
    sudo = shutil.which("sudo")
    prefix = [sudo, "-n"] if sudo and hasattr(os, "geteuid") and os.geteuid() != 0 else []
    env = dict(os.environ, DEBIAN_FRONTEND="noninteractive")
    print(f"Java {MIN_JAVA}+ fehlt, installiere {APT_PACKAGE} ...", file=sys.stderr)
    last = ""
    for cmd in ([apt, "install", "-y", "-q", APT_PACKAGE],
                [apt, "update", "-q"],
                [apt, "install", "-y", "-q", APT_PACKAGE]):
        try:
            proc = subprocess.run(prefix + cmd, capture_output=True, text=True,
                                  errors="replace", env=env, timeout=600)
        except (OSError, subprocess.SubprocessError) as exc:
            return str(exc)
        if proc.returncode == 0 and cmd[1] == "install":
            return ""
        last = (proc.stderr.strip().splitlines() or [f"Exit {proc.returncode}"])[-1]
    return f"apt-get install {APT_PACKAGE} fehlgeschlagen: {last}"


def find_java() -> tuple[Optional[str], str]:
    java = usable_java()
    if java:
        return java, ""
    reason = install_java()
    java = usable_java()
    if java:
        return java, ""
    old = shutil.which("java")
    if old:
        return None, reason or f"Java {java_major(old)} im PATH ist älter als {MIN_JAVA}"
    return None, reason or "nach Installation kein Java im PATH"


def tool_error(message: str, hint: str = "") -> dict:
    summary = {"error": message}
    if hint:
        summary["hint"] = hint
    return {"verdict": "tool_error", "summary": summary}


def run_cli(invoices: list) -> list:
    """Ein JVM-Start fuer alle Rechnungen; je Rechnung ein CLI-JSON, gleiche Reihenfolge."""
    java, reason = find_java()
    if not java:
        return [tool_error(
            f"Java {MIN_JAVA}+ nicht verfügbar ({reason}).",
            f"Java {MIN_JAVA} oder neuer installieren (z. B. `apt-get install {APT_PACKAGE}`) "
            "und die Prüfung wiederholen. Es hat keine Prüfung stattgefunden.",
        ) for _ in invoices]
    timeout = CLI_TIMEOUT_S + BATCH_TIMEOUT_S * (len(invoices) - 1)
    try:
        proc = subprocess.run([java, "-Dfile.encoding=UTF-8", "-jar", str(JAR), "validate",
                               *map(str, invoices)],
                              capture_output=True, text=True, encoding="utf-8", errors="replace",
                              timeout=timeout)
    except subprocess.TimeoutExpired:
        return [tool_error(f"eRechnung-CLI nach {timeout} s abgebrochen.") for _ in invoices]
    # stdout ist der Vertrag: ein JSON-Objekt, bei mehreren Dateien JSON Lines.
    # stderr traegt u. a. "Picked up JAVA_TOOL_OPTIONS".
    results = []
    for chunk in [proc.stdout] if len(invoices) == 1 else proc.stdout.splitlines():
        try:
            results.append(json.loads(chunk))
        except ValueError:
            break
    tail = "\n".join(proc.stderr.strip().splitlines()[-5:])
    return results + [tool_error(f"eRechnung-CLI lieferte kein JSON (Exit {proc.returncode}): {tail}")
                      for _ in invoices[len(results):]]


def render_markdown(result: dict, version: str) -> str:
    s = result.get("summary") or {}
    verdict = result.get("verdict", "tool_error")
    out = ["# E-Rechnungs-Prüfbericht", ""]
    head = [
        ("Datei", s.get("filename") and f"`{s['filename']}`"),
        ("Format", s.get("format")),
        ("Profil (BT-24)", s.get("profile") and f"`{s['profile']}`"),
        ("Generation", s.get("generation")),
        ("Anhang", s.get("attachment") and f"`{s['attachment']}`"),
        ("Engines", ", ".join(k for k, v in (s.get("engines") or {}).items() if v)),
        ("Validator", ", ".join(f"{k} {v}" for k, v in (s.get("validator") or {}).items())),
        ("Skill-Paket", f"eRechnung {version}"),
        ("Dauer", s.get("duration_ms") is not None and f"{s['duration_ms']} ms"),
    ]
    out += [f"- **{k}:** {v}" for k, v in head if v]
    out += ["", f"## Verdict: **{verdict}** – {VERDICT_DE.get(verdict, '')}", ""]

    if s.get("error"):
        out += [f"**Grund:** {s['error']}", ""]
    if s.get("hint"):
        out += [f"**Was tun:** {s['hint']}", ""]

    sections = s.get("sections") or {}
    if sections:
        out += ["## Prüfbereiche", "", "| Check section | Status |", "|---|---|"]
        for name in SECTIONS:
            sec = sections.get(name) or {}
            status = sec.get("status", "?") if sec.get("applicable") else "nicht anwendbar"
            out.append(f"| {name} | {status} |")
        out.append("")

    for key, label in BUCKETS:
        items = s.get(key) or []
        if not items:
            continue
        out += [f"## {label} ({len(items)})", ""]
        for f in items:
            out.append(f"- **{f.get('id') or '—'}** _{f.get('engine')}, {f.get('section')}_ — {f.get('message')}")
            if f.get("location"):
                out.append(f"  - Fundstelle: `{f['location']}`")
        out.append("")

    out += [
        "---",
        "",
        "*Technische Prüfung (Mustang, bei XRechnung zusätzlich KoSIT). Keine steuerliche, "
        "rechtliche oder buchhalterische Freigabe und keine Zahlungsfreigabe.*",
    ]
    return "\n".join(out) + "\n"


def write_artifacts(invoice: pathlib.Path, result: dict, outdir: pathlib.Path,
                    name: str, version: str) -> dict:
    artifacts = {
        "report": outdir / f"{name}-pruefbericht.md",
        "json": outdir / f"{name}-erechnung.json",
    }
    artifacts["report"].write_text(render_markdown(result, version), encoding="utf-8")
    artifacts["json"].write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if result.get("erechnung"):
        artifacts["xml"] = outdir / f"{name}-erechnung.xml"
        artifacts["xml"].write_text(result["erechnung"], encoding="utf-8")
    return {
        "verdict": result.get("verdict", "tool_error"),
        "version": version,
        "summary": result.get("summary") or {},
        "artifacts": {k: str(v.resolve()) for k, v in artifacts.items()},
    }


def validate(invoices: list, outdir: Optional[pathlib.Path]) -> int:
    version = package_version()
    results = run_cli(invoices)

    outdir = outdir or pathlib.Path(tempfile.mkdtemp(prefix="erechnung-"))
    outdir.mkdir(parents=True, exist_ok=True)
    used = set()
    lines = []
    for invoice, result in zip(invoices, results):
        stem = name = invoice.stem or "rechnung"
        n = 2
        while name in used:  # gleicher Dateiname aus verschiedenen Ordnern
            name, n = f"{stem}-{n}", n + 1
        used.add(name)
        lines.append(write_artifacts(invoice, result, outdir, name, version))

    if len(lines) == 1:
        print(json.dumps(lines[0], ensure_ascii=False, indent=2))
    else:
        for line in lines:
            print(json.dumps(line, ensure_ascii=False))
    return max(EXIT.get(line["verdict"], 3) for line in lines)


def main(argv: Optional[list] = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    outdir = None
    bad = False
    if "--out" in args:
        i = args.index("--out")
        bad = i + 1 >= len(args)
        outdir = None if bad else pathlib.Path(args[i + 1])
        del args[i:i + 2]
    if bad or len(args) < 2 or args[0] != "validate" or "--out" in args:
        print(__doc__, file=sys.stderr)
        return 3
    return validate([pathlib.Path(a) for a in args[1:]], outdir)


if __name__ == "__main__":
    sys.exit(main())
