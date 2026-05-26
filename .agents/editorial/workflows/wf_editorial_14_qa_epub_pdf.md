---
id: wf_editorial_14_qa_epub_pdf
title: "QA técnico de EPUB y PDF"
scope: editorial
role: "Productor Editorial"
description: "Valida artefactos EPUB, PDF y LaTeX en entorno local antes de revisión humana."
inputs:
  - "Archivo EPUB"
  - "Archivo PDF o fuente LaTeX"
  - "Metadatos internos"
outputs:
  - "Informe de QA"
  - "Dictamen de estado"
requires_human_approval:
  - "Catalogar como definitivo un artefacto con incidencias"
---

# Workflow Editorial 14 — QA EPUB/PDF local

Valida integridad técnica de artefactos en `exportacion/{idioma}/`.

## Pasos
1. Detectar idioma y artefactos (`novela.epub`, `novela.pdf`, `novela.tex`).
2. Ejecutar validación de estructura EPUB.
3. Revisar compilación PDF/LaTeX y calidad tipográfica.
4. Verificar metadatos internos contra `manifest.yaml`.
5. Emitir `qa_report_entregables.md`.

## Estados válidos
- `no_listo`
- `requiere_correcciones`
- `validado_para_revision_humana`
- `entrega_local_preparada`

Este workflow no publica, no sube archivos y no realiza distribución externa.
#  Workflow: Control de Calidad y QA Técnico de EPUB y PDF

Este workflow detalla los pasos de verificación sistemática que el **Productor Editorial** realiza sobre los archivos compilados de la obra para certificar su conformidad técnica antes de pasar a manos del editor humano para su entrega local.

> [!IMPORTANT]
> Este workflow no publica de forma automatizada. Su función exclusiva es validar la calidad técnica de los entregables y asegurar que estén libres de fallos visuales o estructurales.

---

##  Roles Involucrados
* **Productor Editorial:** Ejecuta la compilación y realiza las auditorías de visualización y código.
* **CEO:** Supervisa el estado de los entregables y archiva los informes.

---

## ️ Skills Invocadas
* `skill_validar_epub_pdf/SKILL.md`
* `skill_formatear_latex/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_editorial_01_calidad_minima.md`
* `regla_editorial_04_no_publicar_sin_revision_humana.md`
* `regla_editorial_06_seguridad_operativa.md`

---

##  Pasos del Proceso

### Paso 1: Identificación de la Edición, Idioma y Artefactos
* Determinar el proyecto activo, el idioma objetivo (es, en, etc.) y recuperar la ruta de compilación (`exportacion/{idioma}/`).
* Localizar los archivos generados: `novela.epub`, `novela.pdf` o fuentes `novela.tex`.

### Paso 2: Validación del Archivo Digital (QA EPUB)
* Ejecutar la skill `skill_validar_epub_pdf` enfocándose en:
  - Estructura interna de navegación.
  - Corrección de enlaces de notas al pie.
  - Comprobación de que la portada se renderice a pantalla completa en dispositivos de prueba.

### Paso 3: Validación del Archivo Físico (QA PDF / LaTeX)
* Analizar la salida de la compilación LaTeX en busca de advertencias críticas de desbordamiento de caja u oraciones cortadas.
* Revisar visualmente la disposición de las páginas de cortesía, dedicatoria e índice físico.

### Paso 4: Validación de Metadatos Internos
* Extraer el archivo de metadatos embebido en el EPUB/PDF y cruzarlo con la información activa de `manifest.yaml` para asegurar coincidencia perfecta de título, subtítulo e identificadores.

### Paso 5: Emisión de Informe de QA
* Redactar un reporte de estado técnico detallado en `exportacion/{idioma}/qa_report_entregables.md` registrando observaciones y sugiriendo uno de estos estados recomendados:
  - `no_listo`
  - `requiere_correcciones`
  - `listo_para_publicacion_manual`

> [!WARNING]
> **requires_human_approval**: Ningún archivo que tenga un reporte de QA en estado `no_listo` o `requiere_correcciones` podrá ser catalogado como definitivo o promovido para su subida. El productor técnico deberá subsanar las observaciones y reiniciar este workflow.
