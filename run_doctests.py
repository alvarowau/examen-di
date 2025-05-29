import doctest  # La herramienta que busca y ejecuta los doctests
import sys  # Para ajustar cómo Python busca los archivos
import os  # Para trabajar con las rutas de los archivos

# Ajustamos la ruta para que Python pueda encontrar tus otros módulos (como 'models')
# Esto le dice a Python que mire en la carpeta "padre" de donde está este script.
# Es importante para que 'import models.datos' funcione.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo donde hemos puesto nuestro doctest
import models.datos


def run_all_doctests():
    """
    Función principal para ejecutar todas las pruebas doctest que tenemos.
    """
    print("\n--- Iniciando ejecución de Doctests ---")

    # Aquí es donde la magia ocurre:
    # doctest.testmod() busca todos los doctests en el módulo 'models.datos'
    # verbose=True nos muestra más detalles mientras los tests se ejecutan
    results = doctest.testmod(models.datos, verbose=True)

    # Una vez que los tests terminan, imprimimos un mensaje de éxito o fracaso
    if results.failed == 0:
        print(f"\n--- ¡Todos los {results.attempted} Doctests PASARON con éxito! 🎉 ---")
    else:
        print(f"\n--- ¡ATENCIÓN! Fallaron {results.failed} de {results.attempted} Doctests. 😥 ---")


# Esta parte asegura que el código solo se ejecute cuando ejecutes este archivo directamente
if __name__ == "__main__":
    # IMPORTANTE: Antes de ejecutar los tests, necesitamos decirle a tu programa
    # cómo conectar a la base de datos para que el test de conexión funcione.
    # Aquí le ponemos la configuración de tu base de datos de Docker Compose.
    print("DEBUG: Asegurando que la configuración de la Base de Datos sea para el doctest.")

    # Importamos DBConfig para poder configurar la conexión
    from models.config import DBConfig

    # Configuramos la base de datos de prueba (¡AJUSTA ESTOS VALORES SI SON DIFERENTES!)
    DBConfig.set_config({
        'db': 'jardineria',  # Nombre de tu base de datos
        'user': 'root',  # Usuario de tu base de datos
        'psw': 'root',  # Contraseña de tu base de datos
        'host': 'localhost',  # Dónde está tu base de datos (si es Docker, suele ser localhost desde el host)
        'port': 3307  # El puerto que usas para conectar a la base de datos Docker
    })

    # Ahora sí, ¡ejecutamos todos los doctests!
    run_all_doctests()