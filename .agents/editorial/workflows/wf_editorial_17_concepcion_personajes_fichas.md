---
id: wf_editorial_17_concepcion_personajes_fichas
title: "Concepcion de Personajes y Fichas"
scope: editorial
role: "Creador de Concepto"
description: "Disena protagonistas, antagonistas, secundarios, relaciones y fichas dramaticas."
inputs:
  - "Ambientacion aprobada"
  - "Facciones o premisa"
outputs:
  - "Fichas de personajes"
  - "Mapa de relaciones"
requires_human_approval:
  - "Aprobar elenco final"
  - "Registrar fichas definitivas en la biblia"
---

#  Workflow: Concepción de Personajes y Creación de Fichas

Este workflow detalla las fases secuenciales que el **Creador de Concepto** ejecuta para diseñar y estructurar la ficha identitaria, psicología y red de relaciones de los personajes de la obra.

---

##  Roles Involucrados
* **Creador de Concepto:** Diseña los perfiles, arquetipos y dinámicas dramáticas.
* **Escritor:** Supervisa para asegurar que las fichas se traducen en arcos de personajes fluidos durante la futura redacción.

---

## ️ Skills Invocadas
* `skill_desarrollo_personajes_base/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_editorial_01_calidad_minima.md`
* `regla_genero_05_tono_contemplativo.md` (o pautas estilísticas del género)
* `regla_editorial_11_estructura_proyecto_novela.md`

---

##  Pasos del Proceso

### Paso 1: Carga de la Ambientación y Facciones
* Revisar `biblia/mundo/`, `biblia/tecnologia/` y `biblia/personajes/` para entender el ecosistema social y las facciones en juego, de manera que los personajes estén integrados de forma orgánica en el mundo.

### Paso 2: Diseño de los Protagonistas y Antagonistas
* Aplicar la skill `skill_desarrollo_personajes_base` para diseñar las fichas de los personajes principales.
* Asegurar que se definen claramente:
  - La mentira que creen.
  - Su deseo consciente y necesidad inconsciente.
  - El conflicto interno motor.

### Paso 3: Diseño de Personajes Secundarios
* Desarrollar fichas simplificadas para personajes secundarios clave (mentores, aliados, catalizadores).

### Paso 4: Mapeado de la Red de Relaciones y Fricciones
* Dibujar un diagrama conceptual o tabla de dinámicas de interrelación (ej: alianzas históricas, deudas de gratitud, diferencias ideológicas).

### Paso 5: Registro de Fichas en la Biblia
* Escribir cada ficha de personaje en `biblia/personajes/{nombre_personaje}.md` y actualizar el índice general en `biblia/personajes/README.md`.

> [!WARNING]
> **requires_human_approval**: El elenco definitivo de personajes y sus dinámicas emocionales deben ser validados y aprobados explícitamente por el usuario humano antes de dar por cerrada esta fase.
