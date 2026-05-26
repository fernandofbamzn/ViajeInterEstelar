---
name: skill_calcular_coste_tokens
scope: editorial
description: Estima el coste de tokens de entrada/salida y actualiza el ledger de gastos.
---

# Calcular Coste de Tokens

## Cuándo usarla
* Al ejecutar workflows que impliquen llamadas masivas o estructuradas a APIs de modelos de lenguaje.
* Cuando el usuario solicite un reporte de viabilidad y costes acumulados del proyecto.

## Entradas necesarias
* Datos de la llamada actual: modelo utilizado (ej: `claude-3-opus`, `gpt-4o`), tokens de entrada y tokens de salida.
* El archivo contable `costes/ledger_tokens.jsonl` (para anexar registros).

## Procedimiento
1. **Identificación de Tarifas:** Aplicar los precios vigentes por millón de tokens para el modelo especificado.
2. **Cálculo Financiero:** 
   $$\text{Coste} = (\text{Tokens Entrada} \times \text{Tarifa Entrada}) + (\text{Tokens Salida} \times \text{Tarifa Salida})$$
3. **Escritura del Registro:** Crear una entrada en formato JSONL con la marca de tiempo, proyecto activo, workflow ejecutado, modelo y coste estimado en euros.
4. **Resumen Contable:** Si es requerido, actualizar `costes/resumen_costes.md` sumando el nuevo gasto al histórico acumulado.

## Salida esperada
* Una línea JSONL correctamente anexada a `costes/ledger_tokens.jsonl`.
* Un cálculo preciso impreso en la respuesta del agente.

## Riesgos / errores frecuentes
* *Tarifas desactualizadas:* Utilizar precios de modelos antiguos. Mitigación: Comprobar fechas de precios o permitir configurarlos en el archivo de manifiesto.
* *Formato JSONL inválido:* Añadir comas o saltar líneas de forma incorrecta. Mitigación: Validar la sintaxis de cada línea antes de escribirla.

## Checklist de finalización
- [ ] La entrada JSONL es de una sola línea y respeta el esquema especificado.
- [ ] El coste estimado se ha convertido correctamente a euros (EUR).
- [ ] Si se desconoce el conteo de tokens, se deja el coste en 0 o null en lugar de inventar.
