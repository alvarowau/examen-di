from PySide6.QtWidgets import QMainWindow, QApplication, QGridLayout, QMessageBox
from PySide6.QtCore import Qt

from views.main_windows_ui import Ui_MainWindow
from controllers.conexion_controller import ConexionController
from controllers.main_productos_controller import MainProductsController
from controllers.conectar_controller import ConectarController
from controllers.informe_controller import InformesVentana
from models.config import DBConfig


class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conexion_controller = ConexionController()
        self.main_productos_controller = MainProductsController()
        self.conectar_act2_controller = ConectarController()
        self.informes_controller = InformesVentana()

        if self.ui.page_conexion.layout():
            for i in reversed(range(self.ui.page_conexion.layout().count())):
                self.ui.page_conexion.layout().itemAt(i).widget().setParent(None)
            self.ui.page_conexion.layout().deleteLater()
        layout_conexion_page = QGridLayout(self.ui.page_conexion)
        layout_conexion_page.addWidget(self.conexion_controller)
        self.ui.page_conexion.setLayout(layout_conexion_page)

        if self.ui.page_productos.layout():
            for i in reversed(range(self.ui.page_productos.layout().count())):
                self.ui.page_productos.layout().itemAt(i).widget().setParent(None)
            self.ui.page_productos.layout().deleteLater()
        layout_producto_page = QGridLayout(self.ui.page_productos)
        layout_producto_page.addWidget(self.main_productos_controller)
        self.ui.page_productos.setLayout(layout_producto_page)

        if self.ui.page_custeion2.layout():
            for i in reversed(range(self.ui.page_custeion2.layout().count())):
                self.ui.page_custeion2.layout().itemAt(i).widget().setParent(None)
            self.ui.page_custeion2.layout().deleteLater()
        layout_conectar_act2_page = QGridLayout(self.ui.page_custeion2)
        layout_conectar_act2_page.addWidget(self.conectar_act2_controller)
        self.ui.page_custeion2.setLayout(layout_conectar_act2_page)

        if self.ui.page_custion3.layout():
            for i in reversed(range(self.ui.page_custion3.layout().count())):
                self.ui.page_custion3.layout().itemAt(i).widget().setParent(None)
            self.ui.page_custion3.layout().deleteLater()
        layout_crear_informes_page = QGridLayout(self.ui.page_custion3)
        layout_crear_informes_page.addWidget(self.informes_controller)
        self.ui.page_custion3.setLayout(layout_crear_informes_page)

        self.setup_connections()
        self.set_initial_ui_state()

    def setup_connections(self):
        self.ui.actionConexi_n.triggered.connect(self.show_old_connection_page)
        self.ui.actionProductos.triggered.connect(self.show_products_page)
        self.ui.actionSalir.triggered.connect(self.close_application)
        self.ui.actionInicio.triggered.connect(self.show_home_page)
        self.ui.menuCuestion2.triggered.connect(self.show_new_conectar_page)
        self.ui.actioninformes.triggered.connect(self.show_crear_informe)

        self.conexion_controller.connection_successful.connect(self.handle_connection_status_change)
        self.conectar_act2_controller.connection_successful.connect(self.handle_connection_status_change)

        self.conexion_controller.volver_a_inicio.connect(self.show_home_page)
        self.main_productos_controller.volver_a_inicio.connect(self.show_home_page)
        self.conectar_act2_controller.volver_a_inicio.connect(self.show_home_page)

    def set_initial_ui_state(self):
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.menuCuestion2.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)

        self._update_dependent_actions_state()

        self.show_home_page()

    def _update_dependent_actions_state(self):
        is_connected = DBConfig.is_connected()
        self.ui.actionProductos.setEnabled(is_connected)
        self.ui.actioninformes.setEnabled(is_connected)

        if is_connected:
            self.ui.statusbar.showMessage("Conexión a la base de datos establecida.")
            self.main_productos_controller.initialize_ui()
        else:
            self.ui.statusbar.showMessage("Desconectado de la base de datos.")
            self.main_productos_controller.setup_empty_table_category()
            self.main_productos_controller.setup_empty_table_product()


    def handle_connection_status_change(self):
        print("DEBUG: handle_connection_status_change llamado. Actualizando estado UI.")
        self._update_dependent_actions_state()


    def show_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.statusbar.showMessage("Mostrando la página de inicio...")
        self._update_dependent_actions_state()


    def show_old_connection_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.statusbar.showMessage("Mostrando la antigua página de conexión...")
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)

    def show_crear_informe(self):
        if DBConfig.is_connected():
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.statusbar.showMessage("Mostrando la página de los informes...")
        else:
            QMessageBox.warning(self, "Acceso Denegado", "Debes establecer una conexión a la base de datos primero para generar informes.")
            self.ui.statusbar.showMessage("Acceso a informes denegado: No hay conexión.")
            self.show_home_page()


    def show_new_conectar_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.statusbar.showMessage("Mostrando la página de conexión (Actividad 2)...")
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)


    def show_products_page(self):
        if DBConfig.is_connected():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.statusbar.showMessage("Mostrando la página de productos...")
        else:
            QMessageBox.warning(self, "Acceso Denegado", "Debes establecer una conexión a la base de datos primero.")
            self.ui.statusbar.showMessage("Acceso a productos denegado: No hay conexión.")
            self.show_home_page()

    def close_application(self):
        self.ui.statusbar.showMessage("Saliendo de la aplicación...")
        self.close()