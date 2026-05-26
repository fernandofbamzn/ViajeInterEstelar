---
id: wf_editorial_04_publicacion
title: "Preparacion y Validacion de Publicacion Completa"
scope: editorial
role: "Productor Editorial"
---

# 🎼 Flujo de Trabajo: Publicacion Completa (Ejecutado por el Productor Editorial)

> [!IMPORTANT]
> **Este workflow automatiza la preparacion y validacion de entregables editoriales.** No realiza la subida real a las tiendas, la cual es una accion estrictamente manual y soberana del editor humano.

## 🎭 Rol del Agente
Actuas como **Productor Editorial** (`rol_editorial_productor.md`) en funciones de control de calidad técnica y preparación de empaquetado para tiendas de distribución física y digital (Amazon KDP y Google Play Books).

---

## 🏛️ Referencias Cruzadas e Interdependencias
* **Metadatos Externos:** Depende de la definicion correcta en [es.yml](file:///c:/ReposGit/LuzVieja/metadata/es.yml) y [en.yml](file:///c:/ReposGit/LuzVieja/metadata/en.yml).
* **Control de Calidad Técnica:** Realiza la ejecucion automatica de validacion de placeholders, estructura del EPUB e informe de control de calidad.

---

## 🛠️ Skills Invocadas
* `skill_validar_epub_pdf/SKILL.md`
* `skill_validar_publicacion_kdp_google/SKILL.md`

---

## 📋 Pasos de Ejecución

El script integrador `publicar.py` ejecuta y valida secuencialmente los siguientes 8 pasos:

### Paso 1: Cargar Metadatos
* Leer el archivo de metadatos YAML correspondiente al idioma (`metadata/es.yml` o `metadata/en.yml`).

### Paso 2: Generar LaTeX
* Construir el archivo de marcas LaTeX en la ruta `exportacion/{lang}/` aplicando el escapado robusto de caracteres y normalizando separadores de escena.

### Paso 3: Compilar PDF
* Intentar compilar el archivo `.tex` a PDF usando `pdflatex` en la ruta `exportacion/{lang}/`. En caso de ausencia del binario, registrar la advertencia para compilación manual.

### Paso 4: Generar EPUB
* Compilar los capítulos del manuscrito a formato EPUB reflowable en la ruta `exportacion/{lang}/` integrando la página legal automática y la portada localizada.

### Paso 5: Validar EPUB
* Verificar que la estructura del ZIP de EPUB sea correcta, que contenga todos los capítulos de la novela (exactamente 20) y que el índice de navegación y la página legal estén presentes.

### Paso 6: Generar Ficha KDP
* Generar automáticamente [metadata_kdp.md](file:///c:/ReposGit/LuzVieja/exportacion/es/metadata_kdp.md) conteniendo todos los metadatos requeridos por la plataforma, marcando KDP Select como inactivo para permitir multitienda.

### Paso 7: Generar Ficha Google Play Books
* Generar automáticamente [metadata_google_play.md](file:///c:/ReposGit/LuzVieja/exportacion/es/metadata_google_play.md).

### Paso 8: Generar Informe QC
* Consolidar el estado de todas las pruebas en [report_qc.md](file:///c:/ReposGit/LuzVieja/exportacion/es/report_qc.md) y consolidar todos los entregables finales aprobados en el mismo directorio `exportacion/{lang}/`.

---

## 📤 Entregables del Workflow (Carpeta `exportacion/{lang}/`)
* **EPUB Final:** Maquetación líquida pulida y con índice funcional.
* **PDF / LaTeX Final:** Listo para impresión o compilación local.
* **Metadata Comercial:** Fichas de KDP y Google Play formateadas.
* **Reporte QC:** Informe de validaciones y placeholders.
* **Portada:** Portada final adaptada de la edición.
