---
name: skill_formatear_latex
scope: editorial
description: "Compone manuscritos Markdown a LaTeX o EPUB usando las rutas de exportacion del proyecto."
inputs:
  - "Capitulos finalizados del manuscrito"
  - "Titulo, autor, idioma y ruta de exportacion"
outputs:
  - "exportacion/{idioma}/novela.tex"
  - "exportacion/{idioma}/novela.epub"
requires_human_approval:
  - "Sobrescribir entregables finales aprobados"
---

# Formatear LaTeX y EPUB

## Cuando usarla
* Al preparar entregables fisicos o digitales de un proyecto.
* Cuando el usuario solicite generar `.tex` o `.epub` a partir de capitulos Markdown.

## Entradas necesarias
* Capitulos en `manuscrito/`.
* Configuracion general de la obra: titulo, autor, idioma y dimensiones.
* Carpeta de salida del proyecto, normalmente `exportacion/{idioma}/`.

## Procedimiento
1. Leer los capitulos en el orden secuencial definido por la trama.
2. Convertir Markdown a LaTeX o XHTML.
3. Mantener la tipografia de dialogos castellanos y separadores de escena.
4. Generar tabla de contenidos y metadatos basicos.
5. Ejecutar `.agents/tools/generar_latex.py` o `.agents/tools/generar_epub.py` desde la raiz del repositorio, o pasando `--project-root`.
6. Escribir siempre en `exportacion/{idioma}/`, nunca dentro de `.agents/tools/`.

## Salida esperada
* `exportacion/{idioma}/novela.tex` cuando se genere LaTeX.
* `exportacion/{idioma}/novela.epub` cuando se genere EPUB.
* Instrucciones de compilacion o validacion posterior.

## Riesgos / errores frecuentes
* *Rutas equivocadas:* generar artefactos dentro de `.agents/tools/`. Mitigacion: resolver la raiz del proyecto y usar `exportacion/{idioma}/`.
* *Escapes incorrectos:* olvidar caracteres reservados de LaTeX. Mitigacion: revisar sintaxis antes de compilar.
* *Dialogos rotos:* sustituir rayas largas por guiones. Mitigacion: mantener UTF-8 y validar visualmente.

## Checklist de finalizacion
- [ ] Los artefactos se han escrito en `exportacion/{idioma}/`.
- [ ] No se ha modificado `manuscrito/`.
- [ ] El documento LaTeX o EPUB se genera sin errores de ruta.
