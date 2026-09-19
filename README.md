# TPA - Gestor de Tareas

![Estado](https://img.shields.io/badge/Estado-en%20desarrollo-yellow)

Proyecto desarrollado progresivamente a lo largo de las clases de **Técnicas de 
Programación Avanzada**. Es un gestor de tareas en Python que se va ampliando 
conforme avanzan los contenidos de las asignaturas.

## Features actuales

* **Modelo de datos (`Tarea`)**
  * Atributos: título, descripción, prioridad, días restantes y tag.
  * Clasificación automática según días restantes: `Urgente`, `Próxima`, `Sin prisa`
  * Validación de datos mediante `@property` (título no vacío, prioridad y estado dentro de valores permitidos, días restantes no negativos).
  * Registro automático de la última fecha de modificación.
  * Constructor alternativo desde diccionario.
* **Gestión de tareas (`GestorTareas`)**
  * Añadir y eliminar tareas.
  * Búsqueda por título (por lista y mediante conversión a diccionario).
  * Mostrar una tarea o todas almacenadas.
  * Copia de tareas (superficial y profunda) con `copy`.
* **Persistencia (`GestorArchivos`)**
  * Guardado de tareas en un archivo `.txt`.
  * Carga de tareas desde archivo, fusionando las tareas existentes en memoria y eliminando tareas duplicadas y/o corruptas.
* **CLI (GestorTareasCLI)**
  * Command Line Interface para acceder a todas las funcionalidades anteriores.
