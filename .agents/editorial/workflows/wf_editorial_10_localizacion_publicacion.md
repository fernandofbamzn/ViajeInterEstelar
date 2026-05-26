---
id: wf_editorial_10_localizacion_publicacion
title: "Preparación de edición localizada"
scope: editorial
role: "Traductor y Productor Editorial"
description: "Prepara metadatos localizados, portada localizada y paquete local de entrega para revisión humana."
inputs:
  - "Traducción auditada"
  - "Metadatos localizados"
  - "Brief de portada localizada"
outputs:
  - "Ficha de edición localizada"
  - "Checklist informativo externo"
  - "Dictamen de estado"
requires_human_approval:
  - "Preparar archivos finales de subida"
  - "Cambiar titulos localizados aprobados"
  - "Promover estado a listo_para_revision_humana"
---

# Workflow Editorial 10  Productor de Ediciones Internacionales (Ejecutado por Traductor y Productor)

Este flujo de trabajo tiene como objetivo la validación comercial, la localización de portadas y la validación de entregables técnicos de una edición internacional para certificar que está lista para su preparación de entrega en tiendas extranjeras.

---

## ️ Roles Operativos e Interdependencias
* **Traductor y Localizador:** Genera los metadatos y glosarios localizados.
* **Productor Editorial:** Valida técnicamente las portadas locales y archivos físicos/digitales.
* **Referencias Cruzadas:** Se asienta sobre los resultados de `wf_editorial_09_traduccion_multilingue.md` (traducción inicial) y `wf_editorial_11_auditoria_traduccion.md` (auditoría de traducción).

---

##  Pasos del Proceso

### 1. Comprobaciones de Plataforma y Declaración de IA
- [ ] **Idiomas soportados:** Comprobar si el idioma de destino está admitido por la tienda correspondiente (revisión externa manual, revisión externa manual).
- [ ] **Coherencia de metadatos:** Asegurar que el idioma de los metadatos coincide con el del manuscrito.
- [ ] **Declaración de IA:** Validar que se ha completado la declaración honesta sobre traducción asistida por IA (`nota_ia.md`).

### 2. Portadas y Localización Visual
- [ ] **Inspección de portada:** Ejecutar `skill_preparar_portada_localizada` para definir el brief de la cubierta internacional.
- [ ] **Variante tipográfica:** Asegurar la maquetación de la portada en `exportacion/{idioma}/portada.png`.
- [ ] **Seguridad:** Queda estrictamente prohibido sobrescribir la portada original de la edición en español.

### 3. Compilación Localizada y Configuración Comercial
- [ ] **Estructura de salida:** Confirmar que los entregables se compilan bajo `exportacion/{idioma}/`.
- [ ] **Precios y Keywords:** Revisar la conversión de precios locales en los mercados objetivo y la presencia de metadatos optimizados en `traducciones/{idioma}/metadatos/`.

---

##  Reglas de Seguridad y Aprobación Humana
* **Este workflow no publica automáticamente.** Toda revisión manual externa reales requiere la intervención manual y validación del usuario humano.
* > [!WARNING]
  > **requires_human_approval**: Se requiere confirmación explícita del usuario humano antes de:
  > - Sobrescribir portadas localizadas existentes.
  > - Cambiar títulos localizados de la obra ya validados por el editor.
  > - Promover el estado de la traducción a `listo_para_revision_humana` en `estado_traduccion.md`.

## Estados válidos
- `no_listo`
- `requiere_correcciones`
- `validado_para_revision_humana`
- `entrega_local_preparada`

##  Dictamen de Estado
El workflow debe concluir con una recomendación de estado de preparación de entrega clara para la edición internacional analizada:
* `no_lista`: Faltan archivos críticos o el manuscrito no se encuentra traducido.
* `lista_para_revision`: Archivos maquetados, pero pendientes de auditoría comparativa.
* `native_review_pending`: Traducción finalizada por IA, requiriendo revisión de hablante nativo.
* `listo_para_revision_humana`: Edición validada con éxito por auditor nativo humano.


Resultado esperado: preparar edición localizada, validar paquete localizado y generar metadatos localizados para revisión humana competente. Estado final permitido: entrega_local_preparada.
