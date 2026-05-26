import argparse
import re
from pathlib import Path


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def load_metadata(project_root: Path, language: str) -> dict:
    file_path = project_root / "metadata" / f"{language}.yml"
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontro el archivo de metadatos: {file_path}")
    
    data = {}
    current_key = None
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            
            if stripped.startswith("-"):
                val = stripped[1:].strip().strip('"').strip("'")
                if current_key and isinstance(data.get(current_key), list):
                    data[current_key].append(val)
                continue
            
            match = re.match(r"^([a-zA-Z_0-9]+)\s*:\s*(.*)$", line)
            if match:
                key, val = match.groups()
                val = val.strip()
                if val.startswith("[") and val.endswith("]"):
                    val = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                    data[key] = val
                elif val.startswith('"') and val.endswith('"'):
                    data[key] = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    data[key] = val[1:-1]
                elif not val:
                    data[key] = []
                else:
                    data[key] = val
                current_key = key
    return data


def validate_metadata(metadata: dict, language: str):
    title = metadata.get("title", "").strip()
    subtitle = metadata.get("subtitle", "").strip()
    author = metadata.get("author", "").strip()
    lang = metadata.get("language", "").strip()
    
    if not title or title == "Untitled":
        raise ValueError("El titulo no puede estar vacio o ser 'Untitled'")
    if not author or author == "Author Name":
        raise ValueError("El autor no puede estar vacio o ser 'Author Name'")
    if not lang:
        raise ValueError("El idioma no puede estar vacio")
    if not subtitle:
        raise ValueError("El subtitulo no puede estar vacio")
    
    placeholders = ["TODO", "FIXME", "[pendiente]", "Lorem ipsum", "anos de distancia"]
    for field in ["title", "subtitle", "author", "language", "publisher", "ai_disclosure"]:
        val = metadata.get(field, "")
        if isinstance(val, str):
            for pl in placeholders:
                if pl.lower() in val.lower():
                    raise ValueError(f"Se detecto el placeholder prohibido '{pl}' en el campo '{field}'")
    
    if language == "es":
        if title != "Luz Vieja":
            raise ValueError(f"El titulo en espanol debe ser 'Luz Vieja', se obtuvo '{title}'")
        if subtitle != "Veinte anos de distancia" and subtitle != "Veinte años de distancia":
            raise ValueError(f"El subtitulo en espanol debe ser 'Veinte anos de distancia', se obtuvo '{subtitle}'")
    elif language == "en":
        if title != "Old Light":
            raise ValueError(f"El titulo en ingles debe ser 'Old Light', se obtuvo '{title}'")
        if subtitle != "Twenty Light-Years of Distance":
            raise ValueError(f"El subtitulo en ingles debe ser 'Twenty Light-Years of Distance', se obtuvo '{subtitle}'")
            
    if author != "IOREB":
        raise ValueError(f"El autor definitivo debe ser 'IOREB', se obtuvo '{author}'")


