---
name: skill_validar_publicacion_kdp_google
scope: editorial
description: Comprueba que el manuscrito, los metadatos y los recursos visuales cumplen las políticas y formatos técnicos de KDP Amazon y Google Play Books.
---

# Validar Preparación de entrega en KDP y Google Play Books

## Cuándo usarla
* En la fase de pre-lanzamiento y preparación de entregables.
* Al ejecutar el flujo de trabajo de preparación de entrega.

## Entradas necesarias
* Metadatos del libro (Título, Autor, Sinopsis, Keywords, Categorías).
* Archivos del entregable: EPUB y PDF de cubierta/interior.
* Políticas vigentes de IA de Amazon y Google (almacenadas o descritas por el usuario).

## Procedimiento
1. **Verificación de Formatos Técnicos:**
   - Confirmar que el EPUB es válido (pasa checks de validación EPUB estándar).
   - Comprobar que el PDF interior tiene las fuentes incrustadas y los márgenes de sangrado configurados si es para tapa blanda.
2. **Revisión de Metadatos:**
   - Validar que el título y subtítulo coincidan exactamente con la portada.
   - Comprobar que las categorías seleccionadas existen y son válidas en las plataformas.
3. **Auditoría de Políticas de IA:**
   - Asegurar que se dispone de la información necesaria para responder a la pregunta de Amazon sobre "Contenido generado por IA" (Texto, Imágenes, Traducción).
4. **Validación de Derechos:**
   - Comprobar que no se infringen marcas comerciales ni derechos de autor en el texto ni en la portada.

## Salida esperada
Un reporte de validación con:
* Estado de conformidad técnica (Apto / Requiere Modificación).
* Respuestas sugeridas para el cuestionario de IA de Amazon KDP.
* Checklist detallado para que el usuario complete la subida manual sin errores.

## Riesgos / errores frecuentes
* *Diferencias de título:* Que el título del formulario difiera una sola letra del de la imagen de portada, lo cual causa rechazo inmediato en Amazon KDP. Mitigación: Comprobar carácter por carácter.
* *Políticas de IA desactualizadas:* Las tiendas cambian sus directrices con frecuencia. Mitigación: Recordar al usuario que verifique las directrices del panel en vivo al subir el manuscrito.

## Checklist de finalización
- [ ] Título y subtítulo validados carácter por carácter frente a la portada.
- [ ] Preparada la declaración de uso de IA para texto e imágenes.
- [ ] Confirmada la presencia de fuentes incrustadas en el PDF de impresión.
