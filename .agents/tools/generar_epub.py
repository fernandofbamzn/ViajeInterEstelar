import argparse
import html
import re
import uuid
import zipfile
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


def parse_markdown_to_html(text: str) -> str:
    html_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        l_line = line.lower()
        if l_line.startswith("# capitulo") or l_line.startswith("# capítulo") or l_line.startswith("# chapter") or l_line.startswith("capitulo ") or l_line.startswith("capítulo ") or l_line.startswith("chapter "):
            clean = line.replace("# ", "", 1) if line.startswith("# ") else line
            parts = re.split(r"\s+[—-]\s+", clean, maxsplit=1)
            title = parts[1].strip() if len(parts) > 1 else clean.strip()
            html_lines.append(f"<h1>{html.escape(title)}</h1>")
            continue

        if line in {"— — —", "***", "---"}:
            html_lines.append("<div class=\"scene-break\">* * *</div>")
            continue

        escaped = html.escape(line)
        escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
        escaped = escaped.replace("₂", "<sub>2</sub>")
        html_lines.append(f"<p>{escaped}</p>")

    return "\n".join(html_lines)


def chapter_title(markdown: str, fallback: str) -> str:
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        l_line = line.lower()
        if l_line.startswith("# capitulo") or l_line.startswith("# capítulo") or l_line.startswith("# chapter") or l_line.startswith("capitulo ") or l_line.startswith("capítulo ") or l_line.startswith("chapter "):
            clean = line.replace("# ", "", 1) if line.startswith("# ") else line
            parts = re.split(r"\s+[—-]\s+", clean, maxsplit=1)
            return parts[1].strip() if len(parts) > 1 else clean.strip()
    return fallback


