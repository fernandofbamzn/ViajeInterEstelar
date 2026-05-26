---
id: regla_editorial_04_no_publicar_sin_revision_humana
title: "Prohibición de Preparación de entrega Automatizada sin Revisión Humana"
scope: editorial
trigger: always_on
---

# Prohibición de Preparación de entrega Automatizada sin Revisión Humana

## 📋 Contexto y Motivación
Los sistemas automáticos pueden cometer alucinaciones, errores de formato o infringir políticas de plataformas sin darse cuenta. La supervisión humana es el último y más importante filtro de seguridad para EditorIAl IOREB.

## 🛠️ Directriz Inviolable
1. **Ninguna Preparación de entrega Autónoma:** Ningún workflow, script o agente tiene autorización para presionar botones de preparación de entrega, subir el manuscrito a tiendas, o lanzar campañas comerciales activas de forma autónoma.
2. **Rol del Agente como Validador y Preparador:** El agente solo recopilará, estructurará y validará los entregables, arrojando un checklist final que el usuario humano deberá marcar y ejecutar manualmente.
3. **Control Final del Manuscrito:** La aprobación final del EPUB, portada, sinopsis y precio corresponde de manera exclusiva al editor humano.

## 🛑 Lo que NUNCA debe hacerse
* Diseñar workflows que intenten interactuar con APIs de KDP o Google Books para realizar publicaciones "directas" o "silenciosas" sin requerir confirmación y acción física del usuario.
* Omitir el paso de validación visual de los archivos EPUB/PDF finales.

## ✅ Comportamiento Esperado
* Finalizar todo flujo de trabajo de producción y preparación de entrega con un informe detallado que liste los archivos listos y un checklist de acciones que el humano debe ejecutar en la consola de preparación de entrega de la plataforma.
