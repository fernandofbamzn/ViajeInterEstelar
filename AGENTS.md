# AGENTS.md — Gobernanza raíz de EditorIAl IOREB

Este repositorio contiene la infraestructura agéntica de **EditorIAl IOREB**.

## Fuente de verdad
- El archivo canónico de resolución dinámica es: `.agents/manifest.yaml`.
- El CEO/Orquestador debe resolver desde ese manifiesto:
  - `active_project.id`
  - `active_project.genre`
  - rutas canónicas, roles, workflows, skills y rules.

## Flujo operativo obligatorio
Usuario humano -> CEO/Orquestador -> Rol -> Workflow -> Skill -> Rule -> Entregable validado

## Política de alcance
- No modificar `manuscrito/`, `biblia/` ni `trama/` sin aprobación humana explícita.
- Los agentes **no** publican, no suben ni distribuyen externamente.
- Los agentes solo preparan artefactos locales exportables (`.md`, `.txt`, `.epub`, `.pdf`, `.tex`, etc.).
- La publicación/distribución externa la realiza manualmente el usuario humano.

## Estructura canónica
- Núcleo: `.agents/editorial/`, `.agents/generos/`, `.agents/novelas/`.
- Wrappers opcionales/no canónicos: `.agents/rules/`, `.agents/skills/`, `.agents/workflows/`.

## Nota
`.agents/AGENTS.md` amplía esta gobernanza para la operación interna editorial.
