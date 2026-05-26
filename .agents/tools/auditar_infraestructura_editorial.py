#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

MOJIBAKE_PATTERNS: tuple[str, ...] = ("ðŸ", "Ã¡", "Ã©", "Ã­", "Ã³", "Ãº", "Ã±")
FORBIDDEN_EXTERNAL_ACTIONS: tuple[str, ...] = (
    "publicar automaticamente",
    "subir a",
    "published",
)

@dataclass
class Finding:
    file: str
    issue: str
    detail: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        logging.error("No se pudo leer %s: %s", path, exc)
        return ""


def scan_docs(base: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in base.rglob("*.md"):
        text = read_text(path)
        lowered = text.lower()
        for pattern in MOJIBAKE_PATTERNS:
            if pattern in text:
                findings.append(Finding(str(path), "mojibake", f"Contiene patrón '{pattern}'"))
        for pattern in FORBIDDEN_EXTERNAL_ACTIONS:
            if pattern in lowered:
                findings.append(Finding(str(path), "accion_externa", f"Contiene '{pattern}'"))
    return findings


def parse_manifest_paths(manifest: Path) -> set[str]:
    text = read_text(manifest)
    return set(re.findall(r'"(\.agents/[^"]+\.md)"', text))


def collect_editorial_components(base: Path, repo: Path) -> set[str]:
    return {str(p.relative_to(repo)) for p in base.rglob("*.md")}


def collect_wrappers(wrapper_dir: Path) -> dict[str, str]:
    wrappers: dict[str, str] = {}
    if not wrapper_dir.exists():
        return wrappers
    for path in wrapper_dir.rglob("*.md"):
        text = read_text(path)
        match = re.search(r"(\.agents/(editorial|generos|novelas)/[^\s`]+\.md)", text)
        wrappers[str(path)] = match.group(1) if match else ""
    return wrappers


def build_report(repo: Path, output: Path) -> int:
    findings = scan_docs(repo / ".agents")
    manifest_paths = parse_manifest_paths(repo / ".agents/manifest.yaml")
    editorial_paths = collect_editorial_components(repo / ".agents/editorial", repo)

    missing_in_manifest = sorted(editorial_paths - manifest_paths)

    wrappers = {}
    wrappers.update(collect_wrappers(repo / ".agents/rules"))
    wrappers.update(collect_wrappers(repo / ".agents/skills"))
    wrappers.update(collect_wrappers(repo / ".agents/workflows"))
    wrappers_without_target = sorted([k for k, v in wrappers.items() if not v])

    report = {
        "findings": [f.__dict__ for f in findings],
        "missing_in_manifest": missing_in_manifest,
        "wrappers_without_target": wrappers_without_target,
        "totals": {
            "findings": len(findings),
            "missing_in_manifest": len(missing_in_manifest),
            "wrappers_without_target": len(wrappers_without_target),
        },
    }

    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    logging.info("Reporte generado: %s", output)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Auditoría de infraestructura editorial")
    parser.add_argument("--repo", default=".", help="Ruta del repositorio")
    parser.add_argument(
        "--output",
        default=".agents/reports/auditoria_infraestructura.json",
        help="Ruta de salida del reporte JSON",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    try:
        return build_report(repo, output)
    except Exception as exc:
        logging.exception("Error en auditoría: %s", exc)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
