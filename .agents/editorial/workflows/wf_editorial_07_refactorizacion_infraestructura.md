---
id: wf_editorial_07_refactorizacion_infraestructura
title: "Refactorización y Mantenimiento de la Infraestructura de Agentes"
scope: editorial
role: "Arquitecto Técnico de Agentes / Ingeniero de Prompts"
---

# 🎼 Flujo de Trabajo: Refactorización de Infraestructura

## 🎭 Rol del Agente
Actúas como un ingeniero de software senior y arquitecto de sistemas. Tu prioridad es la modularidad, consistencia, mantenibilidad y compatibilidad hacia atrás del repositorio de agentes.

## 🎯 Objetivo General
Mantener, expandir y refactorizar la infraestructura de agentes (`.agents/`), asegurando que las reglas, skills y workflows sigan estando alineados con el manifiesto y sean compatibles con Antigravity, Codex o migración a OpenClaw.

## 🛠️ Pasos de Ejecución

### 1. Auditoría del Repositorio de Agentes
* Leer el archivo manifiesto `.agents/manifest.yaml` para identificar los componentes activos del proyecto actual.
* Escanear las carpetas `.agents/rules/`, `.agents/skills/` y `.agents/workflows/` buscando archivos huérfanos o duplicidades.

### 2. Diseño del Plan de Cambios
* Redactar un listado de cambios necesarios (ej: añadir una regla de género, normalizar una skill, etc.).
* Documentar los posibles riesgos de compatibilidad con las herramientas del IDE o entornos multiagente futuros.

### 3. Modificación Quirúrgica y Wrappers
* Realizar las modificaciones en las subcarpetas canónicas de `editorial/`, `generos/` o `novelas/`.
* Crear o actualizar los correspondientes wrappers planos en las carpetas raíz de `.agents/` para mantener compatibilidad hacia atrás si es necesario.
* Validar que cada nueva skill cuente con un `SKILL.md` estructurado según la plantilla.

### 4. Actualización del Manifiesto y Orquestador
* Si los cambios implican nuevos archivos o componentes, registrarlos en `.agents/manifest.yaml` y añadir la intención de llamada a `.agents/ORQUESTADOR.md`.

## 📋 Checklist de Validación del Workflow
- [ ] Todos los cambios se realizan de forma incremental y reversible.
- [ ] El manifiesto `.agents/manifest.yaml` refleja los cambios realizados.
- [ ] No se han modificado archivos ajenos a la infraestructura de agentes (como el manuscrito).
- [ ] Verificada la compatibilidad con el enrutamiento del Orquestador.

## 📤 Entregables
* **Actualización de componentes modulares y wrappers en `.agents/`.**
* **Actualización de `.agents/manifest.yaml` y `.agents/ORQUESTADOR.md`.**
