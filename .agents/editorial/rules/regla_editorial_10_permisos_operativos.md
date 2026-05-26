---
id: regla_editorial_10_permisos_operativos
title: "Matriz operativa de permisos"
scope: editorial
trigger: always_on
description: "Define permisos y bloqueos para agentes de EditorIAl IOREB."
inputs:
  - "Petición del usuario"
  - ".agents/manifest.yaml"
  - "Workflow y skills seleccionadas"
outputs:
  - "Clasificación: libre, requiere_aprobacion, prohibido"
requires_human_approval:
  - "Modificar manuscrito/, biblia/ o trama/"
  - "Sobrescribir traducciones, portadas o metadatos aprobados"
  - "Cambiar estado a entrega_local_preparada"
---

# Regla editorial 10 — Permisos operativos

## Acciones libres
- Lectura de contexto.
- Informes, auditorías, checklists, borradores no canónicos.
- Validación técnica local de artefactos.

## Acciones con aprobación humana
- Cualquier cambio en `manuscrito/`, `biblia/`, `trama/`.
- Sobrescritura de traducciones o activos localizados ya aprobados.
- Cambio de estado a `entrega_local_preparada`.

## Acciones con Aprobacion Humana
* Modificar archivos bajo `manuscrito/`, `biblia/` o `trama/`.
* Sobrescribir traducciones existentes en `traducciones/`.
* Modificar glosarios si afecta a capitulos ya traducidos.
* Cambiar titulos localizados, portadas, metadatos finales o paquetes de exportacion aprobados.
* Preparar artefactos finales para revisión manual externa.
* Cambiar estados a `listo_para_revision_humana` o `entrega_local_preparada`.
* Ejecutar comandos destructivos o acciones irreversibles del sistema.

## Acciones Prohibidas
* Publicar en plataformas externas, distribuir automáticamente o ejecutar cargas a tiendas sin revisión humana.
* Ocultar o falsear el uso de IA en texto, traduccion, imagenes o produccion.
* Borrar material canonico o historico editorial sin una orden explicita del usuario.
* Cambiar canon narrativo sin validacion del Lorekeeper y aprobacion humana.
* Imitar obras, autores, franquicias, marcas o portadas de terceros de forma confundible.

## Estados de Ejecucion
* `propuesta`: idea, plan u outline no aplicado.
* `borrador`: artefacto generado que requiere revision.
* `auditado`: artefacto revisado por un rol critico o tecnico.
* `requiere_aprobacion`: bloqueado hasta decision humana.
* `aprobado`: validado por el usuario o por el responsable humano indicado.

## Regla de Wrappers
Los directorios planos `.agents/rules`, `.agents/skills` y `.agents/workflows` son solo una capa de compatibilidad. Un wrapper no debe contener logica propia: debe apuntar a una ruta canonica dentro de `.agents/editorial`, `.agents/generos` o `.agents/novelas`.

* `validado_para_revision_humana`: validado internamente para revisión humana.
* `entrega_local_preparada`: paquete local listo para revisión humana; no implica publicación externa.
