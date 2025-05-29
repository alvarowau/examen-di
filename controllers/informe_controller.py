import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QWidget

from controllers.crear_informe import advanced_example_using_database
from models.config import DBConfig
from views.informe_ui import Ui_Informe


class InformesVentana(QWidget):
    """Ventana para generación de informes utilizando JasperReports.

    Args:
        conexion (dict, optional): Configuración de conexión a BD. Defaults to None.
        parent (QWidget, optional): Widget padre. Defaults to None.
    """

    def __init__(self, conexion=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Informe()
        self.ui.setupUi(self)
        self.conexion = conexion

        # Configuración básica de la ventana
        self.setWindowTitle("Generar Informe")
        self.setWindowModality(Qt.ApplicationModal)

        # Conexión de señales
        self.ui.pushButton_informe.clicked.connect(self.generar_informe)

    def generar_informe(self):
        """Genera un informe a partir de la plantilla JRXML seleccionada."""
        try:
            # Configuración de rutas
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ruta_informes = os.path.join(base_dir, "informes")

            # Crear directorio si no existe
            if not os.path.exists(ruta_informes):
                os.makedirs(ruta_informes)

            # Definir tipo de informe y rutas
            tipo_informe = "Cliente"
            fichero_entrada = os.path.join(ruta_informes, f"{tipo_informe}.jrxml")
            fichero_salida = os.path.join(ruta_informes, tipo_informe)

            # Validar existencia del archivo JRXML
            if not os.path.exists(fichero_entrada):
                QMessageBox.critical(
                    self, "Error", f"Archivo no encontrado: {fichero_entrada}"
                )
                return

            # Obtener configuración de la base de datos
            config = DBConfig.get_config()

            # Configuración de conexión para JasperReports
            con = {
                "driver": "mysql",
                "username": config["user"],
                "password": config["psw"],
                "host": config["host"],
                "database": config["db"],
                "schema": "DB_SCHEMA",
                "port": int(config["port"]),
                "jdbc_driver": "com.mysql.cj.jdbc.Driver",
                "jdbc_dir": os.path.join(
                    os.path.dirname(__file__), "mysql-connector-java-8.0.30.jar"
                ),
                "jdbc_url": f"jdbc:mysql://{config['host']}:{config['port']}/{config['db']}?serverTimezone=Europe/Madrid",
            }

            # Generar el informe
            advanced_example_using_database(fichero_entrada, fichero_salida, con, {})

            QMessageBox.information(
                self, "Éxito", f"Informe generado en:\n{fichero_salida}"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al generar informe:\n{str(e)}")
