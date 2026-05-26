---
id: regla_editorial_11_estructura_proyecto_novela
title: "Estructura Normalizada de Proyecto de Novela"
scope: editorial
trigger: always_on
description: "Obliga a mantener una estructura editorial minima para toda novela gestionada por agentes."
inputs:
  - ".agents/manifest.yaml"
  - "project_profile.md"
  - "Arbol de carpetas del proyecto"
outputs:
  - "Estructura de novela validada"
  - "Listado de secciones faltantes"
requires_human_approval:
  - "Mover o reestructurar contenido canonico existente"
---

# Estructura Normalizada de Proyecto de Novela

## Directriz
Todo proyecto de novela debe separar manuscrito, trama, personajes, mundo, tecnologia, traducciones, exportacion y costes. Ningun workflow debe mezclar borradores, canon y entregables finales en una misma carpeta.

## Estructura Minima
* `manuscrito/`: capitulos o escenas redactadas.
* `trama/`: premisas, escaletas, cronologia, plan futuro y decisiones de estructura.
* `trama/premisas/`: ideas semilla, pitches y premisa aprobada.
* `trama/escaletas/`: escaletas por bloque, parte o capitulo.
* `biblia/`: canon consolidado.
* `biblia/personajes/`: fichas, arcos y relaciones.
* `biblia/mundo/`: geografia, historia, politica, biologia, cultura y contexto.
* `biblia/tecnologia/`: sistemas tecnicos, ciencia aplicada, limites y supuestos.
* `traducciones/{idioma}/`: traduccion, glosario, guia de estilo, metadatos y auditorias.
* `exportacion/{idioma}/`: LaTeX, EPUB, PDF, assets y artefactos generados por idioma.
* `costes/`: ledger de tokens, costes de herramientas y resumen financiero.

## Reglas de Uso
* El CEO debe comprobar esta estructura antes de iniciar un proyecto nuevo.
* El Creador de Concepto solo puede proponer premisas en `trama/premisas/` hasta que el usuario apruebe una.
* El Lorekeeper registra canon aprobado en `biblia/`; antes de la aprobacion, trabaja con propuestas o dossiers.
* El Productor escribe exportables en `exportacion/{idioma}/`, nunca dentro de `.agents/tools/`.
* Los scripts de `.agents/tools/` son herramientas reutilizables, no carpetas de salida.

## Compatibilidad con Proyectos Existentes
Si una novela antigua usa una organizacion previa, el agente debe crear indices puente o proponer una migracion. No debe mover ni borrar canon existente sin aprobacion humana.
