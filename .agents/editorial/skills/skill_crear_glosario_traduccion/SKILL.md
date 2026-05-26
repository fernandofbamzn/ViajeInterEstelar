---
name: skill_crear_glosario_traduccion
scope: editorial
description: Extracción, traducción y mantenimiento de términos clave antes del proceso de traducción.
---

# Skill — Crear Glosario de Traducción

Esta habilidad permite al agente identificar, extraer y proponer traducciones coherentes para términos críticos antes de iniciar la traducción de la obra completa, garantizando la consistencia del canon.

## Cuándo usarla
- Antes de iniciar la traducción de cualquier obra.
- Al añadir nuevos conceptos en la biblia del lore que deban localizarse.
- Cuando surjan inconsistencias terminológicas en la traducción de capítulos.

## Entradas necesarias
- Biblia del lore en `biblia/`.
- Capítulos estables del manuscrito origen en `manuscrito/`.
- Idioma destino.

## Procedimiento
1. **Extracción:** Analizar los documentos canónicos en `biblia/` para extraer nombres propios, especies, tecnologías, localizaciones, cargos y conceptos científicos clave.
2. **Clasificación:** Organizar los términos extraídos según su tipo (personaje, tecnología, etc.).
3. **Propuesta:** Sugerir opciones de traducción aplicando criterios de sonoridad, exactitud técnica y ritmo literario en el idioma destino.
4. **Asignación de Decisiones:** Etiquetar cada término con un estado de decisión claro (`conservar`, `traducir`, `adaptar`, `pendiente`, `prohibido_cambiar`).
5. **Generación del Glosario:** Escribir o actualizar el glosario en `traducciones/{idioma}/glosario.md`.

## Salida esperada
- Archivo markdown `traducciones/{idioma}/glosario.md` conteniendo la tabla estructurada de términos.

## Riesgos / errores frecuentes
- **Literalidad infantil:** Traducir términos de ciencia ficción dura palabra por palabra sin evaluar el impacto en la inmersión del idioma destino.
- **Traducción de nombres propios inalterables:** Modificar nombres alienígenas o humanos protegidos por el canon.
- **Falta de mantenimiento:** No actualizar el glosario a medida que el manuscrito avanza o cambia.

## Checklist de finalización
- [ ] ¿El glosario contiene las 5 columnas requeridas (`Término original`, `Traducción`, `Tipo`, `Decisión`, `Notas`)?
- [ ] ¿Se han revisado los conceptos científicos para que conserven coherencia de física real?
- [ ] ¿Quedan claras las palabras marcadas como `prohibido_cambiar`?