def escape_latex(text: str) -> str:
    text = text.replace("\\", r"\textbackslash{}")
    replacements = {
        "%": r"\%",
        "#": r"\#",
        "&": r"\&",
        "$": r"\$",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for raw, escaped in replacements.items():
        text = text.replace(raw, escaped)
    return text


def parse_markdown_to_latex(text: str) -> str:
    latex_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            latex_lines.append("")
            continue

        l_line = line.lower()
        if l_line.startswith("# capitulo") or l_line.startswith("# capítulo") or l_line.startswith("# chapter") or l_line.startswith("capitulo ") or l_line.startswith("capítulo ") or l_line.startswith("chapter "):
            clean = line.replace("# ", "", 1) if line.startswith("# ") else line
            parts = re.split(r"\s+[—-]\s+", clean, maxsplit=1)
            title = parts[1].strip() if len(parts) > 1 else clean.strip()
            title = escape_latex(title)
            latex_lines.append(f"\\chapter{{{title}}}")
            latex_lines.append(f"\\markboth{{{title}}}{{{title}}}")
            continue

        if line in {"— — —", "***", "---"}:
            latex_lines.extend([
                r"\vspace{1.5em}",
                r"\begin{center}$\ast$\quad$\ast$\quad$\ast$\end{center}",
                r"\vspace{1.5em}",
            ])
            continue

        line = escape_latex(line)
        line = line.replace("₂", r"\textsubscript{2}")
        line = re.sub(r"\*([^*]+)\*", r"\\textit{\1}", line)
        latex_lines.append(line)

    return "\n".join(latex_lines)


def build_preamble(title: str, subtitle: str, author: str, cover_filename: str | None, language: str = "es") -> str:
    cover_block = ""
    if cover_filename:
        cover_block = rf"""
\newgeometry{{margin=0pt}}
\thispagestyle{{empty}}
\noindent\includegraphics[width=\paperwidth, height=\paperheight]{{{cover_filename}}}
\clearpage
\restoregeometry
"""

    babel_lang = "spanish" if language == "es" else "english"

    if language == "es":
        legal_block = rf"""\clearpage
\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}
{{\small
\textbf{{{escape_latex(title)}}} \\
Autor: {escape_latex(author)} \\
© 2026, {escape_latex(author)}. Todos los derechos reservados. \\
\vspace{{1.5em}}
Cualquier forma de reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley. Diríjase a CEDRO (Centro Español de Derechos Reprográficos) si necesita fotocopiar o escanear algún fragmento de esta obra. \\
\vspace{{1.5em}}
Diseño de portada: {escape_latex(author)}. \\
\vspace{{1.5em}}
Declaración de Asistencia de IA: Esta obra de ciencia ficción ha sido desarrollada y traducida con la asistencia de modelos de lenguaje de inteligencia artificial como parte de un proceso creativo agéntico iterativo en EditorIAl IOREB.
}}
\end{{center}}
\vspace*{{\fill}}
\clearpage"""
    else:
        legal_block = rf"""\clearpage
\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}
{{\small
\textbf{{{escape_latex(title)}}} \\
Author: {escape_latex(author)} \\
© 2026, {escape_latex(author)}. All rights reserved. \\
\vspace{{1.5em}}
No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. \\
\vspace{{1.5em}}
Cover design by: {escape_latex(author)}. \\
\vspace{{1.5em}}
AI Assistance Declaration: This work of science fiction was developed and translated with the assistance of artificial intelligence language models as part of an iterative agentic creative process at EditorIAl IOREB.
}}
\end{{center}}
\vspace*{{\fill}}
\clearpage"""

    return rf"""\documentclass[11pt,a5paper,twoside]{{book}}
\usepackage[utf8]{{inputenc}}
\usepackage[{babel_lang}]{{babel}}
\usepackage[T1]{{fontenc}}
\usepackage{{lmodern}}
\usepackage{{microtype}}
\usepackage{{geometry}}
\geometry{{
    a5paper,
    inner=25mm,
    outer=20mm,
    top=20mm,
    bottom=20mm
}}
\usepackage{{graphicx}}
\usepackage{{titlesec}}
\titleformat{{\chapter}}[display]
  {{\normalfont\huge\bfseries\centering}}{{\chaptertitlename\ \thechapter}}{{20pt}}{{\Huge}}
\usepackage[titles]{{tocloft}}
\setlength{{\cftchapnumwidth}}{{3.5em}}
\widowpenalty=10000
\clubpenalty=10000
\linespread{{1.15}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyfoot[C]{{\thepage}}
\fancyfoot[R]{{\rightmark}}
\renewcommand{{\headrulewidth}}{{0pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\renewcommand{{\thechapter}}{{\Roman{{chapter}}}}
\title{{{escape_latex(title)} \\ \large {escape_latex(subtitle)}}}
\author{{{escape_latex(author)}}}
\date{{}}

\begin{{document}}
{cover_block}
\frontmatter
\maketitle
{legal_block}
\tableofcontents

\mainmatter
"""


def generate_book(project_root: Path, language: str, output: Path | None) -> Path:
    metadata = load_metadata(project_root, language)
    validate_metadata(metadata, language)

    title = metadata["title"]
    subtitle = metadata["subtitle"]
    author = metadata["author"]

    if language == "es":
        manuscript_dir = project_root / "manuscrito"
    else:
        manuscript_dir = project_root / "traducciones" / language / "manuscrito"
    
    export_dir = project_root / "exportacion" / language
    export_dir.mkdir(parents=True, exist_ok=True)

    output_name = title.replace(" ", "") + ".tex"
    output_file = output or export_dir / output_name
    if not output_file.is_absolute():
        output_file = project_root / output_file
    output_file.parent.mkdir(parents=True, exist_ok=True)

    cover_source = project_root / "exportacion" / f"portada_{language}.png"
    if not cover_source.exists():
        cover_source = project_root / "exportacion" / "portada.png"
    cover_filename = cover_source.name if cover_source.exists() else None

    chapter_files = sorted(manuscript_dir.glob("capitulo_*.md"))
    if not chapter_files:
        raise FileNotFoundError(f"No chapter files found in {manuscript_dir}")

    with output_file.open("w", encoding="utf-8", newline="\n") as f_out:
        f_out.write(build_preamble(title, subtitle, author, cover_filename, language))
        for file_path in chapter_files:
            content = file_path.read_text(encoding="utf-8")
            f_out.write(parse_markdown_to_latex(content))
            f_out.write("\n\n")
        f_out.write("\n\\end{document}\n")

    return output_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a LaTeX source file from the project manuscript.")
    parser.add_argument("--project-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--language", default="es")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    output = generate_book(
        project_root=args.project_root.resolve(),
        language=args.language,
        output=args.output,
    )
    print(f"Documento generado con exito: {output}")


if __name__ == "__main__":
    main()
