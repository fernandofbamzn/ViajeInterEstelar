---
name: skill_detectar_olor_ia
scope: editorial
description: Detecta y analiza clichés, muletillas y patrones de redacción artificial o genérica de IA.
---

# Detectar Olor a IA

## Cuándo usarla
* Al auditar borradores de capítulos o sinopsis comerciales.
* Como parte del control de calidad literaria previo a dar por finalizada una sección.

## Entradas necesarias
* El borrador del manuscrito o sección de texto a analizar.

## Procedimiento
1. **Búsqueda de Muletillas de IA:** Rastrear el texto buscando palabras y conceptos abusados sistemáticamente por los LLMs en español, tales como:
   - "eco", "resonar", "burbuja", "umbral", "abismo", "verdad", "memoria", "silencio", "esencia", "testamento".
2. **Evaluación de Estructuras Clínicas:** Detectar finales de capítulo "perfectamente redondos" que resuman la moralina o el tema del capítulo de forma explícita y artificial.
3. **Análisis de Conflicto:** Identificar escenas donde los personajes resuelven sus disputas de forma excesivamente educada o cooperativa, perdiendo dramatismo.
4. **Verificación de Variabilidad de Ritmo:** Detectar estructuras de oraciones planas y monótonas (ej: Sujeto + Verbo + Predicado repetido indefinidamente).
5. **Generación del Reporte:** Enumerar los fragmentos "sospechosos" indicando el motivo de su sospecha y un microejemplo quirúrgico sugerido. Bajo ninguna circunstancia esta skill debe reescribir la escena o el capítulo completo.

## Salida esperada
Un informe de auditoría estilística detallando:
* Lista de palabras clichés detectadas y su frecuencia.
* Párrafos con transiciones artificiales o moralinas conclusivas.
* Diagnósticos de estilo con micropropuestas quirúrgicas que sirvan de guía para que el Escritor o el Editor de Mesa realicen las correcciones manuales.

## Riesgos / errores frecuentes
* *Falsos positivos:* Marcar palabras legítimas (ej: si "burbuja" es un concepto tecnológico de la novela, no debe penalizarse su uso técnico). Mitigación: Considerar siempre el contexto de la obra.
* *Invasión de roles y reescritura excesiva:* Alterar la voz artística original o reescribir escenas completas de forma intrusiva. Mitigación: Ofrecer microalternativas acotadas de ejemplo y delimitar el entregable a un diagnóstico técnico.

## Checklist de finalización
- [ ] Se han listado los pasajes específicos que abusan de muletillas de IA.
- [ ] Se han evaluado los cierres de los capítulos para evitar conclusiones edulcoradas o resumidas.
- [ ] Se proponen alternativas micro y quirúrgicas para ilustrar el diagnóstico.
