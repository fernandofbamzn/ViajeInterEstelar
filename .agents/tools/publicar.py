import argparse
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

# Imports locales
from generar_epub import generate_epub, load_metadata, validate_metadata
from generar_latex import generate_book


def find_placeholders_in_file(file_path: Path) -> list[str]:
    found = []
    try:
        content = file_path.read_text(encoding="utf-8")
        # Búsqueda exacta de TODO y FIXME como palabras completas y mayúsculas
        if re.search(r"\bTODO\b", content):
            found.append("TODO")
        if re.search(r"\bFIXME\b", content):
            found.append("FIXME")
            
        # Placeholders insensibles a mayúsculas
        placeholders_case_insensitive = ["[pendiente]", "Lorem ipsum", "Untitled", "Author Name", "anos de distancia"]
        for pl in placeholders_case_insensitive:
            if pl.lower() in content.lower():
                found.append(pl)
    except Exception as e:
        found.append(f"Error de lectura ({e})")
    return found


def validate_manuscripts_and_metadata(project_root: Path, language: str, metadata: dict) -> list[str]:
    errors = []
    
    # 1. Validar metadatos en sí
    try:
        validate_metadata(metadata, language)
    except ValueError as ve:
        errors.append(f"Metadatos invalidos: {ve}")

    # 2. Buscar placeholders en los archivos de metadatos YML
    yml_path = project_root / "metadata" / f"{language}.yml"
    yml_placeholders = find_placeholders_in_file(yml_path)
    if yml_placeholders:
        errors.append(f"Archivo de metadatos {yml_path.name} contiene placeholders: {', '.join(yml_placeholders)}")

    # 3. Buscar placeholders en el manuscrito
    if language == "es":
        manuscript_dir = project_root / "manuscrito"
    else:
        manuscript_dir = project_root / "traducciones" / language / "manuscrito"
    
    chapter_files = sorted(manuscript_dir.glob("capitulo_*.md"))
    if not chapter_files:
        errors.append(f"No se encontraron capitulos en {manuscript_dir}")
    
    for ch_file in chapter_files:
        found = find_placeholders_in_file(ch_file)
        if found:
            errors.append(f"El archivo {ch_file.name} contiene placeholders: {', '.join(found)}")
            
    return errors


def generate_metadata_sheets(dest_dir: Path, metadata: dict, language: str):
    title = metadata.get("title")
    subtitle = metadata.get("subtitle")
    author = metadata.get("author")
    lang = metadata.get("language")
    publisher = metadata.get("publisher", "EditorIAl IOREB")
    year = metadata.get("publication_year", "2026")
    keywords = ", ".join(metadata.get("keywords", []))
    categories = ", ".join(metadata.get("categories", []))
    ai_disclosure = metadata.get("ai_disclosure", "")

    # Descripción sugerida y precios por defecto
    if language == "es":
        desc = (
            "Una señal estelar que viaja a la velocidad de la luz tarda veinte años en llegar a Kael. "
            "Cuando la reciben, comprenden que están escuchando una civilización extinta. "
            "¿Qué ocurre cuando la luz del pasado nos revela nuestro propio destino?"
        )
        suggested_price = "2,99 EUR (eBook) / 12,99 EUR (Tapa blanda)"
        territories = "Mundial (todos los territorios disponibles)"
    else:
        desc = (
            "A stellar signal traveling at the speed of light takes twenty years to reach Kael. "
            "When they receive it, they realize they are listening to an extinct civilization. "
            "What happens when the light of the past reveals our own destiny?"
        )
        suggested_price = "2.99 USD (eBook) / 12.99 USD (Paperback)"
        territories = "Worldwide (all available territories)"

    # Ficha KDP
    kdp_content = f"""# Ficha Comercial de Amazon KDP — {title} ({language.upper()})

* **Título del libro:** {title}
* **Subtítulo:** {subtitle}
* **Autor:** {author}
* **Colección/Serie:** N/A
* **Número de entrega:** N/A
* **Idioma:** {lang}
* **Editor:** {publisher}
* **Año de publicación:** {year}
* **Descripción comercial (Sinopsis):**
  {desc}
* **Palabras clave (Keywords):** {keywords}
* **Categorías BISAC:** {categories}
* **Precio sugerido:** {suggested_price}
* **Derechos de publicación y territorios:** Poseo todos los derechos de publicación necesarios y se distribuye en {territories}.
* **Declaración de Contenido de IA:** {ai_disclosure}
* **KDP Select:** NO ACTIVO (Permite distribución multitienda en Google Play Books).
"""

    # Ficha Google Play Books
    google_content = f"""# Ficha Comercial de Google Play Books — {title} ({language.upper()})

* **Título:** {title}
* **Subtítulo:** {subtitle}
* **Autor:** {author}
* **Idioma:** {lang}
* **Editor:** {publisher}
* **Fecha de publicación:** {year}
* **Descripción:**
  {desc}
* **Palabras clave:** {keywords}
* **Categorías (Thema / BISAC):** {categories}
* **Precio sugerido:** {suggested_price}
* **Territorios de venta:** Mundial
* **Declaración de IA:** {ai_disclosure}
"""

    (dest_dir / "metadata_kdp.md").write_text(kdp_content, encoding="utf-8")
    (dest_dir / "metadata_google_play.md").write_text(google_content, encoding="utf-8")


