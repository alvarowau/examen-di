# main.py
import sys
from PySide6.QtWidgets import QApplication
import os  # Necesario para os.path.join y os.path.abspath

# --- ¡AÑADE ESTAS LÍNEAS PARA LA CONFIGURACIÓN DE PYREPORTJASPER! ---
import pyreportjasper

# Ruta al JAR JDBC dentro de tu proyecto.
# Apunta a la carpeta 'informes' y al nombre de tu JAR específico.
_JDBC_JAR_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),  # Ruta de main.py (raíz del proyecto)
    'informes',  # Tu carpeta 'informes'
    'mysql-connector-j-8.4.0.jar'  # ¡Tu nombre exacto del JAR y versión!
)

# Añade el JAR al classpath global de pyreportjasper.
# Esto es crucial para que JasperReports (Java) pueda encontrar el driver MySQL.
pyreportjasper.classpath = [_JDBC_JAR_PATH]
# -------------------------------------------------------------------

from controllers.main_window_controller import MainWindowController

if __name__ == "__main__":
    # QApplication se inicializa con una lista vacía si no necesitas argumentos de línea de comandos.
    app = QApplication([])

    ventana = MainWindowController()
    ventana.show()

    # Inicia el bucle de eventos de la aplicación.
    sys.exit(app.exec())  # Usar sys.exit() y app.exec() es la forma estándar y segura.