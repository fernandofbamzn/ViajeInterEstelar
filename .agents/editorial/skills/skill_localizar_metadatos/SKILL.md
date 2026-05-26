---
name: skill_localizar_metadatos
scope: editorial
description: Localización y adaptación comercial de títulos, descripciones, sinopsis y palabras clave para mercados internacionales.
---

# Skill — Localizar Metadatos

Esta habilidad permite crear descripciones y sinopsis atractivas para las tiendas de libros internacionales, optimizando palabras clave y categorías sin limitarse a una traducción automática de los metadatos originales.

## Cuándo usarla
- Al preparar una edición para su preparación de entrega en mercados internacionales (como Amazon US, Amazon UK, etc.).
- Cuando se requiera adaptar el material promocional de la obra a otros idiomas.

## Entradas necesarias
- Metadatos originales de la obra (título, descripción, palabras clave).
- Mercado geográfico e idioma destino.
- Guías comerciales de la editorial.

## Procedimiento
1. **Evaluación del Título:** Analizar candidatos de título localizado según sonoridad, fidelidad conceptual, gancho comercial y claridad del género en el mercado de destino.
2. **Localización de la Sinopsis:** Redactar la descripción larga y la frase gancho adaptándolas a las expectativas de los lectores locales de ciencia ficción.
3. **Optimización de Metadatos:** Seleccionar palabras clave (`keywords`) y categorías específicas optimizadas para los buscadores de la plataforma destino en el idioma correspondiente.
4. **Declaración de IA:** Redactar la nota de declaración de uso de IA para traducción y generación de contenido si las políticas de la tienda lo requieren.
5. **Escritura de Resultados:** Guardar los archivos resultantes en la carpeta `traducciones/{idioma}/metadatos/`.

## Salida esperada
- Archivos markdown de metadatos bajo `traducciones/{idioma}/metadatos/` (`titulo.md`, `descripcion_larga.md`, `nota_ia.md`, etc.).

## Riesgos / errores frecuentes
- **Traducción literal ineficiente:** Traducir sinopsis literalmente perdiendo fuerza comercial o usando terminología comercial que no encaja en la cultura destino.
- **Categorización errónea:** Utilizar categorías de la tienda española en mercados internacionales donde la estructura de categorías de Amazon es diferente.
- **Ocultar uso de IA:** Omitir la declaración de IA cuando la plataforma de entrega local (como revisión externa manual) lo exige bajo riesgo de suspensión.

## Checklist de finalización
- [ ] ¿Se han generado al menos 2 alternativas comerciales para el título si el original no es adecuado?
- [ ] ¿La descripción larga respeta el género y tono de la novela?
- [ ] ¿Se ha completado el archivo `nota_ia.md` detallando las herramientas de traducción automatizada utilizadas?
