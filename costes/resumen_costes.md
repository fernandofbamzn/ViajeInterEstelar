# 🪙 Resumen de Costes Financieros — EditorIAl IOREB

Este documento proporciona una vista consolidada de la inversión en APIs de IA, portadas y marketing para el desarrollo de la novela **Luz Vieja** y otros proyectos de la editorial.

---

## 📋 1. Propósito y Funcionamiento
Para garantizar la rentabilidad de las obras publicadas, se lleva un registro riguroso de cada token consumido durante los procesos de:
* Redacción de prosa (Escritor).
* Revisión de estilo y canon (Editor, Lorekeeper).
* Análisis de ritmo y beta-reading (Crítico).
* Comprobaciones mecánicas y maquetación (Productor, Orquestador).

El registro detallado se anexa línea a línea en `costes/ledger_tokens.jsonl`.

---

## 📊 2. Formato del Ledger (`ledger_tokens.jsonl`)
Cada interacción relevante debe registrarse con la siguiente estructura de datos JSON en una sola línea:

```json
{
  "timestamp": "YYYY-MM-DDTHH:mm:ss",
  "project": "luz_vieja",
  "workflow": "wf_luzvieja_01_escritor",
  "model": "claude-3-5-sonnet",
  "input_tokens": 12450,
  "output_tokens": 1820,
  "estimated_cost_eur": 0.089,
  "human_minutes": 15,
  "result_file": "manuscrito/capitulo_16.md",
  "notes": "Generación del borrador inicial del capítulo 16"
}
```

*Nota: Si se desconoce el número de tokens o el coste exacto, se mantendrán los valores correspondientes en `0` o `null` para evitar distorsiones en la contabilidad.*

---

## 📈 3. Balance Consolidado Actual

| Concepto | Coste Acumulado (EUR) | Estado / Notas |
| :--- | :--- | :--- |
| **Tokens de Entrada / API** | 0.00 EUR | Ledger inicializado |
| **Tokens de Salida / API** | 0.00 EUR | Ledger inicializado |
| **Diseño de Portada** | 0.00 EUR | Suscripción ChatGPT Plus (Coste fijo, excluido de variables) |
| **Servicios de Compilación** | 0.00 EUR | Compilación local por script |
| **Campañas de Promoción** | 0.00 EUR | Sin lanzar |
| **TOTAL INVERTIDO** | **0.00 EUR** | **Proyecto en fase de refactorización** |

---

## 🛠️ 4. Guía de Actualización y Optimización de Gastos
1. **Diferencia entre Estimado y Real:** Los costes de API registrados son estimaciones basadas en las tarifas de precios oficiales del proveedor en el momento de la llamada. El coste real se concilia mensualmente con la factura de la cuenta de API.
2. **Corte Quirúrgico de Contexto:** Evitar pasar el manuscrito completo en cada llamada si el modelo solo va a editar una escena específica. Cargar únicamente el perfil del proyecto, la regla aplicable y el texto a modificar.
3. **Uso de Modelos Baratos:** Tareas de formateo LaTeX, comprobación de nombres u ortografía deben enrutarse a modelos rápidos y de bajo coste.
