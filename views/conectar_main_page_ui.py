# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conectar_main_page.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from widgets.conectar_bd import ConectarBD

class Ui_ConectarMainPage(object):
    def setupUi(self, ConectarMainPage):
        if not ConectarMainPage.objectName():
            ConectarMainPage.setObjectName(u"ConectarMainPage")
        ConectarMainPage.resize(511, 400)
        self.verticalLayout = QVBoxLayout(ConectarMainPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_top)

        self.label = QLabel(ConectarMainPage)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.etqAviso = QLabel(ConectarMainPage)
        self.etqAviso.setObjectName(u"etqAviso")
        self.etqAviso.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.etqAviso.setFont(font)
        self.etqAviso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.etqAviso)

        self.conectarBDWidget = ConectarBD(ConectarMainPage)
        self.conectarBDWidget.setObjectName(u"conectarBDWidget")
        self.conectarBDWidget.setMinimumSize(QSize(0, 200))

        self.verticalLayout.addWidget(self.conectarBDWidget)

        self.btn_volver = QPushButton(ConectarMainPage)
        self.btn_volver.setObjectName(u"btn_volver")

        self.verticalLayout.addWidget(self.btn_volver)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_bottom)


        self.retranslateUi(ConectarMainPage)

        QMetaObject.connectSlotsByName(ConectarMainPage)
    # setupUi

    def retranslateUi(self, ConectarMainPage):
        ConectarMainPage.setWindowTitle(QCoreApplication.translate("ConectarMainPage", u"Conectar a Base de Datos", None))
        self.label.setText(QCoreApplication.translate("ConectarMainPage", u"se puede usar con el tabulador o con el raton volviendo a otro campo", None))
        self.etqAviso.setText(QCoreApplication.translate("ConectarMainPage", u"Estado de Conexi\u00f3n: Pendiente", None))
        self.btn_volver.setText(QCoreApplication.translate("ConectarMainPage", u"Volver", None))
    # retranslateUi

