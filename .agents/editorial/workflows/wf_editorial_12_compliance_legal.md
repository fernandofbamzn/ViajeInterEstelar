---
id: wf_editorial_12_compliance_legal
title: "Compliance Legal y Auditoria Preventiva"
scope: editorial
role: "Responsable de Compliance"
description: "Audita copyright, marcas, declaracion de IA, derechos y politicas de plataforma antes de lanzamiento."
inputs:
  - "Metadatos"
  - "Cubierta y licencias"
  - "Declaracion de uso de IA"
outputs:
  - "Ficha de cumplimiento"
  - "Veredicto de compliance"
requires_human_approval:
  - "Resolver bloqueos legales"
  - "Autorizar publicacion"
---

#  Workflow: Compliance Legal y Auditoría Preventiva de Lanzamiento

Este workflow describe los pasos obligatorios que el **Responsable Legal / Compliance Editorial** ejecuta para validar un proyecto antes de cualquier exportación o intento de preparación de entrega en plataformas.

> [!IMPORTANT]
> Este workflow no sustituye el asesoramiento legal profesional de un abogado cualificado. Su propósito es realizar una auditoría editorial preventiva y un control de calidad y ético interno.

---

##  Roles Involucrados
* **Responsable Legal / Compliance:** Ejecuta las verificaciones y emite el veredicto final.
* **CEO (Director Editorial):** Supervisa el balance y aprueba la resolución.
* **Productor Editorial:** Proporciona los metadatos técnicos y los archivos maquetados.

---

## ️ Skills Invocadas
* `skill_auditar_riesgo_legal/SKILL.md`
* `skill_auditar_producto_editorial/SKILL.md`

---

## ️ Rules de Referencia Obligatorias
* `regla_editorial_02_etica_ia_y_transparencia.md`
* `regla_editorial_04_no_publicar_sin_revision_humana.md`
* `regla_editorial_07_no_imitacion_copyright.md`
* `regla_editorial_09_compliance_plataformas.md`

---

##  Pasos del Proceso

### Paso 1: Carga y Revisión de Metadatos del Proyecto
* Importar la ficha del proyecto activo y sus campos (título, subtítulo, sinopsis, keywords).
* Validar que la descripción de la tienda no contiene afirmaciones engañosas o reseñas fabricadas de forma ficticia.

### Paso 2: Análisis del Uso de IA y Transparencia
* Consultar en el manifiesto y el estado de traducción las herramientas automatizadas que se han empleado.
* Verificar que en la página de créditos del volumen o en la sección de metadatos se incluya la nota técnica correspondiente sobre traducción o redacción asistida por IA.

### Paso 3: Auditoría de Copyright y Marcas
* Contrastar los nombres propios, locaciones y terminologías clave del manuscrito y de los metadatos frente a bases de datos de propiedad intelectual básicas o marcas de dominio literario comunes.
* Asegurar que no se imitan logos, cubiertas o tipografías registradas de otras editoriales o autores.

### Paso 4: Revisión de Contribuyentes y Plataforma Objetivo
* Comprobar que los derechos de traducción de la obra están vigentes para el territorio de destino.
* Validar las restricciones técnicas de las plataformas (ej: verificar que el PDF/EPUB cumple con la guía de contenido apropiado para menores si procede).

### Paso 5: Emisión de la Ficha de Cumplimiento
* Ejecutar la skill `skill_auditar_riesgo_legal` para emitir el veredicto definitivo.
* Registrar el resultado en `exportacion/{idioma}/compliance_report.md` con los estados: `aprobado`, `aprobado_con_observaciones` o `bloqueado_hasta_revision_humana`.

> [!WARNING]
> **requires_human_approval**: Si el veredicto de compliance es `bloqueado_hasta_revision_humana`, el proceso de maquetación y exportación de archivos queda congelado automáticamente. El CEO o el usuario humano deben validar y solventar la anomalía detectada.


Este workflow/rol/skill no sustituye asesoramiento legal profesional. No autoriza publicación externa. Solo prepara una auditoría preventiva interna para revisión humana.
Estados: sin_riesgos_obvios, riesgos_menores_detectados, requiere_revision_humana, bloqueado_para_entrega_local.
