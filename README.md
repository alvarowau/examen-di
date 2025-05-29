# Mi EXAMEN

¡Bienvenido al proyecto **Mi Examen**! 👋

Esta aplicación te ayuda a gestionar productos de jardinería y a generar informes.

---

## Cómo Empezar 🚀

Todas las explicaciones súper sencillas sobre cómo configurar, ejecutar y probar esta aplicación se encuentran en el archivo llamado **[`funcionamiento.txt`](./funcionamiento.txt)** en la carpeta principal de este proyecto.

¡Solo abre [`funcionamiento.txt`](./funcionamiento.txt) para encontrar todas las instrucciones paso a paso!

---

## Estructura del Proyecto 📁

Aquí tienes un vistazo rápido a las carpetas y archivos principales de este proyecto:

* **`controllers/`**: Contiene la lógica de las ventanas de tu aplicación y algunos controladores JDBC.
* **`models/`**: Gestiona los datos y la interacción con la base de datos (incluyendo la configuración y los modelos de datos).
* **`views/`**: Define el aspecto de las ventanas de tu aplicación (interfaces de usuario).
* **`informes/`**: Guarda tus plantillas de informes (`.jrxml`) y los controladores JDBC necesarios (`mysql-connector-j-8.4.0.jar`).
* **`resources/`**: Contiene recursos como imágenes y archivos `.ui` para las interfaces de usuario.
* **`util/`**: Incluye utilidades de ayuda, como cuadros de mensajes.
* **`widgets/`**: Contiene widgets personalizados de la interfaz de usuario.

---

### Archivos clave en la raíz del proyecto:

* **`docker-compose.yml`**: Ayuda a configurar y ejecutar tu base de datos MySQL fácilmente con Docker.
* **`Dockerfile`**: Define cómo construir tu imagen de la base de datos MySQL.
* **`init.sql`**: Script SQL para inicializar tu base de datos MySQL.
* **`main.py`**: El archivo principal para ejecutar tu aplicación Python.
* **`requirements.txt`**: Lista todas las librerías de Python que tu proyecto necesita.
* **`run_doctests.py`**: El script para ejecutar las pruebas automáticas (doctests) del proyecto.
* **`funcionamiento.txt`**: **¡ESTE ARCHIVO!** ¡Aquí están todas las explicaciones detalladas y fáciles de entender para usar la aplicación!

---

¡Esperamos que este proyecto te sea muy útil! Si tienes alguna pregunta, consulta primero **[`funcionamiento.txt`](./funcionamiento.txt)**. 😊
