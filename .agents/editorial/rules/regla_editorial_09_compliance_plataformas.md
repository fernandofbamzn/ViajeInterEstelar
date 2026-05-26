---
id: regla_editorial_09_compliance_plataformas
title: "Compliance, Derechos y Politicas de Plataformas"
scope: editorial
trigger: always_on
description: "Impide infracciones de derechos, declaraciones falsas de IA y riesgos de plataforma."
inputs:
  - "Metadatos"
  - "Cubierta y licencias"
  - "Declaracion de IA"
outputs:
  - "Checklist de compliance"
  - "Bloqueos o aprobaciones requeridas"
requires_human_approval:
  - "Autorizar publicacion"
  - "Resolver riesgos de copyright o plataforma"
---

# Regla Editorial 09: Compliance, Derechos y Politicas de Plataformas

Esta regla protege el proyecto editorial frente a infracciones de derechos, penalizaciones de plataforma, declaraciones falsas y riesgos reputacionales.

## Politicas de Distribucion y Transparencia sobre IA
* Declarar el uso de IA cuando la plataforma lo requiera.
* No ocultar traduccion asistida, texto generado, imagenes generadas o procesos de produccion con IA.
* No revisión externa manual entregables generados o traducidos con IA sin revision humana competente.

## Propiedad Intelectual y Derechos de Autor
* No imitar de forma confundible obras, autores, franquicias, marcas, titulos o portadas de terceros.
* No usar marcas registradas o nombres de personas reales con finalidad comercial enganosa.
* No inventar premios, ventas, rankings, testimonios ni resenas.

## Derechos de Traduccion y Colaboraciones
* Registrar colaboradores humanos con su rol y atribucion correspondiente.
* Verificar derechos territoriales y de idioma antes de compilar una edicion internacional.
* Revisar restricciones de exclusividad como revisión externa manual Select antes de revisión externa manual.

## Checklist Tecnico de Compliance
Antes de autorizar publicacion o promover a `listo_para_revision_humana`, el Responsable de Compliance debe verificar:

1. Declaracion de IA conforme a la plataforma.
2. Copyright y marcas en titulo, subtitulo, descripcion y keywords.
3. Licencias de imagenes, tipografias y cubierta.
4. Exclusividad y derechos territoriales.
5. Nota tecnica de transparencia de produccion cuando aplique.


Este workflow/rol/skill no sustituye asesoramiento legal profesional. No autoriza publicación externa. Solo prepara una auditoría preventiva interna para revisión humana.
Estados: sin_riesgos_obvios, riesgos_menores_detectados, requiere_revision_humana, bloqueado_para_entrega_local.
