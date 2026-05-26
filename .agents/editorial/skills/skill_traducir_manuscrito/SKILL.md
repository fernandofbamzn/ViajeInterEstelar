---
name: skill_traducir_manuscrito
scope: editorial
description: Traducción capítulo a capítulo de manuscritos, manteniendo tono, voz, ritmo y canon.
---

# Skill — Traducir Manuscrito

Esta habilidad permite traducir secuencialmente los capítulos del manuscrito conservando la experiencia de lectura original sin alterar el canon ni la trama.

## Cuándo usarla
- Durante la fase de traducción activa de la novela en un workflow de traducción.
- Para re-traducir secciones específicas tras correcciones editoriales.

## Entradas necesarias
- Idioma origen y destino.
- Capítulo o fragmento en `manuscrito/`.
- Glosario oficial en `traducciones/{idioma}/glosario.md`.
- Guía de decisiones de estilo en `traducciones/{idioma}/decisiones_estilo.md`.
- Reglas de género y novela aplicables.

## Procedimiento
1. **Lectura Contextual:** Analizar el fragmento a traducir identificando el POV, la atmósfera y el ritmo.
2. **Aplicación del Glosario:** Sustituir los términos técnicos e institucionales exactamente por sus equivalentes del glosario.
3. **Localización de Estilo:** Adaptar la puntuación, diálogos, comillas y unidades de medida a las normas del idioma destino según la guía de estilo.
4. **Traducción Narrativa:** Realizar la traducción manteniendo la voz de los personajes, evitando construcciones literales y traduciendo con un pacing contemplativo si el género lo requiere.
5. **Registro de Dudas:** Documentar las dudas o dobles interpretaciones surgidas para su posterior validación por el auditor o corrector nativo.

## Salida esperada
- El capítulo traducido guardado en `traducciones/{idioma}/manuscrito/capitulo_XX.md`.
- Registro de dudas terminológicas o decisiones difíciles.

## Riesgos / errores frecuentes
- **Sobreescritura accidental:** Reemplazar archivos ya traducidos y corregidos sin confirmación previa del usuario.
- **Antropomorfización o pérdida de tono:** En ciencia ficción, traducir metáforas de perspectiva alienígena a modismos de cultura humana común.
- **Pérdida de exactitud científica:** Adaptar términos matemáticos o físicos a un lenguaje de fantasía o magia.
- **Traducción masiva degradada:** Intentar traducir la novela completa en una única llamada masiva, lo que provoca olvido de reglas y pérdida de consistencia tipográfica.

## Checklist de finalización
- [ ] ¿El capítulo traducido mantiene exactamente el mismo número de párrafos y escenas?
- [ ] ¿Se han adaptado las rayas de diálogo españolas a la puntuación del idioma de destino?
- [ ] ¿Los nombres propios y términos alienígenas protegidos se han conservado exactamente igual?
- [ ] ¿Se han registrado las dudas en el archivo de auditoría?
