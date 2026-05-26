---
name: skill_generar_metadatos
scope: editorial
description: Genera y optimiza los metadatos bibliográficos (clasificaciones, palabras clave, SEO) para plataformas de preparación de entrega.
---

# Generar Metadatos

## Cuándo usarla
* Al preparar la ficha de lanzamiento de un libro.
* Cuando se inicie un nuevo proyecto o se preparen los entregables finales.

## Entradas necesarias
* Perfil del proyecto y del género.
* Resumen del argumento principal de la novela.
* Público objetivo y competidores referenciales.

## Procedimiento
1. **Definición de Clasificaciones (BISAC / Thema):**
   - Investigar y seleccionar los tres códigos de categoría más representativos de la obra (ej: `FIC028010` - Fiction / Science Fiction / Hard Science Fiction).
2. **Selección de Palabras Clave (Keywords):**
   - Generar una lista de 7 palabras o frases clave altamente relevantes y optimizadas para SEO que los lectores utilicen en las tiendas (ej: "ciencia ficcion alienigenas", "primer contacto real", "hard sci fi en español").
3. **Estructura Bibliográfica:**
   - Redactar los metadatos básicos: Título oficial, subtítulo, autor, serie (si aplica), número de volumen, idioma, precio recomendado por territorio (EUR, USD).
4. **Ficha Técnica en XML/YAML:**
   - Formatear la información en una estructura limpia para su consulta por otros scripts o agentes.

## Salida esperada
Un bloque de metadatos con:
* Ficha básica de preparación de entrega.
* Clasificaciones BISAC y Thema recomendadas.
* Lista optimizada de 7 keywords comerciales para el buscador de KDP.
* Propuestas de precios sugeridos por mercado basados en la longitud de la novela.

## Riesgos / errores frecuentes
* *Keywords inútiles:* Usar términos demasiado genéricos como "libro" o "novela". Mitigación: Enfocarse en términos específicos de nicho que reflejen el valor diferencial del libro.
* *Categorías erróneas:* Asignar categorías de fantasía a un libro de ciencia ficción pura. Mitigación: Seguir rigurosamente la taxonomía BISAC oficial.

## Checklist de finalización
- [ ] Listadas al menos 3 categorías BISAC válidas.
- [ ] Se aportan 7 palabras clave de búsqueda sin duplicar términos del título.
- [ ] Propuesto el esquema de precios en EUR y USD.
