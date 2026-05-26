---
id: wf_editorial_11_auditoria_traduccion
title: "Auditoria de Traduccion Editorial"
scope: editorial
role: "Traductor y Lector Cero"
description: "Compara original y traduccion para detectar perdida de sentido, tono, glosario o canon."
inputs:
  - "Texto original"
  - "Texto traducido"
  - "Glosario de traduccion"
outputs:
  - "Informe de auditoria de traduccion"
  - "Recomendacion de estado"
requires_human_approval:
  - "Promover una traduccion a listo_para_revision_humana"
---

# Workflow Editorial 11  Auditor de Traducción Editorial

Este flujo de trabajo se ejecuta para comprobar de forma exhaustiva la fidelidad, el estilo y la cohesión de una traducción parcial o completa de la obra.

---

## ️ Rol Operativo
**Auditor de Traducción Editorial**: Evaluador independiente encargado de cotejar el original y la versión traducida para evitar discrepancias, omisiones o pérdida del tono literario y científico de la novela.

---

##  Pasos del Proceso

### 1. Definición del Alcance de la Auditoría
- [ ] **Seleccionar alcance:** Especificar si la revisión se realizará sobre un capítulo individual, un bloque de capítulos, el manuscrito completo o los metadatos localizados.
- [ ] **Cargar recursos:** Cargar el glosario oficial `traducciones/{idioma}/glosario.md` y la guía de estilo `traducciones/{idioma}/decisiones_estilo.md`.

### 2. Ejecución del Chequeo Comparativo
- [ ] **Comparar textos:** Cotejar el contenido original en `manuscrito/` con el traducido en `traducciones/{idioma}/manuscrito/`.
- [ ] **Validar glosario:** Verificar que no se han introducido desviaciones terminológicas en los conceptos de ciencia dura, especies alienígenas o nombres de personajes.
- [ ] **Análisis estilístico:** Comprobar la fluidez, naturalidad, ritmo contemplativo (si aplica) y que se hayan adaptado correctamente las voces de los personajes al idioma destino.
- [ ] **Detección de errores:** Listar errores de sentido, falsos amigos, literalidades torpes u omisiones involuntarias.

### 3. Emisión del Informe de Auditoría
- [ ] **Generar informe:** Rellenar la plantilla en `traducciones/{idioma}/auditoria/informe_calidad.md` categorizando los fallos detectados según su severidad (críticos, medios, menores).
- [ ] **Restricción:** El auditor no reescribirá el texto traducido de forma directa, salvo que el usuario lo solicite expresamente; su función es señalar los puntos problemáticos.

### 4. Recomendación de Estado de Calidad
- [ ] **Emitir dictamen:** Basándose en los resultados, proponer la actualización del estado de progreso:
  - Si hay errores críticos de traducción o alucinaciones: devolver el estado a `draft`.
  - Si la traducción es buena pero requiere revisión nativa obligatoria (IA): mantener en `native_review_pending`.
  - Si se cuenta con validación nativa contrastada: promover a `listo_para_revision_humana`.


Resultado esperado: preparar edición localizada, validar paquete localizado y generar metadatos localizados para revisión humana competente. Estado final permitido: entrega_local_preparada.
