# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informe.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Informe(object):
    def setupUi(self, Informe):
        if not Informe.objectName():
            Informe.setObjectName(u"Informe")
        Informe.resize(509, 326)
        Informe.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Informe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(Informe)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_informe = QPushButton(self.widget)
        self.pushButton_informe.setObjectName(u"pushButton_informe")
        font = QFont()
        font.setFamilies([u"MADE Tommy Soft"])
        font.setPointSize(15)
        font.setWeight(QFont.ExtraBold)
        font.setItalic(False)
        self.pushButton_informe.setFont(font)
        self.pushButton_informe.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_informe, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Informe)

        QMetaObject.connectSlotsByName(Informe)
    # setupUi

    def retranslateUi(self, Informe):
        Informe.setWindowTitle(QCoreApplication.translate("Informe", u"Informe", None))
#if QT_CONFIG(tooltip)
        self.pushButton_informe.setToolTip(QCoreApplication.translate("Informe", u"Conectar con la base de datos.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_informe.setText(QCoreApplication.translate("Informe", u"GENERAR INFORME", None))
    # retranslateUi

