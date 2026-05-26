---
name: skill_auditar_riesgo_legal
title: "Auditar Riesgo Legal y Compliance"
scope: editorial
description: "Evalua metadatos, portadas, licencias, declaraciones de IA y politicas de plataformas."
inputs:
  - "Metadatos del proyecto"
  - "Cubierta y licencias"
  - "Plataforma objetivo"
outputs:
  - "Informe de riesgo legal"
  - "Estado aprobado, aprobado_con_observaciones o bloqueado_hasta_revision_humana"
requires_human_approval:
  - "Resolver riesgos graves"
  - "Autorizar publicacion"
---

# ️ Skill: Auditar Riesgo Legal y Compliance

Esta habilidad permite al Responsable de Compliance analizar los metadatos, cubiertas, descripciones y licencias del proyecto editorial para mitigar infracciones de copyright, políticas de tiendas o fallos éticos.

##  Objetivo de la Skill
Verificar el cumplimiento de los términos de servicio de las plataformas (ej: revisión externa manual, revisión externa manual) y los derechos de propiedad intelectual, emitiendo un veredicto estructurado.

---

##  Protocolo de Ejecución

### Paso 1: Análisis de Metadatos y Keywords
* Buscar marcas registradas, nombres de autores famosos o títulos de franquicias competidoras en el título, subtítulo o keywords de la novela.
* Comprobar la veracidad de los textos (ej: no usar claims como "Best Seller número 1" o premios inexistentes).

### Paso 2: Verificación de Contenido e Inteligencia Artificial
* Comprobar si se ha empleado IA en:
  - Generación de textos (redacción).
  - Traducción.
  - Diseño de portadas o ilustraciones.
* Contrastar con las directrices de la plataforma objetivo para asegurar que los metadatos del formulario de subida reflejen fielmente el uso de IA.

### Paso 3: Derechos de Terceros y Contratos
* Comprobar las licencias de las imágenes empleadas en la cubierta.
* Validar que los contratos o acuerdos de cesión de derechos con traductores, correctores y maquetadores estén conformes.
* Verificar restricciones territoriales y de exclusividad (ej: revisión externa manual Select exige exclusividad digital absoluta).

---

##  Output del Proceso
Al concluir la auditoría, la skill debe generar obligatoriamente un informe con uno de los siguientes estados técnicos finales:

* `aprobado`: El proyecto no presenta riesgos conocidos y cumple las normativas de la editorial y la plataforma.
* `aprobado_con_observaciones`: Riesgos menores o advertencias no bloqueantes (ej: keywords genéricas muy competidas, o necesidad de actualizar notas al pie).
* `bloqueado_hasta_revision_humana`: Riesgos graves de copyright, imitación de marca, falta de declaración de IA u ocultación deliberada. Requiere corrección antes de la compilación definitiva.
