# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)
from . import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionConexi_n = QAction(MainWindow)
        self.actionConexi_n.setObjectName(u"actionConexi_n")
        self.actionProductos = QAction(MainWindow)
        self.actionProductos.setObjectName(u"actionProductos")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionInicio = QAction(MainWindow)
        self.actionInicio.setObjectName(u"actionInicio")
        self.actioncuestion2 = QAction(MainWindow)
        self.actioncuestion2.setObjectName(u"actioncuestion2")
        self.actioninformes = QAction(MainWindow)
        self.actioninformes.setObjectName(u"actioninformes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pagina_inicio = QWidget(self.page)
        self.pagina_inicio.setObjectName(u"pagina_inicio")
        self.gridLayout_3 = QGridLayout(self.pagina_inicio)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.pagina_inicio)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/brianda1.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.pagina_inicio, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_productos = QWidget()
        self.page_productos.setObjectName(u"page_productos")
        self.stackedWidget.addWidget(self.page_productos)
        self.page_custeion2 = QWidget()
        self.page_custeion2.setObjectName(u"page_custeion2")
        self.stackedWidget.addWidget(self.page_custeion2)
        self.page_custion3 = QWidget()
        self.page_custion3.setObjectName(u"page_custion3")
        self.stackedWidget.addWidget(self.page_custion3)
        self.page_conexion = QWidget()
        self.page_conexion.setObjectName(u"page_conexion")
        self.stackedWidget.addWidget(self.page_conexion)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuCuestion1 = QMenu(self.menubar)
        self.menuCuestion1.setObjectName(u"menuCuestion1")
        self.menuCuestion2 = QMenu(self.menubar)
        self.menuCuestion2.setObjectName(u"menuCuestion2")
        self.menuCuestion3 = QMenu(self.menubar)
        self.menuCuestion3.setObjectName(u"menuCuestion3")
        self.menuInicio = QMenu(self.menubar)
        self.menuInicio.setObjectName(u"menuInicio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCuestion1.menuAction())
        self.menubar.addAction(self.menuCuestion2.menuAction())
        self.menubar.addAction(self.menuCuestion3.menuAction())
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menuCuestion1.addAction(self.actionConexi_n)
        self.menuCuestion1.addAction(self.actionProductos)
        self.menuCuestion1.addAction(self.actionSalir)
        self.menuCuestion2.addAction(self.actioncuestion2)
        self.menuCuestion3.addAction(self.actioninformes)
        self.menuInicio.addAction(self.actionInicio)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConexi_n.setText(QCoreApplication.translate("MainWindow", u"Conexi\u00f3n", None))
        self.actionProductos.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionInicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.actioncuestion2.setText(QCoreApplication.translate("MainWindow", u"cuestion2", None))
        self.actioninformes.setText(QCoreApplication.translate("MainWindow", u"informes", None))
        self.label.setText("")
        self.menuCuestion1.setTitle(QCoreApplication.translate("MainWindow", u"Cuestion1", None))
        self.menuCuestion2.setTitle(QCoreApplication.translate("MainWindow", u"Cuestion2", None))
        self.menuCuestion3.setTitle(QCoreApplication.translate("MainWindow", u"Cuestion3", None))
        self.menuInicio.setTitle(QCoreApplication.translate("MainWindow", u"Inicio", None))
    # retranslateUi

