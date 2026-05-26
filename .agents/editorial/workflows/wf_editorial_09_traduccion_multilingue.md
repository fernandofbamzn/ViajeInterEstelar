---
id: wf_editorial_09_traduccion_multilingue
title: "Traduccion Multilingue"
scope: editorial
role: "Traductor y Localizador"
description: "Coordina glosario, guia de estilo, traduccion secuencial, auditoria y estado de revision nativa."
inputs:
  - "Manuscrito origen"
  - "Idioma destino"
  - "Glosario y decisiones de estilo"
outputs:
  - "Capitulos traducidos"
  - "glosario.md"
  - "decisiones_estilo.md"
  - "estado_traduccion.md"
requires_human_approval:
  - "Sobrescribir traducciones existentes"
  - "Marcar una traduccion como listo_para_revision_humana"
---

# Workflow Editorial 09  Coordinador de Traducción Editorial

Este flujo de trabajo gestiona de forma integral la traducción, localización y adecuación de manuscritos para la creación de ediciones internacionales de obras en **EditorIAl IOREB**.

---

## ️ Rol Operativo
**Coordinador de Traducción Editorial**: Responsable de orquestar el flujo de traducción, velar por la coherencia del glosario y auditar que la prosa traducida no sufra pérdidas de calidad.

---

##  Pasos del Proceso

### 1. Preparación y Carga de Contexto
- [ ] **Identificar:** Definir el proyecto activo, el idioma de origen y el idioma de destino.
- [ ] **Validar manuscrito origen:** Confirmar en `project_profile.md` que los capítulos del manuscrito de origen están lo suficientemente estables (cerrados) para iniciar la traducción.
- [ ] **Estructura:** Crear la carpeta de traducción en `traducciones/{idioma}/` y sus subcarpetas de manuscrito, metadatos y auditoría si no existen.
- [ ] **Cargar directrices:** Cargar las reglas editoriales del proyecto (ej: `regla_editorial_08_traduccion_multilingue.md`), las de género y las de la novela activa.

### 2. Extracción del Glosario de Traducción
- [ ] **Glosario previo:** Ejecutar `skill_crear_glosario_traduccion`.
- [ ] **Tabla de términos:** Extraer nombres, tecnologías, especies y términos de lore clave. Rellenar `traducciones/{idioma}/glosario.md` con las traducciones preliminares y decisiones correspondientes (`conservar`, `traducir`, etc.).
- [ ] **Bloqueo:** No iniciar la traducción de capítulos completos si el glosario no ha sido debidamente establecido.

### 3. Redacción de la Guía de Estilo Localizada
- [ ] **Estilo de destino:** Crear o actualizar `traducciones/{idioma}/decisiones_estilo.md` detallando las decisiones de formato de diálogos, comillas, rayas, unidades, fechas y ritmo tipográfico característicos del idioma de destino.

### 4. Traducción Secuencial de Capítulos
- [ ] **Traducción controlada:** Traducir los capítulos del manuscrito **uno a uno** ejecutando `skill_traducir_manuscrito`.
- [ ] **Restricción:** Queda terminantemente prohibido traducir la novela completa en un único bloque masivo.
- [ ] **Salida:** Escribir cada archivo resultante en `traducciones/{idioma}/manuscrito/capitulo_XX.md`.
- [ ] **Registro:** Anotar en el informe de auditoría cualquier término nuevo que surja o dudas para el corrector nativo.
- [ ] **Seguridad:** No modificar bajo ningún concepto el manuscrito original en `manuscrito/`.

### 5. Auditoría y Control de Calidad
- [ ] **Auditoría inicial:** Ejecutar la `skill_auditar_traduccion` sobre los capítulos traducidos para generar el informe comparativo.
- [ ] **Estado por defecto:** Establecer el estado del proyecto traducido en `estado_traduccion.md` como mínimo en `native_review_pending` si ha intervenido IA en la traducción.

### 6. Localización de Metadatos y Marketing
- [ ] **Localizar metadatos:** Ejecutar `skill_localizar_metadatos` para redactar sinopsis, keywords, categorías y notas de IA localizadas en `traducciones/{idioma}/metadatos/`.
- [ ] **Título comercial:** Evaluar y proponer candidatos comerciales para el título, evitando traducciones mecánicas ineficaces.

### 7. Registro de Costes y Control de Balance
- [ ] **Registro financiero:** Registrar los tokens consumidos y costes estimados en `costes/ledger_tokens.jsonl` bajo el formato JSON del departamento de costes, dejando campos como `null` o `0` si no se dispone de autocalculadores en el entorno.

### 8. Actualización de Ficha de Estado
- [ ] **Ficha de progreso:** Rellenar la información en `traducciones/{idioma}/estado_traduccion.md` indicando la versión del manuscrito, los capítulos traducidos, la fecha y el estado de revisión nativa pendiente.


Resultado esperado: preparar edición localizada, validar paquete localizado y generar metadatos localizados para revisión humana competente. Estado final permitido: entrega_local_preparada.
