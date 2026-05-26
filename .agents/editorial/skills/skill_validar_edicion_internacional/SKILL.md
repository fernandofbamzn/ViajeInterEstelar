---
name: skill_validar_edicion_internacional
scope: editorial
description: Validación final de la documentación, entregables y estados de la edición internacional para certificar el estado de preparación de entrega.
---

# Skill — Validar Edición Internacional

Esta habilidad ejecuta una auditoría de control de calidad final sobre todos los artefactos de la traducción para autorizar su envío al flujo de maquetación y preparación de entrega de IOREB.

## Cuándo usarla
- Como comprobación final en el flujo de preparación de entrega internacional.
- Para verificar que una traducción IA no avance a `listo_para_revision_humana` sin validación humana suficiente.

## Entradas necesarias
- Manuscrito traducido completo.
- Glosario oficial y guía de estilo validados.
- Informe de auditoría comparativa.
- Archivos de metadatos localizados.
- Estado declarado en `estado_traduccion.md`.

## Procedimiento
1. **Verificación de Integridad:** Comprobar la presencia y coherencia de todos los archivos obligatorios del idioma.
2. **Evaluación de Auditoría:** Confirmar que no hay errores críticos pendientes en el informe de calidad.
3. **Chequeo de Estado:** Revisar si la traducción fue generada por IA. Si es el caso, comprobar si ha habido una validación humana nativa documentada.
4. **Control de Estado de Preparación de entrega:** Si no hay validación nativa suficiente, restringir el estado del proyecto a `native_review_pending` e impedir el cambio a `listo_para_revision_humana`.
5. **Checklist de Plataformas:** Confirmar que se dispone de las descripciones localizadas, keywords y la nota de declaración de IA.

## Salida esperada
- Dictamen de validación recomendando los estados de calidad: `no_lista`, `lista_para_revision`, `native_review_pending` o `listo_para_revision_humana`.

## Riesgos / errores frecuentes
- **Aprobación automatizada descontrolada:** Validar como lista para preparación de entrega una traducción IA sin haber realizado una corrección nativa.
- **Falta de metadatos o portadas:** Aprobar el manuscrito sin verificar que los archivos de marketing y portadas locales también están listos.

## Checklist de finalización
- [ ] ¿El dictamen detalla explícitamente si se requiere revisión nativa?
- [ ] ¿Se han comprobado los checklists de revisión externa manual y revisión externa manual?
- [ ] ¿Los entregables compilados en `exportacion/{idioma}/` están al día con la traducción?


Resultado esperado: preparar edición localizada, validar paquete localizado y generar metadatos localizados para revisión humana competente. Estado final permitido: entrega_local_preparada.
