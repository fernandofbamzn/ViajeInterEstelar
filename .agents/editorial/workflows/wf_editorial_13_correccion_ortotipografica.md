---
id: wf_editorial_13_correccion_ortotipografica
title: "Correccion Ortotipografica"
scope: editorial
role: "Corrector Ortotipografico"
description: "Corrige ortografia, puntuacion, dialogos y convenciones mecanicas sin alterar voz ni canon."
inputs:
  - "Capitulo o fragmento"
  - "Modo de ejecucion"
outputs:
  - "Informe de correccion"
  - "Texto corregido o patch propuesto"
requires_human_approval:
  - "Sobrescribir el manuscrito original"
---

#  Workflow: Corrección Ortotipográfica y Control Mecánico del Texto

Este workflow describe las etapas de corrección mecánica que el **Corrector Ortotipográfico** aplica sobre los capítulos de la novela para garantizar su pulcritud formal.

---

##  Roles Involucrados
* **Corrector Ortotipográfico:** Ejecuta las pruebas y revisiones.
* **Editor de Mesa:** Supervisa y asegura que las correcciones no dañen el tono literario.
* **CEO:** Aprueba la aplicación definitiva del texto.

---

## ️ Skills Invocadas
* `skill_corregir_ortotipografia/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_editorial_01_calidad_minima.md`
* `regla_editorial_05_separacion_roles.md`

---

## ️ Modos de Ejecución
Este workflow opera bajo tres modalidades diferenciadas que el usuario o el CEO deben seleccionar en el prompt:

1. **`modo_informe` (Por Defecto):** El Corrector analiza el texto del capítulo y genera un listado con los errores detectados (errores de raya de diálogo, comillas, acentos, erratas) en `exportacion/{idioma}/informe_ortotipografia.md`, indicando la línea y la corrección sugerida. **No modifica el manuscrito.**
2. **`modo_sugerencias`:** El Corrector genera un archivo diff o borrador paralelo del capítulo (ej: `capitulo_01.sug.md`) para que el usuario o el Editor de Mesa puedan contrastar los cambios de manera visual antes de aplicarlos.
3. **`modo_aplicacion_controlada`:** El Corrector aplica directamente los cambios sobre el manuscrito original, limitándose exclusivamente a las erratas ortográficas directas y los signos de puntuación estructurales.

---

##  Pasos del Proceso

### Paso 1: Carga del Capítulo de Manuscrito
* Importar el archivo `.md` del capítulo correspondiente del manuscrito activo.

### Paso 2: Análisis Ortográfico y Gramatical
* Ejecutar un escaneo del texto para contrastar palabras dudosas con la RAE (o equivalente localizado).
* Detectar inconsistencias en la escritura de nombres del canon (ej: `Kael'thin`, `La Burbuja`, `Nadia`).

### Paso 3: Análisis Tipográfico y de Diálogos
* Identificar si las rayas de diálogo (``) y los signos dobles de apertura y cierre están correctamente posicionados y no tienen espacios en blanco sobrantes.

### Paso 4: Generación de Entregable según Modo
* Si se opera en `modo_informe`, redactar el reporte detallado y finalizar.
* Si se opera en `modo_sugerencias`, generar el borrador diff.
* Si se opera en `modo_aplicacion_controlada`:
  > [!WARNING]
  > **requires_human_approval**: Se requiere confirmación explícita del usuario humano antes de sobrescribir el archivo del manuscrito original en `manuscrito/`.
