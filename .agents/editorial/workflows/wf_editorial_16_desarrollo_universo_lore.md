---
id: wf_editorial_16_desarrollo_universo_lore
title: "Desarrollo de Universo y Lore"
scope: editorial
role: "Creador de Concepto y Lorekeeper"
description: "Desarrolla marco fisico, cultura, facciones, linguistica y documentos de lore."
inputs:
  - "Premisa aprobada"
  - "Perfil de genero"
outputs:
  - "Dossier de worldbuilding"
  - "Propuesta de consolidacion de biblia"
requires_human_approval:
  - "Consolidar leyes fisicas o lore en la biblia"
---

#  Workflow: Desarrollo de Universo y Diseño de Lore (Expandido)

Este workflow guía al **Creador de Concepto** en la estructuración sistemática del worldbuilding, la antropología ficticia, las jergas y la creación de artefactos in-universe, cimentando la Biblia de Lore en su espectro más amplio.

---

##  Roles Involucrados
* **Creador de Concepto:** Diseña el worldbuilding físico, cultural y lingüístico de la obra.
* **Experto en Lore / Lorekeeper:** Custodia la consistencia del canon científico e histórico del proyecto.

---

## ️ Skills Invocadas
* `skill_diseno_worldbuilding/SKILL.md`
* `skill_desarrollo_lore_profundo/SKILL.md`
* `skill_extrapolar_ciencia_dura/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_genero_01_ciencia_dura.md`
* `regla_editorial_06_seguridad_operativa.md`
* `regla_editorial_11_estructura_proyecto_novela.md`

---

##  Pasos del Proceso

### Paso 1: Carga y Definición del Marco Físico
* Cargar la premisa autorizada en `trama/premisas/`.
* Invocar la skill `skill_diseno_worldbuilding` para definir la geología, astrofísica, ecología y dinámicas socio-técnicas principales de la obra.

### Paso 2: Desarrollo Antropológico y Lingüístico
* Invocar la skill `skill_desarrollo_lore_profundo` para detallar la vertiente sociocultural de cada facción o especie.
* Diseñar la jerga, modismos lingüísticos y bases de conlangs que darán identidad a los diálogos.
* Trazar el panorama de mitos de creación, religiones vigentes, tabúes y costumbres rituales de los personajes.

### Paso 3: Elaboración de Artefactos In-Universe
* Escribir extractos de diarios, bitácoras espaciales, correspondencia o bases de datos ficticias que ayuden a contextualizar la historia.
* Estos artefactos se guardarán como propuesta bajo la seccion correspondiente de `biblia/mundo/` o `biblia/tecnologia/`, segun su naturaleza, para ser utilizados como material de lore o paratexto.

### Paso 4: Consolidación de la Enciclopedia de Lore
* Organizar y registrar los entregables resultantes en `biblia/mundo/` para cultura, historia, geografia o politica, y en `biblia/tecnologia/` para ciencia aplicada, sistemas tecnicos y limites fisicos.

---

##  Reglas de Confirmación
* > [!WARNING]
  > **requires_human_approval**: La consolidación final de la Biblia de Lore (incluyendo las leyes de la física, bases culturales de facciones, conlangs e hitos históricos consolidantes) requiere la aprobación del usuario antes de pasar a la fase de diseño de tramas o redacción del borrador.
