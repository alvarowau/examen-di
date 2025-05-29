# main.py
import sys
from PySide6.QtWidgets import QApplication


from controllers.main_window_controller import MainWindowController

if __name__ == "__main__":
    """Punto de entrada principal de la aplicación."""
    app = QApplication([])

    ventana = MainWindowController()
    ventana.show()

    sys.exit(app.exec())