def generate_epub(project_root: Path, language: str, output: Path | None) -> Path:
    metadata = load_metadata(project_root, language)
    validate_metadata(metadata, language)

    title = metadata["title"]
    author = metadata["author"]

    if language == "es":
        manuscript_dir = project_root / "manuscrito"
    else:
        manuscript_dir = project_root / "traducciones" / language / "manuscrito"
    
    export_dir = project_root / "exportacion" / language
    export_dir.mkdir(parents=True, exist_ok=True)

    output_name = title.replace(" ", "") + ".epub"
    output_file = output or export_dir / output_name
    if not output_file.is_absolute():
        output_file = project_root / output_file
    output_file.parent.mkdir(parents=True, exist_ok=True)

    cover_path = project_root / "exportacion" / f"portada_{language}.png"
    if not cover_path.exists():
        cover_path = project_root / "exportacion" / "portada.png"

    chapter_files = sorted(manuscript_dir.glob("capitulo_*.md"))
    if not chapter_files:
        raise FileNotFoundError(f"No chapter files found in {manuscript_dir}")

    book_id = str(uuid.uuid4())
    files_to_zip: dict[str, str] = {
        "mimetype": "application/epub+zip",
        "META-INF/container.xml": """<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""",
        "OEBPS/stylesheet.css": """
body {
    font-family: serif;
    margin: 5%;
    text-align: justify;
    line-height: 1.5;
}
h1 {
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1em;
    font-size: 1.8em;
}
p {
    text-indent: 1.5em;
    margin: 0;
}
.scene-break {
    text-align: center;
    margin: 2em 0;
}
.toc-list {
    list-style-type: none;
    padding: 0;
    text-align: center;
}
.toc-list li {
    margin: 1em 0;
}
""",
    }

    manifest_items = [
        '<item id="css" href="stylesheet.css" media-type="text/css"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="toc-page" href="toc.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="legal-page" href="legal.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine_items = ['<itemref idref="legal-page"/>', '<itemref idref="toc-page"/>']
    nav_points = []
    toc_links = []

    legal_title = "Página Legal" if language == "es" else "Legal Notice"
    if language == "es":
        legal_text = f"""
        <p><strong>{title}</strong></p>
        <p>Autor: {author}</p>
        <p>© 2026, {author}. Todos los derechos reservados.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">Cualquier forma de reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley. Diríjase a CEDRO (Centro Español de Derechos Reprográficos) si necesita fotocopiar o escanear algún fragmento de esta obra.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">Diseño de portada: {author}.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">Declaración de Asistencia de IA: Esta obra de ciencia ficción ha sido desarrollada y traducida con la asistencia de modelos de lenguaje de inteligencia artificial como parte de un proceso creativo agéntico iterativo en EditorIAl IOREB.</p>
        """
    else:
        legal_text = f"""
        <p><strong>{title}</strong></p>
        <p>Author: {author}</p>
        <p>© 2026, {author}. All rights reserved.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">Cover design by: {author}.</p>
        <p style="margin-top: 1.5em; text-indent: 0; font-size: 0.9em; text-align: left;">AI Assistance Declaration: This work of science fiction was developed and translated with the assistance of artificial intelligence language models as part of an iterative agentic creative process at EditorIAl IOREB.</p>
        """
    
    files_to_zip["OEBPS/legal.xhtml"] = f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{legal_title}</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
  <div style="margin-top: 3em; font-size: 0.85em; line-height: 1.4;">
    {legal_text}
  </div>
</body>
</html>"""

    has_cover = cover_path.exists()
    if has_cover:
        manifest_items.extend([
            '<item id="cover-page" href="cover.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="cover-image" href="portada.png" media-type="image/png"/>',
        ])
        spine_items.insert(0, '<itemref idref="cover-page"/>')
        files_to_zip["OEBPS/cover.xhtml"] = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Portada</title></head>
<body><div><img src="portada.png" alt="Portada" /></div></body>
</html>"""

    for index, file_path in enumerate(chapter_files, start=1):
        markdown = file_path.read_text(encoding="utf-8")
        html_content = parse_markdown_to_html(markdown)
        chap_id = f"chap_{index:02d}"
        chap_href = f"chapter_{index:02d}.xhtml"
        safe_title = html.escape(chapter_title(markdown, f"Capitulo {index}"))

        files_to_zip[f"OEBPS/{chap_href}"] = f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
{html_content}
</body>
</html>"""

        manifest_items.append(f'<item id="{chap_id}" href="{chap_href}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="{chap_id}"/>')
        nav_points.append(f"""    <navPoint id="navpoint-{index}" playOrder="{index}">
      <navLabel><text>{safe_title}</text></navLabel>
      <content src="{chap_href}"/>
    </navPoint>""")
        toc_links.append(f'<li><a href="{chap_href}">{safe_title}</a></li>')

    toc_title = "Índice" if language == "es" else "Table of Contents"
    files_to_zip["OEBPS/toc.xhtml"] = f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{toc_title}</title>
  <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
  <h1>{toc_title}</h1>
  <ul class="toc-list">
    {"".join(toc_links)}
  </ul>
</body>
</html>"""

    cover_meta = '<meta name="cover" content="cover-image"/>' if has_cover else ""
    files_to_zip["OEBPS/content.opf"] = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{html.escape(title)}</dc:title>
    <dc:creator>{html.escape(author)}</dc:creator>
    <dc:language>{html.escape(language)}</dc:language>
    <dc:identifier id="bookid">urn:uuid:{book_id}</dc:identifier>
    {cover_meta}
  </metadata>
  <manifest>
    {chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
    {chr(10).join(spine_items)}
  </spine>
</package>"""

    files_to_zip["OEBPS/toc.ncx"] = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{book_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{html.escape(title)}</text></docTitle>
  <navMap>
{chr(10).join(nav_points)}
  </navMap>
</ncx>"""

    with zipfile.ZipFile(output_file, "w") as epub:
        epub.writestr("mimetype", files_to_zip["mimetype"], compress_type=zipfile.ZIP_STORED)
        for path, content in files_to_zip.items():
            if path != "mimetype":
                epub.writestr(path, content, compress_type=zipfile.ZIP_DEFLATED)
        if has_cover:
            epub.write(cover_path, "OEBPS/portada.png", compress_type=zipfile.ZIP_DEFLATED)

    return output_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an EPUB file from the project manuscript.")
    parser.add_argument("--project-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--language", default="es")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    output = generate_epub(
        project_root=args.project_root.resolve(),
        language=args.language,
        output=args.output,
    )
    print(f"EPUB generado con exito: {output}")


if __name__ == "__main__":
    main()
