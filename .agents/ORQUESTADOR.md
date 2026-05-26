# ORQUESTADOR.md — Enrutamiento dinámico de EditorIAl IOREB

El CEO/Orquestador clasifica peticiones y enruta componentes en forma dinámica usando `.agents/manifest.yaml`.

## Protocolo
1. Leer `.agents/manifest.yaml`.
2. Resolver `active_project.id` y `active_project.genre`.
3. Aplicar precedencia: `user_request -> safety -> novel -> genre -> editorial`.
4. Seleccionar rol y workflow.
5. Cargar skills mínimas necesarias.
6. Aplicar rules obligatorias.
7. Emitir entregable validado o bloquear con `requiere_revision_humana`.

## Rutas canónicas dinámicas
- Editorial: `.agents/editorial/...`
- Género: `.agents/generos/{active_project.genre}/...`
- Proyecto: `.agents/novelas/{active_project.id}/...`

## Ejemplo con el manifest actual
Con:
- `active_project.id = bitacora_centauri`
- `active_project.genre = hard_scifi_contemplativa`

La ruta patrón:
`.agents/novelas/{active_project.id}/workflows/wf_bitacora_01_escritor_diario.md`
se resuelve como:
`.agents/novelas/bitacora_centauri/workflows/wf_bitacora_01_escritor_diario.md`

## Tabla de enrutamiento (patrón + ejemplo)
| Intención | Patrón genérico / Envoltorio | Ejemplo actual / Asignación |
|---|---|---|
| Escritura narrativa | `.agents/novelas/{active_project.id}/workflows/...` | `.agents/novelas/bitacora_centauri/workflows/wf_bitacora_01_escritor_diario.md` |
| Reglas de género | `.agents/generos/{active_project.genre}/rules/...` | `.agents/generos/hard_scifi_contemplativa/rules/regla_genero_01_ciencia_dura.md` |
| Compliance | `.agents/editorial/workflows/wf_editorial_12_compliance_legal.md` | igual |
| QA EPUB/PDF | `.agents/editorial/workflows/wf_editorial_14_qa_epub_pdf.md` | igual |
| "Prepara publicacion", "Genera paquete KDP", "Genera EPUB final", "Prepara Google Play" | `wf_07_publicacion.md` | Productor Editorial |

## Límites operativos
- No publicar, no subir y no distribuir externamente.
- Solo preparación local: informes, checklists y artefactos exportables.
- La preparación de entrega externa la realiza manualmente el usuario.
- No modificar `manuscrito/`, `biblia/` o `trama/` sin aprobación explícita.

