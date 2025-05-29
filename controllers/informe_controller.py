from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from views.informe_ui import Ui_Informe
from controllers.crear_informe import advanced_example_using_database
from models.datos import BaseDAO
from models.config import DBConfig
import os


class InformesVentana(QWidget):
    def __init__(self, conexion=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Informe()
        self.ui.setupUi(self)
        self.conexion = conexion

        self.setWindowTitle("Generar Informe")
        self.setWindowModality(Qt.ApplicationModal)

        self.ui.pushButton_informe.clicked.connect(self.generar_informe)

    def generar_informe(self):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ruta_informes = os.path.join(base_dir, "informes")

            if not os.path.exists(ruta_informes):
                os.makedirs(ruta_informes)

            tipo_informe = "Clientes"
            fichero_entrada = os.path.join(ruta_informes, f"{tipo_informe}.jrxml")
            fichero_salida = os.path.join(ruta_informes, tipo_informe)

            if not os.path.exists(fichero_entrada):
                QMessageBox.critical(self, "Error",
                                     f"Archivo no encontrado: {fichero_entrada}")
                return

            config = DBConfig.get_config()
            print(DBConfig.get_config())

            con = {
                'driver': 'mysql',
                'username': config['user'],
                'password': config['psw'],
                'host': config['host'],
                'database': config['db'],
                'schema': 'DB_SCHEMA',
                'port': int(config['port']),
                'jdbc_driver': 'com.mysql.cj.jdbc.Driver',
                'jdbc_dir': os.path.join(os.path.dirname(__file__), 'mysql-connector-java-8.0.30.jar'),
                'jdbc_url': f"jdbc:mysql://{config['host']}:{config['port']}/{config['db']}?serverTimezone=Europe/Madrid"
            }

            advanced_example_using_database(
                fichero_entrada,
                fichero_salida,
                con,{}
            )

            QMessageBox.information(self, "Éxito",
                                    f"Informe generado en:\n{fichero_salida}")

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 f"Error al generar informe:\n{str(e)}")