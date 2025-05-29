# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conectar_bd_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_ConectarBDWidget(object):
    def setupUi(self, ConectarBDWidget):
        if not ConectarBDWidget.objectName():
            ConectarBDWidget.setObjectName(u"ConectarBDWidget")
        ConectarBDWidget.resize(400, 300)
        self.gridLayout_main = QGridLayout(ConectarBDWidget)
        self.gridLayout_main.setObjectName(u"gridLayout_main")
        self.label_bd = QLabel(ConectarBDWidget)
        self.label_bd.setObjectName(u"label_bd")

        self.gridLayout_main.addWidget(self.label_bd, 0, 0, 1, 1)

        self.line_bd = QLineEdit(ConectarBDWidget)
        self.line_bd.setObjectName(u"line_bd")

        self.gridLayout_main.addWidget(self.line_bd, 0, 1, 1, 1)

        self.label_user = QLabel(ConectarBDWidget)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout_main.addWidget(self.label_user, 1, 0, 1, 1)

        self.line_user = QLineEdit(ConectarBDWidget)
        self.line_user.setObjectName(u"line_user")

        self.gridLayout_main.addWidget(self.line_user, 1, 1, 1, 1)

        self.label_password = QLabel(ConectarBDWidget)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout_main.addWidget(self.label_password, 2, 0, 1, 1)

        self.line_password = QLineEdit(ConectarBDWidget)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_main.addWidget(self.line_password, 2, 1, 1, 1)

        self.label_host = QLabel(ConectarBDWidget)
        self.label_host.setObjectName(u"label_host")

        self.gridLayout_main.addWidget(self.label_host, 3, 0, 1, 1)

        self.line_host = QLineEdit(ConectarBDWidget)
        self.line_host.setObjectName(u"line_host")

        self.gridLayout_main.addWidget(self.line_host, 3, 1, 1, 1)

        self.label_port = QLabel(ConectarBDWidget)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout_main.addWidget(self.label_port, 4, 0, 1, 1)

        self.line_port = QLineEdit(ConectarBDWidget)
        self.line_port.setObjectName(u"line_port")

        self.gridLayout_main.addWidget(self.line_port, 4, 1, 1, 1)


        self.retranslateUi(ConectarBDWidget)

        QMetaObject.connectSlotsByName(ConectarBDWidget)
    # setupUi

    def retranslateUi(self, ConectarBDWidget):
        ConectarBDWidget.setWindowTitle(QCoreApplication.translate("ConectarBDWidget", u"Form", None))
        self.label_bd.setText(QCoreApplication.translate("ConectarBDWidget", u"Base de Datos:", None))
        self.label_user.setText(QCoreApplication.translate("ConectarBDWidget", u"Usuario:", None))
        self.label_password.setText(QCoreApplication.translate("ConectarBDWidget", u"Contrase\u00f1a:", None))
        self.label_host.setText(QCoreApplication.translate("ConectarBDWidget", u"Host:", None))
        self.label_port.setText(QCoreApplication.translate("ConectarBDWidget", u"Puerto:", None))
    # retranslateUi

