# Bitácora de Prompts — Registro de Uso de IA (CAG Project)

### Entrada 1: Reinicio Limpio del Proyecto y Planificación de Sprints
- **Objetivo del prompt:** Limpiar el entorno de fallos previos, clonar el fork desde cero y estructurar la metodología Scrum uniendo Commits, Prompts e Informe.
- **Prompt usado:** "ya borre la carpeta del repositorio local empecemos clonando el fork..."
- **Resumen de la respuesta recibida:** La IA estructuró la hoja de ruta definitiva unificando el Sprint 1 (Infraestructura y Persistencia) con las pautas de Git y documentación en Word.
- **Decisión humana tomada:** Realizar un hard reset del entorno local para asegurar un historial de commits limpio y transparente.
- **Cambios realizados en el proyecto:** Clonación del repositorio, creación de la carpeta de evidencias y adición de SCRUM.md y PROMPTS.md en `docs/`.

--------------------------------------------------------------------------

### Entrada 2: Diagnóstico Inicial del Monolito (Requisito 3)
- **Objetivo del prompt:** Resolver el problema de importación de pytest y ejecutar la suite de pruebas base del repositorio.
- **Prompt usado:** "No module named pytest"
- **Resumen de la respuesta recibida:** La IA explicó que el error se debe a la resolución de rutas en entornos virtuales bajo Git Bash, recomendando la ejecución explícita mediante `python -m pytest`.
- **Decisión humana tomada:** Ejecutar el comando recomendado para obtener el estado del arte inicial del proyecto y documentar los fallos base (HTTP 501) requeridos por la rúbrica.
- **Cambios realizados en el proyecto:** Guardada la captura de pantalla de los tests fallando en `docs/evidencias/pruebas_base_fallando.png`.

----------------------------------------------------------------------------------------------

### Entrada 3: Implementación de la Capa de Persistencia del Módulo CAG
- **Objetivo del prompt:** Sustituir los marcadores de posición e implementar la lógica de persistencia real en la clase `ContextStore`.
- **Prompt usado:** `"""Base placeholder for student implementation.""" class ContextStore... [código base enviado] ... context_store ya te paso el assistant`
- **Resumen de la respuesta recibida:** La IA generó la lógica completa usando almacenamiento local en formato JSON, asegurando el aislamiento por `user_id` y normalizando el retorno de `list_for_user` en un formato de lista estructurada compatible con el validador.
- **Decisión humana tomada:** Utilizar un archivo JSON plano local por su simplicidad técnica y rapidez de lectura/escritura dentro de un monolito ligero, evitando añadir motores de bases de datos pesados que compliquen el despliegue.
- **Cambios realizados en el proyecto:** Actualización completa de `backend/context_store.py` y almacenamiento de la evidencia del éxito en `docs/evidencias/pruebas_contrato_exitosas.png`.
- **Verificación aplicada:** Ejecución de `python -m pytest`, comprobando que los contratos pasaron de error HTTP 501 a éxito total.