---
id: regla_editorial_03_control_costes
title: "Control de Costes y Registro de Tokens"
scope: editorial
trigger: always_on
---

# Control de Costes y Registro de Tokens

## 📋 Contexto y Motivación
El desarrollo de obras mediante llamadas a APIs de modelos avanzados de lenguaje (como Claude, GPT u otros) conlleva costes financieros variables. Un control riguroso permite evaluar la viabilidad comercial de la editorial.

## 🛠️ Directriz Inviolable
Toda interacción de generación de contenido, reescritura o auditoría exhaustiva debe estar sujeta a un control presupuestario:
1. **Registro Obligatorio:** Todos los consumos financieros estimados o de tokens deben ser documentados en el registro contable (`costes/ledger_tokens.jsonl`) si se dispone de la información.
2. **Uso de Modelos de Coste Eficiente:** Utilizar modelos económicos para tareas repetitivas o de baja complejidad (formateo, maquetación, checks sintácticos) y reservar los modelos caros para la redacción principal y la crítica literaria profunda.
3. **No Inventar Datos:** Si el coste exacto no puede ser calculado, se debe registrar como estimado indicando los tokens o marcar el campo como `null` o `0` en vez de introducir cifras aleatorias.

## 🛑 Lo que NUNCA debe hacerse
* Ejecutar bucles automatizados de reescritura masiva con modelos premium sin monitorizar el consumo de tokens.
* Escribir valores de coste inventados en el registro financiero.

## ✅ Comportamiento Esperado
* Comprobar la eficiencia de los prompts y limitar los contextos gigantescos a lo estrictamente necesario.
* Rellenar el ledger de tokens cada vez que se ejecuten procesos automatizados o workflows complejos que consuman API.
