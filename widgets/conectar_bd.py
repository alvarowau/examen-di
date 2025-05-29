# widgets/conectar_bd.py
from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import Signal, Property, Qt
from PySide6.QtGui import QIntValidator, QColor, QPalette, QBrush # Importa QPalette y QBrush

from views.conectar_bd_widget_ui import Ui_ConectarBDWidget


class ConectarBD(QWidget):
    connection_data_ready = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConectarBDWidget()
        self.ui.setupUi(self)

        # ------------------------------------------------------------------
        # ¡CORRECCIONES PARA EL FONDO COMPLETO AQUÍ!
        # 1. autoFillBackground es buena práctica para QWidget que pintan su fondo.
        self.setAutoFillBackground(True)
        # 2. Establece un QPalette para el fondo, que es más fiable que solo setStyleSheet
        #    para el fondo de un QWidget que contiene otros widgets.
        self._background_color = QColor(Qt.white) # Color de fondo inicial
        self.update_background_style() # Aplicar el estilo inicial
        # ------------------------------------------------------------------

        self.preparar_ui()
        self.conectar_eventos()


    def preparar_ui(self):
        self.ui.line_bd.setText("jardineria")
        self.ui.line_user.setText("root")
        self.ui.line_password.setText("root")
        self.ui.line_password.setEchoMode(QLineEdit.Password)
        self.ui.line_host.setText("localhost")

        validador = QIntValidator()
        self.ui.line_port.setPlaceholderText("Ingresa solo números")
        self.ui.line_port.setValidator(validador)
        self.ui.line_port.setText("3306")

    def conectar_eventos(self):
        self.ui.line_port.editingFinished.connect(self.emit_connection_data)

    def emit_connection_data(self):
        print("DEBUG: emit_connection_data() en ConectarBD llamado.")
        db_name = self.ui.line_bd.text().strip()
        user = self.ui.line_user.text().strip()
        psw = self.ui.line_password.text().strip()
        host = self.ui.line_host.text().strip()
        port_str = self.ui.line_port.text().strip()

        try:
            port = int(port_str)
        except ValueError:
            port = 0

        connection_data = {
            "db": db_name,
            "user": user,
            "psw": psw,
            "host": host,
            "port": port,
        }
        print(f"DEBUG: Componente ConectarBD emitiendo señal con datos: {connection_data}")
        self.connection_data_ready.emit(connection_data)

    # --- Implementación de la propiedad personalizada "colorFondo" ---
    def get_background_color(self):
        return self._background_color

    def set_background_color(self, color: QColor):
        if self._background_color != color:
            self._background_color = color
            self.update_background_style()

    colorFondo = Property(QColor, get_background_color, set_background_color, designable=True, user=True)

    def update_background_style(self):
        """
        Actualiza el color de fondo del widget usando QPalette,
        que es más fiable para QWidgets contenedores que setStyleSheet directo del fondo.
        """
        # Creas una paleta basada en la actual del widget
        palette = self.palette()
        # Estableces el color del rol de fondo
        palette.setBrush(QPalette.Window, QBrush(self._background_color))
        # Aplicas la nueva paleta al widget
        self.setPalette(palette)
        # Forzar un repintado (aunque setPalette a menudo lo hace automáticamente)
        self.update()

        # Opcional: Si quieres bordes redondeados y padding, aún puedes usar setStyleSheet
        # para esas propiedades, pero no para el color de fondo principal.
        # self.setStyleSheet(f"QWidget#ConectarBDWidget {{ border-radius: 5px; padding: 10px; }}")