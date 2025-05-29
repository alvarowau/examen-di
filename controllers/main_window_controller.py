from PySide6.QtWidgets import QGridLayout, QMainWindow, QMessageBox

from controllers.conectar_controller import ConectarController
from controllers.conexion_controller import ConexionController
from controllers.informe_controller import InformesVentana
from controllers.main_productos_controller import MainProductsController
from models.config import DBConfig
from views.main_windows_ui import Ui_MainWindow


class MainWindowController(QMainWindow):
    """
    Controlador principal de la aplicación.

    Gestiona la navegación entre las diferentes vistas (páginas) de la aplicación,
    la inicialización de los controladores de cada vista y el estado de la conexión a la base de datos.

    Attributes:
        ui (Ui_MainWindow): Instancia de la interfaz de usuario generada por Qt Designer.
        conexion_controller (ConexionController): Controlador para la página de conexión.
        main_productos_controller (MainProductsController): Controlador para la página de productos.
        conectar_act2_controller (ConectarController): Controlador para la segunda página de conexión (Actividad 2).
        informes_controller (InformesVentana): Controlador para la página de informes.
    """

    def __init__(self):
        """
        Inicializa la clase MainWindowController.

        Configura la interfaz de usuario, inicializa los controladores de las diferentes páginas
        y los integra en el stacked widget principal.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conexion_controller = ConexionController()
        self.main_productos_controller = MainProductsController()
        self.conectar_act2_controller = ConectarController()
        self.informes_controller = InformesVentana()

        # Configuración del layout para la página de conexión
        if self.ui.page_conexion.layout():
            for i in reversed(range(self.ui.page_conexion.layout().count())):
                self.ui.page_conexion.layout().itemAt(i).widget().setParent(None)
            self.ui.page_conexion.layout().deleteLater()
        layout_conexion_page = QGridLayout(self.ui.page_conexion)
        layout_conexion_page.addWidget(self.conexion_controller)
        self.ui.page_conexion.setLayout(layout_conexion_page)

        # Configuración del layout para la página de productos
        if self.ui.page_productos.layout():
            for i in reversed(range(self.ui.page_productos.layout().count())):
                self.ui.page_productos.layout().itemAt(i).widget().setParent(None)
            self.ui.page_productos.layout().deleteLater()
        layout_producto_page = QGridLayout(self.ui.page_productos)
        layout_producto_page.addWidget(self.main_productos_controller)
        self.ui.page_productos.setLayout(layout_producto_page)

        # Configuración del layout para la segunda página de conexión (Actividad 2)
        if self.ui.page_custeion2.layout():
            for i in reversed(range(self.ui.page_custeion2.layout().count())):
                self.ui.page_custeion2.layout().itemAt(i).widget().setParent(None)
            self.ui.page_custeion2.layout().deleteLater()
        layout_conectar_act2_page = QGridLayout(self.ui.page_custeion2)
        layout_conectar_act2_page.addWidget(self.conectar_act2_controller)
        self.ui.page_custeion2.setLayout(layout_conectar_act2_page)

        # Configuración del layout para la página de informes
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
        """
        Configura las conexiones de señales y slots para la navegación y el estado de la aplicación.
        """
        self.ui.actionConexi_n.triggered.connect(self.show_old_connection_page)
        self.ui.actionProductos.triggered.connect(self.show_products_page)
        self.ui.actionSalir.triggered.connect(self.close_application)
        self.ui.actionInicio.triggered.connect(self.show_home_page)
        self.ui.menuCuestion2.triggered.connect(self.show_new_conectar_page)
        self.ui.actioninformes.triggered.connect(self.show_crear_informe)

        self.conexion_controller.connection_successful.connect(
            self.handle_connection_status_change
        )
        self.conectar_act2_controller.connection_successful.connect(
            self.handle_connection_status_change
        )

        self.conexion_controller.volver_a_inicio.connect(self.show_home_page)
        self.main_productos_controller.volver_a_inicio.connect(self.show_home_page)
        self.conectar_act2_controller.volver_a_inicio.connect(self.show_home_page)

    def set_initial_ui_state(self):
        """
        Establece el estado inicial de los elementos de la interfaz de usuario al iniciar la aplicación.
        """
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.menuCuestion2.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)

        self._update_dependent_actions_state()

        self.show_home_page()

    def _update_dependent_actions_state(self):
        """
        Actualiza el estado de las acciones del menú que dependen de la conexión a la base de datos.
        """
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
        """
        Maneja el cambio en el estado de la conexión a la base de datos.

        Actualiza el estado de la interfaz de usuario para reflejar si hay conexión o no.
        """
        self._update_dependent_actions_state()

    def show_home_page(self):
        """
        Muestra la página de inicio de la aplicación.
        """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.statusbar.showMessage("Mostrando la página de inicio...")
        self._update_dependent_actions_state()

    def show_old_connection_page(self):
        """
        Muestra la página de conexión original (conexión 1).
        """
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.statusbar.showMessage("Mostrando la antigua página de conexión...")
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)

    def show_crear_informe(self):
        """
        Muestra la página de creación de informes.

        Solo permite el acceso si hay una conexión a la base de datos establecida.
        """
        if DBConfig.is_connected():
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.statusbar.showMessage("Mostrando la página de los informes...")
        else:
            QMessageBox.warning(
                self,
                "Acceso Denegado",
                "Debes establecer una conexión a la base de datos primero para generar informes.",
            )
            self.ui.statusbar.showMessage(
                "Acceso a informes denegado: No hay conexión."
            )
            self.show_home_page()

    def show_new_conectar_page(self):
        """
        Muestra la segunda página de conexión (conexión 2).
        """
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.statusbar.showMessage(
            "Mostrando la página de conexión (Actividad 2)..."
        )
        self.ui.actionConexi_n.setEnabled(True)
        self.ui.actionInicio.setEnabled(True)

    def show_products_page(self):
        """
        Muestra la página de productos.

        Solo permite el acceso si hay una conexión a la base de datos establecida.
        """
        if DBConfig.is_connected():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.statusbar.showMessage("Mostrando la página de productos...")
        else:
            QMessageBox.warning(
                self,
                "Acceso Denegado",
                "Debes establecer una conexión a la base de datos primero.",
            )
            self.ui.statusbar.showMessage(
                "Acceso a productos denegado: No hay conexión."
            )
            self.show_home_page()

    def close_application(self):
        """
        Cierra la aplicación.
        """
        self.ui.statusbar.showMessage("Saliendo de la aplicación...")
        self.close()
