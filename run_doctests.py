import doctest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import models.datos


def run_all_doctests():
    """Ejecuta todos los doctests del módulo models.datos y muestra los resultados.

    Imprime un resumen detallado de las pruebas ejecutadas y un mensaje de éxito/fallo.

    Returns:
        None: Los resultados se imprimen directamente en la consola.
    """
    print("\n--- Iniciando ejecución de Doctests ---")
    results = doctest.testmod(models.datos, verbose=True)

    if results.failed == 0:
        print(
            f"\n--- ¡Todos los {results.attempted} Doctests PASARON con éxito! 🎉 ---"
        )
    else:
        print(
            f"\n--- ¡ATENCIÓN! Fallaron {results.failed} de {results.attempted} Doctests. 😥 ---"
        )


if __name__ == "__main__":
    """Configura la base de datos de prueba y ejecuta los doctests."""
    print(
        "DEBUG: Asegurando que la configuración de la Base de Datos sea para el doctest."
    )

    from models.config import DBConfig

    # Configuración de la base de datos de prueba (Docker Compose)
    DBConfig.set_config(
        {
            "db": "jardineria",
            "user": "root",
            "psw": "root",
            "host": "localhost",
            "port": 3307,
        }
    )

    run_all_doctests()
