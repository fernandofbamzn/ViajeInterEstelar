# 🌍 Departamento de Traducción y Localización — EditorIAl IOREB

Este directorio gestiona las versiones multilingües y las ediciones internacionales de las obras del repositorio.

## 📂 Estructura Recomendada por Idioma
Para cada idioma objetivo, se debe crear una subcarpeta con el código ISO correspondiente (ej. `en/` para inglés, `fr/` para francés, `de/` para alemán, `pt/` para portugués):

```text
traducciones/{idioma}/
  glosario.md             # Términos específicos del lore localizados.
  decisiones_estilo.md    # Convenciones tipográficas y estilísticas del idioma destino.
  estado_traduccion.md    # Metadatos del estado y progreso de la traducción.
  manuscrito/             # Archivos de los capítulos traducidos.
    capitulo_01.md
    capitulo_02.md
  metadatos/              # Metadatos localizados para tiendas (KDP, Google Play).
    titulo.md
    subtitulo.md
    descripcion_corta.md
    descripcion_larga.md
    keywords.md
    categorias.md
    nota_ia.md
  auditoria/              # Reportes de calidad técnica e IA.
    informe_calidad.md
    dudas_pendientes.md
```

## ⚙️ Estados de una Traducción
El progreso de la edición internacional se clasifica en los siguientes estados secuenciales:

1. `draft`: Borrador o fase inicial de preparación.
2. `glossary_ready`: Glosario de términos clave extraído y localizado.
3. `style_ready`: Guía de estilo e instrucciones tipográficas definidas para el idioma destino.
4. `translated`: Capítulos traducidos en borrador (por IA o traductor humano).
5. `audited`: Traducción auditada mediante herramientas de control de calidad o segundas lecturas.
6. `native_review_pending` (Estado por defecto de traducción IA): Traducción finalizada por IA, pendiente de validación por un hablante nativo competente.
7. `publishable`: Edición validada por revisión nativa y autorizada por la editorial para su maquetación final.
8. `published`: Obra publicada oficialmente en las tiendas internacionales.

## 🛑 Regla de Seguridad Crítica
Queda estrictamente prohibido marcar una edición como `publishable` o proceder con su subida y publicación en tiendas si no se cuenta con una validación humana nativa suficiente o un reporte de auditoría completo y satisfactorio.
