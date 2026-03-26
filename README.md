# Sistema de Gestión de Biblioteca Pro (Django)

Este proyecto es una aplicación web profesional desarrollada con **Django**. Permite gestionar un catálogo de libros con un sistema de seguridad por niveles y una interfaz moderna.

## Características Principales
*   **CRUD Profesional:** Gestión completa de libros (Crear, Leer, Editar, Eliminar).
*   **Seguridad y Permisos:** 
    *   **Visitantes:** Acceso de solo lectura (botones de edición ocultos).
    *   **Administradores:** Acceso total tras iniciar sesión (Navbar dinámica con nombre de usuario).
*   **Buscador Inteligente:** Filtro en tiempo real por título de libro.
*   **Interfaz Moderna:** Diseño responsivo con **Bootstrap 5**, tarjetas (Cards) e iconografía de **FontAwesome**.
*   **Notificaciones:** Alertas visuales de éxito para cada acción realizada.

## Tecnologías Utilizadas
*   **Backend:** Python 3.x / Django
*   **Frontend:** Bootstrap 5, FontAwesome (Iconos CDN)
*   **Base de Datos:** SQLite3

## Cómo Ejecutar el Proyecto
1.  **Clonar el repositorio:** `git clone [URL-DE-TU-REPO]`
2.  **Crear entorno virtual:** `python -m venv venv`
3.  **Activar entorno:** `.\venv\Scripts\activate` (Windows)
4.  **Instalar librerías:** `pip install -r requirements.txt`
5.  **Migrar base de datos:** `python manage.py migrate`
6.  **Iniciar servidor:** `python manage.py runserver`

Acceso local: `http://127.0.0.1`

---
**Nota del Desarrollador:** Este portafolio refleja mi capacidad para construir soluciones seguras, ordenadas y enfocadas en la experiencia del usuario final.
