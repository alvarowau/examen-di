from PySide6.QtWidgets import QWidget, QLineEdit, QMessageBox
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIntValidator, QColor

from views.conexion_ui import Ui_connection_bd
from models.config import DBConfig
from models.datos import BaseDAO
from util.message_box import MessageBox

class ConexionController(QWidget):
    volver_a_inicio = Signal()
    connection_successful = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_connection_bd()
        self.ui.setupUi(self)
        self.preparar_ui()

        self.ui.etqConexion.setText("Estado: Desconectado")
        self.ui.etqConexion.setAlignment(Qt.AlignCenter)
        self.ui.etqConexion.setStyleSheet("color: gray;")

        self.conectar_acciones()

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

    def conectar_acciones(self):
        self.ui.btn_clean.clicked.connect(self.limpiar_campos)
        self.ui.btn_volver.clicked.connect(self.volver)
        self.ui.btn_acept.clicked.connect(self.confirmar_conexion)

    def limpiar_campos(self):
        self.ui.line_bd.clear()
        self.ui.line_user.clear()
        self.ui.line_password.clear()
        self.ui.line_host.clear()
        self.ui.line_port.clear()
        self.ui.etqConexion.setText("Estado: Campos limpios")
        self.ui.etqConexion.setStyleSheet("color: gray;")
        print("Campos de conexión limpiados.")
        DBConfig.set_connected_status(False)

    def volver(self):
        self.volver_a_inicio.emit()

    def confirmar_conexion(self):
        db_name = self.ui.line_bd.text().strip()
        user = self.ui.line_user.text().strip()
        psw = self.ui.line_password.text().strip()
        host = self.ui.line_host.text().strip()
        port_str = self.ui.line_port.text().strip()

        if not all([db_name, user, psw, host, port_str]):
            self.ui.etqConexion.setText("Error: Todos los campos son obligatorios.")
            self.ui.etqConexion.setStyleSheet("color: red; font-weight: bold;")
            QMessageBox.warning(self, "Campos Incompletos", "Por favor, rellena todos los campos de conexión correctamente.")
            DBConfig.set_connected_status(False)
            return

        if not port_str.isdigit():
            self.ui.etqConexion.setText("Error: Puerto debe ser un número válido.")
            self.ui.etqConexion.setStyleSheet("color: red; font-weight: bold;")
            QMessageBox.warning(self, "Error de Puerto", "El puerto debe ser un número entero válido.")
            DBConfig.set_connected_status(False)
            return

        port = int(port_str)

        config = {
            "db": db_name, "user": user, "psw": psw, "host": host, "port": port,
        }
        DBConfig.set_config(config)

        try:
            dao = BaseDAO()
            dao.close()

            self.ui.etqConexion.setText("Conexión establecida con éxito (MySQL).")
            self.ui.etqConexion.setStyleSheet("color: green; font-weight: bold;")
            DBConfig.set_connected_status(True)
            self.connection_successful.emit()

        except Exception as e:
            self.ui.etqConexion.setText(f"Error de conexión: {e}")
            self.ui.etqConexion.setStyleSheet("color: red; font-weight: bold;")
            DBConfig.set_connected_status(False)
            MessageBox("Error de Conexión", "error", f"No se pudo conectar a la base de datos:\n{e}").show()