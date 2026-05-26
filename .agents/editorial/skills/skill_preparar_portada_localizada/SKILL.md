---
name: skill_preparar_portada_localizada
scope: editorial
description: Preparación de instrucciones y briefs de diseño para la localización visual y tipográfica de portadas de libros por idioma.
---

# Skill — Preparar Portada Localizada

Esta habilidad coordina la adaptación de portadas para mercados internacionales, definiendo los textos traducidos (títulos, subtítulos, frases gancho) y analizando el espacio tipográfico disponible.

## Cuándo usarla
- Al preparar el dossier de exportación de una edición internacional.
- Cuando la portada original contenga texto que deba traducirse o localizarse visualmente.

## Entradas necesarias
- Imagen de la portada original o plantilla PSD/Figma.
- Título y subtítulo decididos en el glosario/metadatos localizados.
- Idioma y mercado destino.

## Procedimiento
1. **Inspección de Textos:** Identificar qué elementos tipográficos aparecen en la portada de origen (ej. título de la novela, subtítulo, nombre del autor, frase de crítica literaria).
2. **Localización Textual:** Traducir las frases comerciales al idioma de destino utilizando textos cortos que quepan en la composición gráfica original.
3. **Análisis de Dimensiones:** Comprobar si las longitudes de los nuevos textos alteran la composición o requieren cambios de fuente o espaciado.
4. **Instrucciones para Diseñador/IA:** Elaborar el brief detallado en `traducciones/{idioma}/metadatos/portada_localizada.md` para el equipo de arte o para el script generativo de imágenes.

## Salida esperada
- El documento `traducciones/{idioma}/metadatos/portada_localizada.md` con las especificaciones y textos exactos para la portada.

## Riesgos / errores frecuentes
- **Sobreescritura accidental:** Reemplazar el archivo de portada en español `exportacion/portada.png` por la versión localizada de otro idioma.
- **Traducción descuidada:** Usar tipografías no preparadas para caracteres especiales del idioma destino (como tildes, cedillas o diéresis).
- **Textos demasiado largos:** Usar traducciones literales de títulos o subtítulos que arruinan la proporción visual del diseño de cubierta.

## Checklist de finalización
- [ ] ¿El brief detalla las dimensiones exactas requeridas para la portada?
- [ ] ¿Los textos promocionales localizados han sido auditados contra la guía de estilo del idioma?
- [ ] ¿Se especifican las fuentes tipográficas recomendadas?
