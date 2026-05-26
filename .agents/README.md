# EditorIAl IOREB - Infraestructura de Agentes

EditorIAl IOREB es una microeditorial asistida por IA. Su funcion es organizar trabajo literario semiautonomo sin perder control humano sobre manuscrito, canon, derechos, traducción y preparación de entrega local.

## Como Interactua el Humano

El usuario humano hace peticiones editoriales en lenguaje natural: escribir, revisar, auditar, traducir, crear premisas, preparar exportables o comprobar compliance.

El agente no ejecuta directamente la primera accion que parezca adecuada. Primero actua como CEO:

1. Lee `.agents/manifest.yaml`.
2. Clasifica la intencion.
3. Carga `.agents/ORQUESTADOR.md`.
4. Aplica `wf_editorial_00_ejecucion_semiautonoma.md`.
5. Selecciona el rol responsable.
6. Carga el workflow canonico del rol.
7. Usa solo las skills necesarias.
8. Respeta siempre reglas editoriales, de genero y de novela.
9. Se detiene si una accion requiere aprobacion humana.

## Cadena Operativa

```text
Humano -> CEO/Orquestador -> Rol -> Workflow -> Skills -> Entregable
                                  \-> Rules siempre activas
```

* **CEO:** clasifica, enruta, controla permisos, costes y riesgos.
* **Rol:** adopta una responsabilidad editorial concreta.
* **Workflow:** define el procedimiento para una tarea.
* **Skill:** ejecuta una tecnica concreta y reutilizable.
* **Rule:** limita y protege todo el proceso.

## Arquitectura

```text
.agents/
  manifest.yaml
  ORQUESTADOR.md
  README.md
  tools/
  templates/
  editorial/
    roles/
    rules/
    skills/
    workflows/
  generos/<genero>/
    genre_profile.md
    rules/
    skills/
    workflows/
  novelas/<proyecto>/
    project_profile.md
    rules/
    skills/
    workflows/
```

Las carpetas canonicas son `.agents/editorial`, `.agents/generos` y `.agents/novelas`.

Las carpetas planas `.agents/rules`, `.agents/skills` y `.agents/workflows` son wrappers de compatibilidad. Un wrapper no debe contener logica propia: solo debe apuntar a una ruta canonica.

## Estructura Normalizada de Novela

Todo proyecto literario debe separar estas secciones:

```text
manuscrito/
trama/
  README.md
  premisas/
  escaletas/
biblia/
  personajes/
  mundo/
  tecnologia/
traducciones/{idioma}/
exportacion/{idioma}/
costes/
```

El Productor y los scripts de `.agents/tools/` deben escribir exportables en `exportacion/{idioma}/`, nunca dentro de `.agents/tools/`.

## Permisos

Acciones libres:
* Leer contexto.
* Emitir informes, propuestas, outlines y auditorias.
* Crear borradores no canonicos.

Requieren aprobacion humana:
* Modificar `manuscrito/`, `biblia/` o `trama/`.
* Reestructurar canon existente.
* Sobrescribir traducciones, portadas, metadatos o exportables finales.
* Cambiar estados a `listo_para_revision_humana` o `entrega_local_preparada`.

Prohibido:
* La publicación automatizada está totalmente excluida de las capacidades de la IA.
* Ocultar uso de IA.
* Borrar contenido canonico o historico sin orden explicita.
* Imitar marcas, autores, franquicias o portadas de terceros de forma confundible.

## Estados

* `propuesta`
* `borrador`
* `auditado`
* `requiere_aprobacion`
* `aprobado`

## Auditoria

Ejecutar:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents\tools\audit_agents.ps1
```

La auditoria valida:
* rutas declaradas en el manifiesto,
* front matter minimo,
* componentes canonicos huerfanos,
* wrappers con destino canonico,
* estructura minima de novela.


## Auditoría y saneamiento (recomendado)

Para auditar redundancias, wrappers sin destino, mojibake y referencias operativas no permitidas:

```bash
python .agents/tools/auditar_infraestructura_editorial.py
```

Salida:
- `.agents/reports/auditoria_infraestructura.json`

Interpretación rápida:
- `findings`: incidencias de codificación o verbos de acción externa automatizada.
- `missing_in_manifest`: documentos canónicos no declarados en `manifest.yaml`.
- `wrappers_without_target`: wrappers de compatibilidad que no apuntan a ruta canónica.
