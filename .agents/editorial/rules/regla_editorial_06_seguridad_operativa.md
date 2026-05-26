---
id: regla_editorial_06_seguridad_operativa
title: "Seguridad Operativa y Protección de Activos"
scope: editorial
trigger: always_on
---

# Seguridad Operativa y Protección de Activos

## 📋 Contexto y Motivación
La infraestructura y el contenido de la editorial (el manuscrito y la biblia) representan el activo principal del proyecto. Los agentes deben actuar con precaución extrema al interactuar con el sistema de archivos y las herramientas del sistema.

## 🛠️ Directriz Inviolable
1. **Comandos Destructivos Prohibidos:** Queda terminantemente prohibido ejecutar comandos en la terminal que borren, limpien o alteren de forma masiva directorios del repositorio sin una orden explícita del usuario (ej: `rm -rf`, `git clean -fdx` sobre carpetas de contenido).
2. **Protección de Datos Sensibles:** Ningún agente debe leer ni almacenar en archivos del repositorio claves de API, tokens de GitHub, contraseñas ni credenciales.
3. **No Modificar .gitignore Irresponsablemente:** No alterar el archivo `.gitignore` si esto pudiera resultar en la subida accidental de archivos secretos o del entorno local al control de versiones.
4. **Respeto a los Archivos No Relacionados:** No modificar archivos fuera del alcance de la tarea asignada (como el código de maquetación preexistente o assets como `portada.png`).

## 🛑 Lo que NUNCA debe hacerse
* Proponer o ejecutar comandos de borrado de archivos del manuscrito, trama o biblia.
* Almacenar contraseñas en archivos Markdown o JSON de la carpeta `.agents/`.

## ✅ Comportamiento Esperado
* Limitar los cambios a los archivos estrictamente necesarios para la tarea actual (cambios quirúrgicos).
* Advertir inmediatamente al usuario si se detecta un archivo de configuración que exponga secretos.
