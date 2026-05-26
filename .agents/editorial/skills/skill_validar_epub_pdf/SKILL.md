---
name: skill_validar_epub_pdf
title: "Validar Calidad Tecnica de EPUB y PDF"
scope: editorial
description: "Revisa estructura, metadatos, enlaces, tipografia, indices y calidad tecnica de entregables."
inputs:
  - "Archivo EPUB"
  - "Archivo PDF o fuente LaTeX"
outputs:
  - "Informe QA"
  - "Estado tecnico del entregable"
requires_human_approval:
  - "Marcar como definitivo un archivo con incidencias"
---

# ️ Skill: Validar Calidad Técnica de EPUB y PDF (QA Entregables)

Esta habilidad dota al Productor Editorial del protocolo técnico para analizar la integridad estructural, legibilidad y compatibilidad de los ficheros de exportación digital y física antes de enviarlos a entrega local.

##  Objetivo de la Skill
Verificar sistemáticamente que los archivos resultantes no contengan fallos estructurales de visualización, enlaces rotos o metadatos inconsistentes.

---

##  Lista de Verificación (Checklist) de QA

### 1. Validación de EPUB (Edición Digital)
* **Índice y Navegación:** Comprobar la tabla de contenidos (NCX y nav.xhtml). Garantizar que todos los capítulos son accesibles y que la jerarquía es correcta.
* **Metadatos Internos:** Verificar la inclusión correcta de:
  - Título del libro (coincidencia exacta).
  - Autor (coincidencia exacta).
  - Idioma de la edición (código ISO).
  - Identificador único (UUID/ISBN).
* **Cubierta e Imágenes:** Asegurar que la portada está debidamente embebida y declarada como tal en el manifest del EPUB. El tamaño de archivo no debe ser excesivo.
* **Maquetación y Hojas de Estilo:**
  - Controlar que las fuentes embebidas se visualicen y se hayan empaquetado correctamente.
  - Asegurar saltos de página lógicos al inicio de cada capítulo (`page-break-before: always`).
  - Validar compatibilidad en lectores electrónicos populares (Kindle, revisión externa manual, Apple Books) y dispositivos móviles (lectura fluida responsive).
* **Caracteres Especiales:** Verificar que la codificación UTF-8 se aplique estrictamente, evitando caracteres rotos u extraños en diálogos.
* **Notas y Enlaces:** Comprobar que los hipervínculos o notas al pie de página sean bidireccionales y retornen correctamente.

### 2. Validación de PDF y LaTeX (Edición Física)
* **Estructura del LaTeX:** Verificar la compilación libre de errores fatales (*overfull/underfull hbox* críticos).
* **Paginación y Márgenes:** Controlar los márgenes de encuadernación (medianil), sangrías de primera línea y la consistencia en números de página.
* **Consistencia de Portada y Lomo:** Validar el tamaño exacto del lomo físico en relación con el número final de páginas y el gramaje del papel.
* **Imágenes y Colores:** Asegurar que las imágenes del volumen físico estén configuradas en CMYK y con resolución de 300 ppp.

---

##  Output del Proceso
El productor técnico genera un informe estructurado de QA con uno de los siguientes estados técnicos recomendados:

* `no_listo`: Presenta fallos de compilación fatales, archivos dañados o falta de metadatos básicos.
* `requiere_correcciones`: El archivo compila, pero tiene desajustes visuales, notas rotas, falta la portada o tiene fallos menores.
* `listo_para_publicacion_manual`: Cumple con el 100% de los estándares de visualización y metadatos.