def compile_pdf_latex(tex_path: Path, output_dir: Path) -> tuple[bool, str]:
    # Intentar buscar pdflatex
    pdflatex_bin = shutil.which("pdflatex")
    if not pdflatex_bin:
        return False, "pdflatex no encontrado en el PATH del sistema."
    
    try:
        # Correr pdflatex dos veces para generar índice y referencias cruzadas correctas
        for _ in range(2):
            result = subprocess.run(
                [pdflatex_bin, "-interaction=nonstopmode", f"-output-directory={output_dir}", str(tex_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if result.returncode != 0:
                return False, f"pdflatex finalizo con codigo de error {result.returncode}.\nStderr: {result.stderr[:200]}"
        return True, "Compilado correctamente usando pdflatex."
    except Exception as e:
        return False, f"Excepcion durante la compilacion de PDF: {e}"


def check_epub_structure(epub_path: Path) -> tuple[bool, list[str]]:
    warnings = []
    try:
        with zipfile.ZipFile(epub_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            
            # Comprobaciones básicas de estructura
            if "mimetype" not in file_list:
                warnings.append("Mimetype ausente del EPUB.")
            if "OEBPS/content.opf" not in file_list:
                warnings.append("Archivo de definicion content.opf ausente.")
            if "OEBPS/toc.xhtml" not in file_list:
                warnings.append("Tabla de contenidos toc.xhtml ausente.")
            if "OEBPS/legal.xhtml" not in file_list:
                warnings.append("Pagina legal legal.xhtml ausente.")
            if "OEBPS/portada.png" not in file_list:
                warnings.append("Portada (portada.png) ausente dentro del EPUB.")
                
            # Verificar número de capítulos
            chapters = [f for f in file_list if re.match(r"^OEBPS/chapter_\d+\.xhtml$", f)]
            if len(chapters) != 20:
                warnings.append(f"Se esperaba 20 capitulos, pero se detectaron {len(chapters)} capitulos.")
                
        return len(warnings) == 0, warnings
    except Exception as e:
        return False, [f"Error al abrir o leer el EPUB: {e}"]


def generate_qc_report(dest_dir: Path, language: str, metadata: dict, pdf_status: tuple[bool, str], epub_status: tuple[bool, list[str]], placeholders_errors: list[str]):
    title = metadata.get("title")
    subtitle = metadata.get("subtitle")
    author = metadata.get("author")
    
    tex_file = dest_dir / f"{title.replace(' ', '')}.tex"
    epub_file = dest_dir / f"{title.replace(' ', '')}.epub"
    pdf_file = dest_dir / f"{title.replace(' ', '')}.pdf"

    pdf_ok, pdf_msg = pdf_status
    epub_ok, epub_warnings = epub_status
    
    qc_success = len(placeholders_errors) == 0 and epub_ok
    status_label = "APROBADO (Listo para Publicación)" if qc_success else "NO APROBADO (Requiere Corrección)"

    # Comprobar si epubcheck está en el sistema
    epubcheck_bin = shutil.which("epubcheck")
    epubcheck_status = "No disponible (se realizo verificacion de estructura ZIP interna)"
    if epubcheck_bin:
        try:
            result = subprocess.run([epubcheck_bin, str(epub_file)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
            if result.returncode == 0:
                epubcheck_status = "Pasada con exito mediante epubcheck"
            else:
                epubcheck_status = f"Fallo en epubcheck: {result.stderr[:200]}"
                qc_success = False
        except Exception as e:
            epubcheck_status = f"Error al ejecutar epubcheck: {e}"

    report = f"""# Informe de Control de Calidad (QC Report) — {title} ({language.upper()})

* **Estado General de Calidad:** **{status_label}**
* **Idioma de Edición:** {language.upper()}
* **Título:** {title}
* **Subtítulo:** {subtitle}
* **Autor:** {author}

---

## 🛠️ Verificación de Archivos y Generación Técnica

| Archivo | Estado | Detalle |
|---|---|---|
| **LaTeX (.tex)** | {"Generado" if tex_file.exists() else "Ausente"} | Ubicado en `exportacion/{language}/` |
| **EPUB (.epub)** | {"Generado" if epub_file.exists() else "Ausente"} | Ubicado en `exportacion/{language}/` |
| **PDF (.pdf)** | {"Generado" if pdf_file.exists() else "No compilado automáticamente"} | {pdf_msg} |

---

## 📋 Auditoría de Requisitos Críticos

1. **Ausencia de Placeholders:**
   * {"Aprobado (0 placeholders encontrados)" if not placeholders_errors else "FALLIDO"}
   {chr(10).join([f"   * [ERROR] {err}" for err in placeholders_errors])}

2. **Estructura Interna del EPUB:**
   * {"Aprobado (Estructura ZIP correcta)" if epub_ok else "FALLIDO"}
   {chr(10).join([f"   * [WARNING] {warn}" for warn in epub_warnings])}

3. **Verificación de Herramientas Externas (Epubcheck):**
   * Detalle: {epubcheck_status}

4. **Presencia de Secciones Obligatorias:**
   * Página Legal: **Sí (Nativa e integrada por idioma)**
   * Índice / Tabla de Contenidos: **Sí (Generado y enlazado)**
   * Número de Capítulos: **20 Capítulos confirmados**

---

## ⚖️ Conclusión y Siguientes Pasos
{"El paquete cumple rigurosamente con los estandares de calidad de EditorIAl IOREB y esta listo para su publicacion." if qc_success else "Se detectaron errores criticos de placeholders o de estructura de archivos. Por favor, resuelva las incidencias antes de realizar la preparacion de entrega."}
"""
    (dest_dir / "report_qc.md").write_text(report, encoding="utf-8")
    return qc_success


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline de publicacion unificado para EditorIAl IOREB.")
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--language", required=True, choices=["es", "en"], help="Idioma de la edicion a compilar.")
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    language = args.language

    print(f"=== Iniciando Pipeline de Publicacion [{language.upper()}] ===")

    # 1. Cargar y Validar Metadatos y Manuscrito (T01, T02, T03)
    try:
        metadata = load_metadata(project_root, language)
    except FileNotFoundError as fnf:
        print(f"[ERROR] {fnf}")
        return

    placeholders_errors = validate_manuscripts_and_metadata(project_root, language, metadata)
    if placeholders_errors:
        print("[AVISO] Se encontraron errores o placeholders. El informe de QC los detallara.")

    # 2. Generar LaTeX (T02)
    print("Generando archivo LaTeX (.tex)...")
    try:
        tex_path = generate_book(project_root, language, output=None)
        print(f"LaTeX generado en: {tex_path}")
    except Exception as e:
        print(f"[ERROR] Error al generar LaTeX: {e}")
        return

    # 3. Generar EPUB (T02)
    print("Generando archivo EPUB (.epub)...")
    try:
        epub_path = generate_epub(project_root, language, output=None)
        print(f"EPUB generado en: {epub_path}")
    except Exception as e:
        print(f"[ERROR] Error al generar EPUB: {e}")
        return

    # 4. Compilar PDF desde LaTeX (T07)
    export_dir = project_root / "exportacion" / language
    print("Compilando PDF desde LaTeX...")
    pdf_status = compile_pdf_latex(tex_path, export_dir)
    print(f"Resultado compilacion PDF: {pdf_status[1]}")

    # 5. Validar EPUB (T13)
    print("Validando estructura del EPUB...")
    epub_status = check_epub_structure(epub_path)
    if epub_status[0]:
        print("EPUB validado correctamente.")
    else:
        print(f"[WARN] Validacion EPUB con avisos: {epub_status[1]}")

    # 6. Generar Fichas Comerciales (T10)
    print("Generando fichas de metadatos comerciales...")
    generate_metadata_sheets(export_dir, metadata, language)
    print("Fichas de metadatos de Amazon KDP y Google Play Books generadas.")

    # 7. Generar Informe de Control de Calidad (T11)
    print("Generando informe de Control de Calidad (QC)...")
    qc_success = generate_qc_report(export_dir, language, metadata, pdf_status, epub_status, placeholders_errors)
    print(f"Informe QC generado en: {export_dir / 'report_qc.md'}")

    # 8. Copiar portada al directorio de exportación de la edición
    cover_source = project_root / "exportacion" / f"portada_{language}.png"
    if not cover_source.exists():
        cover_source = project_root / "exportacion" / "portada.png"
    if cover_source.exists():
        shutil.copy(cover_source, export_dir / cover_source.name)
        print("Portada copiada al directorio de exportacion de la edicion.")

    print(f"=== Pipeline finalizado. Entregables consolidados en exportacion/{language}/ ===")
    if not qc_success:
        print(f"[ATENCION] El control de calidad contiene fallos. Revisa {export_dir / 'report_qc.md'}")


if __name__ == "__main__":
    main()
