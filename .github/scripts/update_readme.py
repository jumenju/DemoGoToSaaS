#!/usr/bin/env python3
"""Regenerates the STRUCTURE, TECH and CONTRIBUTIONS sections in README.md."""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


# ── helpers ──────────────────────────────────────────────────────────────────

def replace_section(content: str, marker: str, new_body: str) -> str:
    pattern = rf"(<!-- {marker}_START -->).*?(<!-- {marker}_END -->)"
    replacement = rf"\1\n{new_body}\n\2"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


# ── 1. Structure du projet ────────────────────────────────────────────────────

IGNORED = {".git", ".github", "node_modules"}

FILE_ROLES: dict[str, str] = {
    "index.html": "Page unique du site : en-tête, section changelog, footer",
    "README.md":  "Documentation du projet",
}

def file_role(rel: Path) -> str:
    return FILE_ROLES.get(rel.name, "")

def build_structure() -> str:
    rows = []
    tree_lines = ["```", "DemoGoToSaaS/"]
    files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and not any(part in IGNORED for part in p.parts)
    )
    for f in files:
        rel = f.relative_to(ROOT)
        parts = rel.parts
        indent = "│   " * (len(parts) - 1)
        tree_lines.append(f"{indent}├── {parts[-1]}")
        rows.append(f"| `{rel}` | {file_role(rel)} |")
    tree_lines.append("```")

    table = "| Fichier | Rôle |\n|---|---|\n" + "\n".join(rows)
    return "\n".join(tree_lines) + "\n\n" + table


# ── 2. Technologies utilisées (parsed from index.html) ───────────────────────

def build_tech() -> str:
    index = (ROOT / "index.html").read_text(encoding="utf-8")

    techs = [
        ("HTML5", "—", "Structure de la page"),
        ("CSS3", "—", "Styles personnalisés (variables CSS, gradients)"),
    ]

    # Bootstrap version from CDN link
    m = re.search(r"bootstrap/(\d+\.\d+\.\d+)/css/bootstrap\.min\.css", index)
    if m:
        techs.append((
            "[Bootstrap](https://getbootstrap.com/)",
            m.group(1),
            "Mise en page responsive, tableau, cartes",
        ))

    # GitHub Pages always used for hosting
    techs.append(("GitHub Pages", "—", "Hébergement statique"))

    # Cloudflare cdnjs
    if "cdnjs.cloudflare.com" in index:
        techs.append((
            "[Cloudflare cdnjs](https://cdnjs.cloudflare.com/)",
            "—",
            "Livraison CDN de Bootstrap",
        ))

    header = "| Technologie | Version | Usage |\n|---|---|---|"
    rows = "\n".join(f"| {t} | {v} | {u} |" for t, v, u in techs)
    return header + "\n" + rows


# ── 3. Contributions approuvées (git log) ────────────────────────────────────

def build_contributions() -> str:
    result = subprocess.run(
        ["git", "log", "--pretty=format:%ad|%s|%an", "--date=short"],
        capture_output=True, text=True, cwd=ROOT,
    )
    header = "| Date | Contribution | Auteur |\n|---|---|---|"
    rows = []
    for line in result.stdout.strip().splitlines():
        # skip auto-commits from this workflow
        if "[skip ci]" in line:
            continue
        date, msg, author = line.split("|", 2)
        rows.append(f"| {date} | {msg} | {author} |")
    return header + "\n" + "\n".join(rows)


# ── main ─────────────────────────────────────────────────────────────────────

readme = (ROOT / "README.md").read_text(encoding="utf-8")
readme = replace_section(readme, "STRUCTURE", build_structure())
readme = replace_section(readme, "TECH", build_tech())
readme = replace_section(readme, "CONTRIBUTIONS", build_contributions())
(ROOT / "README.md").write_text(readme, encoding="utf-8")
print("README.md updated.")
