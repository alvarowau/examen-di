# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_productos.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_main_productos(object):
    def setupUi(self, main_productos):
        if not main_productos.objectName():
            main_productos.setObjectName(u"main_productos")
        main_productos.resize(831, 510)
        self.gridLayout = QGridLayout(main_productos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_title = QLabel(main_productos)
        self.txt_title.setObjectName(u"txt_title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.txt_title.setFont(font)
        self.txt_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_title, 0, 0, 1, 1)

        self.table_category = QTableView(main_productos)
        self.table_category.setObjectName(u"table_category")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_category.sizePolicy().hasHeightForWidth())
        self.table_category.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.table_category.setFont(font1)

        self.gridLayout.addWidget(self.table_category, 1, 0, 1, 1)

        self.table_productos = QTableView(main_productos)
        self.table_productos.setObjectName(u"table_productos")
        sizePolicy.setHeightForWidth(self.table_productos.sizePolicy().hasHeightForWidth())
        self.table_productos.setSizePolicy(sizePolicy)
        self.table_productos.setFont(font1)

        self.gridLayout.addWidget(self.table_productos, 2, 0, 1, 1)

        self.btn_cerrar = QPushButton(main_productos)
        self.btn_cerrar.setObjectName(u"btn_cerrar")

        self.gridLayout.addWidget(self.btn_cerrar, 3, 0, 1, 1)


        self.retranslateUi(main_productos)

        QMetaObject.connectSlotsByName(main_productos)
    # setupUi

    def retranslateUi(self, main_productos):
        main_productos.setWindowTitle(QCoreApplication.translate("main_productos", u"main_productos", None))
#if QT_CONFIG(tooltip)
        self.txt_title.setToolTip(QCoreApplication.translate("main_productos", u"student", None))
#endif // QT_CONFIG(tooltip)
        self.txt_title.setText(QCoreApplication.translate("main_productos", u"Productos", None))
#if QT_CONFIG(tooltip)
        self.table_category.setToolTip(QCoreApplication.translate("main_productos", u"Listado de estudiantes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.table_productos.setToolTip(QCoreApplication.translate("main_productos", u"Listado de estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cerrar.setText(QCoreApplication.translate("main_productos", u"CERRAR", None))
    # retranslateUi

