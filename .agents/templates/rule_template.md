---
id: regla_[nivel]_[nombre_corto]
title: "Titulo descriptivo de la regla"
scope: editorial | genre | novel
project: "[id_novela_si_aplica]"
genre: "[id_genero_si_aplica]"
trigger: "always_on | conditional"
description: "Problema operativo que evita esta regla."
inputs:
  - "Contexto que debe revisar el agente"
outputs:
  - "Comportamiento o dictamen esperado"
requires_human_approval:
  - "Acciones que bloquea hasta aprobacion humana"
---

# Titulo de la Regla

## Contexto y Motivacion
[Explica brevemente por que existe esta regla y que problema evita.]

## Directriz Inviolable
[Define de manera explicita la regla que el agente debe obedecer.]

## Lo que NUNCA debe hacerse
* [Ejemplo de accion prohibida]
* [Ejemplo de accion prohibida]

## Comportamiento Esperado
* [Ejemplo de accion permitida/correcta]
* [Ejemplo de accion permitida/correcta]
