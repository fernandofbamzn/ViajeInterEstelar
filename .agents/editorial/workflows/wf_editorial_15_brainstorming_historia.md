---
id: wf_editorial_15_brainstorming_historia
title: "Brainstorming de Historia y Seleccion de Premisa"
scope: editorial
role: "Creador de Concepto"
description: "Genera, filtra y desarrolla premisas semilla para nuevos proyectos literarios."
inputs:
  - "Restricciones creativas del usuario"
  - "Genero o mercado objetivo"
outputs:
  - "Reporte de premisas"
  - "Pitch de premisa seleccionada"
requires_human_approval:
  - "Iniciar formalmente un nuevo proyecto literario"
---

#  Workflow: Brainstorming de Historia y Selección de Premisa

Este workflow describe las fases sistemáticas que el **Creador de Concepto** ejecuta para madurar ideas narrativas iniciales y elegir el "high concept" de un nuevo proyecto literario.

---

##  Roles Involucrados
* **Creador de Concepto:** Genera las ideas, realiza el filtrado y redacta el informe final de premisa.
* **CEO:** Evalúa la viabilidad comercial y autoriza la apertura del proyecto.

---

## ️ Skills Invocadas
* `skill_brainstorming_premisas/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_editorial_01_calidad_minima.md`
* `regla_editorial_07_no_imitacion_copyright.md`
* `regla_editorial_11_estructura_proyecto_novela.md`

---

##  Pasos del Proceso

### Paso 1: Apertura de Sesión de Brainstorming
* Definir los parámetros generales deseados (género primario, mercado objetivo o restricciones especiales planteadas por el usuario).
* Realizar un escaneo del mercado para identificar tendencias de interés sin perder la identidad artística de la editorial.

### Paso 2: Generación y Contraste de Ideas Semilla
* Aplicar la skill `skill_brainstorming_premisas` para estructurar un mínimo de 3 propuestas conceptuales diferenciadas.
* Contrastar las propuestas valorando su originalidad, viabilidad científica (si es ciencia ficción dura) y profundidad dramática.

### Paso 3: Selección y Desarrollo de Pitch Comercial
* Elegir la premisa ganadora de forma colaborativa con el usuario humano.
* Desarrollar el One-liner, la atmósfera sugerida y una sinopsis semilla.

### Paso 4: Creación de la Ficha Técnica del Proyecto
* Escribir el dossier de premisa en `trama/premisas/idea_seleccionada.md`.
* Si se inicia una novela nueva, proponer la estructura normalizada completa antes de crear contenido canonico: `manuscrito/`, `trama/`, `trama/premisas/`, `trama/escaletas/`, `biblia/personajes/`, `biblia/mundo/`, `biblia/tecnologia/`, `exportacion/{idioma}/`, `traducciones/{idioma}/` y `costes/`.

> [!WARNING]
> **requires_human_approval**: La elección definitiva de la premisa de la novela a desarrollar y el inicio formal del proyecto requieren la autorización explícita del usuario humano. El agente no podrá avanzar a la fase de worldbuilding o creación de personajes sin el visto bueno de la idea semilla.
