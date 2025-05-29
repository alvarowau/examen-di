from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMessageBox, QWidget

from models.config import DBConfig
from models.datos import BaseDAO
from util.message_box import MessageBox
from views.conectar_main_page_ui import Ui_ConectarMainPage


class ConectarController(QWidget):
    """Controlador para la interfaz de conexión a base de datos.

    Attributes:
        connection_successful (Signal): Se emite cuando la conexión es exitosa.
        volver_a_inicio (Signal): Se emite al solicitar volver al inicio.
    """

    connection_successful = Signal()
    volver_a_inicio = Signal()

    def __init__(self, parent=None):
        """Inicializa el controlador de conexión.

        Args:
            parent (QWidget, optional): Widget padre. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_ConectarMainPage()
        self.ui.setupUi(self)

        self._set_initial_state()
        self._connect_signals()

    def _set_initial_state(self):
        """Configura el estado inicial de la interfaz."""
        self.ui.etqAviso.setText("Estado: Pendiente de conexión")
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.etqAviso.setStyleSheet("color: gray;")
        self.ui.etqAviso.setAlignment(Qt.AlignCenter)
        self.ui.conectarBDWidget.colorFondo = QColor(Qt.white)

    def volver(self):
        """Emite la señal para volver a la pantalla de inicio."""
        self.volver_a_inicio.emit()

    def _connect_signals(self):
        """Conecta las señales internas de los widgets."""
        self.ui.conectarBDWidget.connection_data_ready.connect(
            self.handle_connection_data
        )

    def handle_connection_data(self, config_data: dict):
        """Procesa los datos de conexión recibidos del widget.

        Args:
            config_data (dict): Diccionario con parámetros de conexión:
                - db: Nombre de la base de datos
                - user: Usuario
                - psw: Contraseña
                - host: Dirección del servidor
                - port: Puerto de conexión
        """

        db_name = config_data.get("db", "").strip()
        user = config_data.get("user", "").strip()
        psw = config_data.get("psw", "").strip()
        host = config_data.get("host", "").strip()
        port = config_data.get("port", 0)

        if not all([db_name, user, psw, host, port]) or port == 0:
            self.ui.etqAviso.setText("Error: Faltan datos o puerto inválido.")
            self.ui.etqAviso.setStyleSheet("color: red;")
            self.ui.conectarBDWidget.colorFondo = QColor(Qt.red)
            QMessageBox.warning(
                self,
                "Campos Incompletos",
                "Por favor, rellena todos los campos de conexión correctamente.",
            )
            return

        DBConfig.set_config(config_data)

        try:
            dao = BaseDAO()
            dao.close()

            self.ui.etqAviso.setText("Conexión establecida con éxito (MySQL).")
            self.ui.etqAviso.setStyleSheet("color: green; font-weight: bold;")
            self.ui.conectarBDWidget.colorFondo = QColor(Qt.green)
            DBConfig.set_connected_status(True)
            self.connection_successful.emit()

        except Exception as e:
            self.ui.etqAviso.setText(f"Error de conexión: {e}")
            self.ui.etqAviso.setStyleSheet("color: red; font-weight: bold;")
            self.ui.conectarBDWidget.colorFondo = QColor(Qt.red)
            DBConfig.set_connected_status(False)
            MessageBox(
                "Error de Conexión",
                "error",
                f"No se pudo conectar a la base de datos:\n{e}",
            ).show()
