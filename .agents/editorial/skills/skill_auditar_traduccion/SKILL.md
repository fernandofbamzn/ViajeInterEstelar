---
name: skill_auditar_traduccion
scope: editorial
description: Auditoría comparativa entre texto original y traducido para verificar calidad y consistencia.
---

# Skill — Auditar Traducción

Esta habilidad se encarga de analizar comparativamente los capítulos traducidos frente a los originales para certificar la integridad narrativa, la ausencia de alucinaciones y la consistencia técnica.

## Cuándo usarla
- Al finalizar la traducción de un bloque o de la novela completa.
- Tras la traducción de metadatos o sinopsis comerciales.
- Como paso indispensable antes de pasar el estado de una traducción a `audited` o `native_review_pending`.

## Entradas necesarias
- Texto original (`manuscrito/capitulo_XX.md`).
- Texto traducido (`traducciones/{idioma}/manuscrito/capitulo_XX.md`).
- Glosario oficial de traducción.
- Reglas de género (ej. dosificación de infodumping).

## Procedimiento
1. **Comparación Estructural:** Comprobar que no hay omisiones de frases o añadidos de trama inventada.
2. **Revisión Terminológica:** Validar que los términos traducidos coinciden al 100% con las decisiones del glosario.
3. **Análisis de Tono y Ritmo:** Identificar caídas de ritmo, literalidades torpes, falsos amigos o pérdidas de voz.
4. **Verificación Técnica:** Asegurar que los conceptos de ciencia dura no han sido diluidos o malinterpretados por la traducción automática.
5. **Generación del Reporte:** Escribir o actualizar el informe de calidad en `traducciones/{idioma}/auditoria/informe_calidad.md`.

## Salida esperada
- El informe de auditoría `traducciones/{idioma}/auditoria/informe_calidad.md` clasificado por severidad de incidencias.

## Riesgos / errores frecuentes
- **No marcar alucinaciones:** Pasar por alto añadidos estilísticos innecesarios del traductor automático.
- **Auditoría superficial:** Evaluar únicamente la gramática sin comparar con el manuscrito original, obviando pérdidas de información conceptual.
- **Declarar lista sin revisión humana:** Intentar marcar como `listo_para_revision_humana` una traducción generada por IA sin una auditoría nativa previa.

## Checklist de finalización
- [ ] ¿El informe detalla los errores categorizados en críticos, medios y menores?
- [ ] ¿Se ha revisado el cumplimiento del glosario en el capítulo evaluado?
- [ ] ¿Se incluye una recomendación de estado de traducción para el equipo editorial?
