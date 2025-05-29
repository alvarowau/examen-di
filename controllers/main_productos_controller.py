from PySide6.QtWidgets import QAbstractItemView, QWidget, QHeaderView, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex, Qt, Signal

from views.main_productos_ui import Ui_main_productos
from models.datos import JardineriaRepository
from models.config import DBConfig
from util.message_box import MessageBox


class MainProductsController(QWidget):
    volver_a_inicio = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_productos()
        self.ui.setupUi(self)
        self.productos = None
        self.jardineria_dao = None

        if DBConfig.is_connected():
            self.initialize_ui()
        else:
            self.setup_empty_table_category()
            self.setup_empty_table_product()
            self.ui.table_category.setEnabled(False)
            self.ui.table_productos.setEnabled(False)

    def initialize_ui(self):
        try:
            self.setup_events()
            self.setup_table_category()
            self.setup_empty_table_product()
        except Exception as e:
            MessageBox("Error al configurar la UI de productos", "error", str(e)).show()
            self.ui.table_category.setEnabled(False)
            self.ui.table_productos.setEnabled(False)

    def setup_events(self):
        self.ui.table_category.clicked.connect(self.on_category_click)
        self.ui.btn_cerrar.clicked.connect(self.on_cerrar_click)

    def setup_table_category(self):
        if not DBConfig.is_connected():
            self.setup_empty_table_category()
            return

        try:
            self.ui.table_category.setEnabled(True)

            self.jardineria_dao = JardineriaRepository()
            categories = self.jardineria_dao.get_all()
            self.jardineria_dao.close()

            if categories is None:
                categories = []

            headers = ["gama", "descripcion_texto"]
            self.model = QStandardItemModel(len(categories), len(headers))
            self.model.setHorizontalHeaderLabels(headers)

            for row, category in enumerate(categories):
                gama_text = str(category.gama)
                descripcion_text = str(category.descripcion_texto)

                self.model.setItem(row, 0, QStandardItem(gama_text))
                self.model.setItem(row, 1, QStandardItem(descripcion_text))

            self.ui.table_category.setModel(self.model)
            self.ui.table_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.table_category.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_category.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_category.setEditTriggers(QAbstractItemView.NoEditTriggers)

        except Exception as e:
            MessageBox("Error al cargar la tabla de categorías", "error", details=str(e)).show()
            self.setup_empty_table_category()
            self.ui.table_category.setEnabled(False)

    def setup_empty_table_category(self):
        headers = ["gama", "descripcion_texto"]
        self.model = QStandardItemModel(0, len(headers))
        self.model.setHorizontalHeaderLabels(headers)
        self.ui.table_category.setModel(self.model)
        self.ui.table_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_category.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.table_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.table_category.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setup_empty_table_product(self):
        headers = ["codigo_producto", "nombre", "proveedor", "descripcion"]
        self.model_productos = QStandardItemModel(0, len(headers))
        self.model_productos.setHorizontalHeaderLabels(headers)
        self.ui.table_productos.setModel(self.model_productos)
        self.ui.table_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_productos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.table_productos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.table_productos.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def on_cerrar_click(self):
        self.volver_a_inicio.emit()

    def on_category_click(self, index: QModelIndex):
        if not DBConfig.is_connected():
            QMessageBox.warning(self, "Sin Conexión", "No hay conexión a la base de datos para cargar productos.")
            self.setup_empty_table_product()
            return

        try:
            self.ui.table_productos.setEnabled(True)

            row = index.row()
            name_category = self.model.item(row, 0).text()

            self.jardineria_dao = JardineriaRepository()
            self.productos = self.jardineria_dao.get_all_product_gama(name_category)
            self.jardineria_dao.close()

            self.setup_table_product()
        except Exception as e:
            MessageBox("Error al seleccionar categoría", "error", details=str(e)).show()
            self.setup_empty_table_product()
            self.ui.table_productos.setEnabled(False)

    def setup_table_product(self):
        try:
            headers = ["codigo_producto", "nombre", "proveedor", "descripcion"]

            if self.productos is None:
                self.productos = []
            elif not isinstance(self.productos, list):
                self.productos = [self.productos]

            self.model_productos = QStandardItemModel(len(self.productos), len(headers))
            self.model_productos.setHorizontalHeaderLabels(headers)

            for row, product in enumerate(self.productos):
                self.model_productos.setItem(row, 0, QStandardItem(str(product.codigo_producto)))
                self.model_productos.setItem(row, 1, QStandardItem(str(product.nombre)))
                self.model_productos.setItem(row, 2, QStandardItem(str(product.proveedor)))
                self.model_productos.setItem(row, 3, QStandardItem(str(product.descripcion)))

            self.ui.table_productos.setModel(self.model_productos)
            self.ui.table_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.table_productos.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_productos.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_productos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        except Exception as e:
            MessageBox("No se pudo cargar la tabla de productos", "error", details=str(e)).show()
            self.setup_empty_table_product()
            self.ui.table_productos.setEnabled(False)