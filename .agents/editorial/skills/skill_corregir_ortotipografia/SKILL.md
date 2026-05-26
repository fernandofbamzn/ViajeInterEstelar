---
name: skill_corregir_ortotipografia
title: "Corregir Ortotipografia"
scope: editorial
description: "Detecta y corrige errores mecanicos de ortografia, puntuacion, dialogo y estilo tipografico."
inputs:
  - "Texto o capitulo a corregir"
  - "Convenciones editoriales aplicables"
outputs:
  - "Informe de correcciones"
  - "Texto corregido o propuesta de patch"
requires_human_approval:
  - "Sobrescribir manuscrito original"
---

# ️ Skill: Corregir Ortotipografía y Formato Mecánico

Esta habilidad permite al Corrector Ortotipográfico realizar un escaneo automatizado y quirúrgico de un texto en castellano (o en el idioma localizado de destino) para corregir fallos mecánicos de puntuación, mayúsculas, cursivas y formatos tipográficos sin interferir en el estilo literario.

##  Objetivo de la Skill
Normalizar el manuscrito para que cumpla con los estándares tipográficos profesionales (ej: convención RAE en español, Chicago Manual of Style en inglés).

---

##  Directrices Técnicas

### 1. Diálogos con Raya de Diálogo (Castellano)
* Los diálogos deben estructurarse con la raya larga (``, U+2014) pegada a la primera palabra de la intervención del personaje, y separada por un espacio si hay un inciso del narrador:
  - **Correcto:** `¿A qué hora llega la señal? preguntó Elena.`
  - **Incorrecto:** `- ¿A qué hora llega la señal ?  preguntó Elena.`
* Si el diálogo continúa después del inciso del narrador y el inciso termina en verbo de habla (*verbum dicendi*), la puntuación se coloca después de la raya de cierre del inciso:
  - **Correcto:** `La señal es débil susurró el operador, pero constante.`

### 2. Convención de Comillas
* Priorizar el uso de comillas angulares o latinas (`«` y `»`) para textos generales en español, seguidas de comillas inglesas (`"`) y simples (`'`) para anidamientos sucesivos.
* En inglés, utilizar comillas inglesas dobles (`"`) para diálogos y simples (`'`) para anidaciones.

### 3. Cursivas, Mayúsculas y Números
* Emplear cursiva exclusivamente para extranjerismos, nombres de naves espaciales, o énfasis textual muy acotado.
* Verificar la correcta acentuación de mayúsculas (ej: `Á`, ``, ``).
* Asegurar que las cifras numéricas y sus unidades científicas mantengan el espacio duro si corresponde (ej: `53 GB`, `2,4 UA`, `300.000 km/s`).

### 4. Puntuación en Incisos y Signos Dobles
* Comprobar la simetría de signos de apertura y cierre (`¿...?`, `¡...!`, `(...)`, `[...]`).
* Eliminar puntos repetidos y dobles espacios.
