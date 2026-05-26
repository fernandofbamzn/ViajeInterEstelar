---
id: wf_editorial_00_ejecucion_semiautonoma
title: "Ejecucion Semiautonoma Orquestada"
scope: editorial
role: "CEO / Orquestador"
description: "Workflow maestro para clasificar peticiones, cargar contexto minimo, resolver roles y detenerse ante aprobaciones obligatorias."
inputs:
  - "Peticion del usuario"
  - ".agents/manifest.yaml"
  - ".agents/ORQUESTADOR.md"
outputs:
  - "Ruta de ejecucion seleccionada"
  - "Entregable del workflow delegado"
  - "Checklist de permisos y aprobaciones"
requires_human_approval:
  - "Cualquier accion marcada como requires_human_approval por reglas, workflow o skill"
---

# Workflow Editorial 00 - Ejecucion Semiautonoma Orquestada

## Rol Operativo
El CEO actua como enrutador y supervisor. No sustituye al rol especializado: clasifica la peticion, carga el contexto minimo y delega la ejecucion al workflow canonico correcto.

## Pasos del Proceso

### 1. Clasificar Intencion
* Identificar si la peticion es de escritura, canon, edicion, critica, ciencia, traduccion, publicacion, marketing, compliance, QA, brainstorming, worldbuilding, personajes o infraestructura.
* Si hay varias intenciones, separarlas por entregable y resolver dependencias.

### 2. Cargar Manifiesto
* Leer `.agents/manifest.yaml`.
* Extraer `active_project.id`, `active_project.genre`, rutas canonicas y componentes activos.
* No cargar componentes no relacionados salvo que el workflow lo requiera.

### 3. Resolver Nivel y Ruta Canonica
* Nivel editorial: usar `.agents/editorial/...`.
* Nivel de genero: usar `.agents/generos/{active_project.genre}/...`.
* Nivel de novela: usar `.agents/novelas/{active_project.id}/...`.
* Tratar `.agents/rules`, `.agents/skills` y `.agents/workflows` solo como wrappers de compatibilidad.

### 4. Cargar Reglas Minimas
* Aplicar siempre precedencia: usuario, seguridad, novela, genero, editorial.
* Cargar `regla_editorial_10_permisos_operativos.md` antes de cualquier accion que pueda modificar archivos.
* Cargar `regla_editorial_11_estructura_proyecto_novela.md` si la tarea crea o reorganiza una novela.
* Cargar reglas de novela y genero solo cuando la tarea afecte contenido narrativo, canon o tono.

### 5. Ejecutar Workflow Especializado
* Adoptar el rol indicado por el workflow canonico.
* Ejecutar solo las skills declaradas por el workflow o por el orquestador.
* Mantener separados diagnostico, propuesta y cambios aplicados.

### 6. Control de Aprobaciones
* Antes de escribir en `manuscrito/`, `biblia/`, `trama/`, `traducciones/`, `exportacion/` o metadatos finales, clasificar el permiso.
* Si aparece `requires_human_approval`, detener la ejecucion y pedir aprobacion concreta.
* Nunca promover una edicion a `listo_para_revision_humana` o `entrega_local_preparada` sin validacion humana suficiente.

### 7. Entrega y Checklist
* Entregar el artefacto pedido o el informe de bloqueo.
* Incluir workflow usado, roles implicados, rutas tocadas y estado final: `propuesta`, `borrador`, `auditado`, `requiere_aprobacion` o `aprobado`.

## Entregables
* Decision de enrutamiento.
* Ejecucion del workflow especializado.
* Checklist de permisos y estado final.
