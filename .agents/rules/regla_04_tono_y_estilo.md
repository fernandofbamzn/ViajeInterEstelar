---
trigger: always_on
---

# Wrapper — regla_04_tono_y_estilo

Esta regla ha sido desglosada en tres niveles modulares para mejorar la reutilización de código:

1. **Nivel Editorial (Idioma es-ES y Tono Colaborativo):**
   `.agents/editorial/rules/regla_editorial_02_etica_ia_y_transparencia.md`
2. **Nivel de Género (Pacing Contemplativo y Muestra, No Cuentes):**
   `.agents/generos/hard_scifi_contemplativa/rules/regla_genero_05_tono_contemplativo.md`
3. **Nivel de Proyecto (Atmósfera y Voz de Luz Vieja):**
   `.agents/novelas/bitacora_centauri/rules/regla_bitacora_02_tono_bitacora.md`

Carga estos archivos según el proyecto y género activos.
