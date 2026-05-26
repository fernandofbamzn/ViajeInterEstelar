---
id: wf_editorial_08_productor_entregables
title: "Productor de Entregables y Composición Técnica"
scope: editorial
role: "Productor Editorial"
---

# 🎼 Flujo de Trabajo: Productor de Entregables (Ejecutado por el Productor Editorial)

## 🎭 Rol del Agente
Actúas como **Productor Editorial** (`rol_editorial_productor.md`) en tu función de maquetador técnico. Te responsabilizas de la estructura técnica de los archivos fuente y de la correcta compilación de los formatos de lectura física y digital de la editorial.

---

## 🏛️ Referencias Cruzadas e Interdependencias
* **Compilación Técnica Inicial:** Este flujo se encarga de estructurar y generar las fuentes.
* **Control de Calidad (QA):** Una vez generados los archivos intermedios o finales, se debe activar obligatoriamente el flujo `wf_editorial_14_qa_epub_pdf.md` para validar su visualización.

---

## 🛠️ Skills Invocadas
* `skill_formatear_latex/SKILL.md`
* `skill_preparar_portada_localizada/SKILL.md`

---

## ⚖️ Rules de Referencia Obligatorias
* `regla_editorial_01_calidad_minima.md`
* `regla_editorial_06_seguridad_operativa.md`

---

## 📋 Pasos de Ejecución

### Paso 1: Recopilación e Indexación
* Leer el perfil de proyecto activo (`manifest.yaml`) para ubicar el manuscrito, la trama y el canon.
* Comprobar que todos los capítulos están listos y no tienen anotaciones o textos pendientes.

### Paso 2: Conversión Tipográfica y de Formato
* Emplear la skill `skill_formatear_latex` para transpolar el texto Markdown del manuscrito original al formato tipográfico de libro físico o digital.
* Configurar márgenes, hojas de estilo, preámbulos y la tabla de contenidos general.

### Paso 3: Empaquetamiento y Exportación
* Generar los ficheros `.tex` u otros formatos intermedios (como HTML para EPUB).
* > [!WARNING]
  > **requires_human_approval**: Se requiere confirmación explícita del usuario humano antes de sobrescribir archivos finales de maquetación en la carpeta de exportación activa o al alterar los scripts de exportación existentes.

---

## 📋 Checklist de Validación del Workflow
- [ ] La secuencia de capítulos es correcta.
- [ ] Los diálogos y acotaciones se ajustan a la tipografía exigida.
- [ ] Los metadatos de título y autor coinciden con la ficha del libro.
- [ ] Los archivos intermedios de maquetación se han generado en `exportacion/{idioma}/`.

---

## 📤 Entregables
* **Archivos fuente de maquetación (.tex, HTML/CSS).**
* **Fuentes de portada y cubiertas preliminares.**
