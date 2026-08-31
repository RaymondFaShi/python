# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(230, 408)
        Form.setMinimumSize(QSize(230, 408))
        Form.setMaximumSize(QSize(230, 408))
        Form.setBaseSize(QSize(230, 408))
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 90, 231, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.gridLayoutWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(48, 48))
        self.addButton.setMaximumSize(QSize(48, 48))
        self.addButton.setBaseSize(QSize(50, 50))
        self.addButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.addButton, 3, 3, 1, 1)

        self.number1 = QPushButton(self.gridLayoutWidget)
        self.number1.setObjectName(u"number1")
        self.number1.setMinimumSize(QSize(48, 48))
        self.number1.setMaximumSize(QSize(48, 48))
        self.number1.setBaseSize(QSize(50, 50))
        self.number1.setAutoDefault(False)

        self.gridLayout.addWidget(self.number1, 3, 0, 1, 1)

        self.modButton = QPushButton(self.gridLayoutWidget)
        self.modButton.setObjectName(u"modButton")
        self.modButton.setMinimumSize(QSize(48, 48))
        self.modButton.setMaximumSize(QSize(48, 48))
        self.modButton.setBaseSize(QSize(50, 50))
        self.modButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.modButton, 0, 2, 1, 1)

        self.number0 = QPushButton(self.gridLayoutWidget)
        self.number0.setObjectName(u"number0")
        self.number0.setMinimumSize(QSize(48, 48))
        self.number0.setMaximumSize(QSize(48, 48))
        self.number0.setBaseSize(QSize(50, 50))
        self.number0.setAutoDefault(False)

        self.gridLayout.addWidget(self.number0, 4, 1, 1, 1)

        self.number6 = QPushButton(self.gridLayoutWidget)
        self.number6.setObjectName(u"number6")
        self.number6.setMinimumSize(QSize(48, 48))
        self.number6.setMaximumSize(QSize(48, 48))
        self.number6.setBaseSize(QSize(50, 50))
        self.number6.setAutoDefault(False)

        self.gridLayout.addWidget(self.number6, 2, 2, 1, 1)

        self.number2 = QPushButton(self.gridLayoutWidget)
        self.number2.setObjectName(u"number2")
        self.number2.setMinimumSize(QSize(48, 48))
        self.number2.setMaximumSize(QSize(48, 48))
        self.number2.setBaseSize(QSize(50, 50))
        self.number2.setAutoDefault(False)

        self.gridLayout.addWidget(self.number2, 3, 1, 1, 1)

        self.mulButton = QPushButton(self.gridLayoutWidget)
        self.mulButton.setObjectName(u"mulButton")
        self.mulButton.setMinimumSize(QSize(48, 48))
        self.mulButton.setMaximumSize(QSize(48, 48))
        self.mulButton.setBaseSize(QSize(50, 50))
        self.mulButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.mulButton, 1, 3, 1, 1)

        self.equalButton = QPushButton(self.gridLayoutWidget)
        self.equalButton.setObjectName(u"equalButton")
        self.equalButton.setMinimumSize(QSize(48, 48))
        self.equalButton.setMaximumSize(QSize(48, 48))
        self.equalButton.setBaseSize(QSize(50, 50))
        self.equalButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.equalButton, 4, 3, 1, 1)

        self.subButton = QPushButton(self.gridLayoutWidget)
        self.subButton.setObjectName(u"subButton")
        self.subButton.setMinimumSize(QSize(48, 48))
        self.subButton.setMaximumSize(QSize(48, 48))
        self.subButton.setBaseSize(QSize(50, 50))
        self.subButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.subButton, 2, 3, 1, 1)

        self.decButton = QPushButton(self.gridLayoutWidget)
        self.decButton.setObjectName(u"decButton")
        self.decButton.setMinimumSize(QSize(48, 48))
        self.decButton.setMaximumSize(QSize(48, 48))
        self.decButton.setBaseSize(QSize(50, 50))
        self.decButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.decButton, 4, 2, 1, 1)

        self.acButton = QPushButton(self.gridLayoutWidget)
        self.acButton.setObjectName(u"acButton")
        self.acButton.setMinimumSize(QSize(48, 48))
        self.acButton.setMaximumSize(QSize(48, 48))
        self.acButton.setBaseSize(QSize(50, 50))
        self.acButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.acButton, 0, 1, 1, 1)

        self.number8 = QPushButton(self.gridLayoutWidget)
        self.number8.setObjectName(u"number8")
        self.number8.setMinimumSize(QSize(48, 48))
        self.number8.setMaximumSize(QSize(48, 48))
        self.number8.setBaseSize(QSize(50, 50))
        self.number8.setAutoDefault(False)

        self.gridLayout.addWidget(self.number8, 1, 1, 1, 1)

        self.number3 = QPushButton(self.gridLayoutWidget)
        self.number3.setObjectName(u"number3")
        self.number3.setMinimumSize(QSize(48, 48))
        self.number3.setMaximumSize(QSize(48, 48))
        self.number3.setBaseSize(QSize(50, 50))
        self.number3.setAutoDefault(False)

        self.gridLayout.addWidget(self.number3, 3, 2, 1, 1)

        self.delButton = QPushButton(self.gridLayoutWidget)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setMinimumSize(QSize(48, 48))
        self.delButton.setMaximumSize(QSize(48, 48))
        self.delButton.setBaseSize(QSize(50, 50))
        self.delButton.setStyleSheet(u"")
        self.delButton.setAutoDefault(False)
        self.delButton.setFlat(False)

        self.gridLayout.addWidget(self.delButton, 0, 0, 1, 1)

        self.number7 = QPushButton(self.gridLayoutWidget)
        self.number7.setObjectName(u"number7")
        self.number7.setMinimumSize(QSize(48, 48))
        self.number7.setMaximumSize(QSize(48, 48))
        self.number7.setBaseSize(QSize(50, 50))
        self.number7.setAutoDefault(False)

        self.gridLayout.addWidget(self.number7, 1, 0, 1, 1)

        self.number9 = QPushButton(self.gridLayoutWidget)
        self.number9.setObjectName(u"number9")
        self.number9.setMinimumSize(QSize(48, 48))
        self.number9.setMaximumSize(QSize(48, 48))
        self.number9.setBaseSize(QSize(50, 50))
        self.number9.setAutoDefault(False)

        self.gridLayout.addWidget(self.number9, 1, 2, 1, 1)

        self.number4 = QPushButton(self.gridLayoutWidget)
        self.number4.setObjectName(u"number4")
        self.number4.setMinimumSize(QSize(48, 48))
        self.number4.setMaximumSize(QSize(48, 48))
        self.number4.setBaseSize(QSize(50, 50))
        self.number4.setAutoDefault(False)

        self.gridLayout.addWidget(self.number4, 2, 0, 1, 1)

        self.number5 = QPushButton(self.gridLayoutWidget)
        self.number5.setObjectName(u"number5")
        self.number5.setMinimumSize(QSize(48, 48))
        self.number5.setMaximumSize(QSize(48, 48))
        self.number5.setBaseSize(QSize(50, 50))
        self.number5.setAutoDefault(False)

        self.gridLayout.addWidget(self.number5, 2, 1, 1, 1)

        self.divButton = QPushButton(self.gridLayoutWidget)
        self.divButton.setObjectName(u"divButton")
        self.divButton.setMinimumSize(QSize(48, 48))
        self.divButton.setMaximumSize(QSize(48, 48))
        self.divButton.setBaseSize(QSize(50, 50))
        self.divButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.divButton, 0, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(48, 48))
        self.pushButton_8.setMaximumSize(QSize(48, 48))
        self.pushButton_8.setBaseSize(QSize(50, 50))
        self.pushButton_8.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton_8, 4, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 303, 96))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.previewLabel = QLabel(self.verticalLayoutWidget)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setMinimumSize(QSize(0, 0))
        self.previewLabel.setMaximumSize(QSize(229, 30))
        font = QFont()
        font.setPointSize(20)
        self.previewLabel.setFont(font)
        self.previewLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.previewLabel.setWordWrap(True)
        self.previewLabel.setMargin(0)

        self.verticalLayout.addWidget(self.previewLabel)

        self.resultLabel = QLabel(self.verticalLayoutWidget)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setMaximumSize(QSize(230, 32))
        font1 = QFont()
        font1.setPointSize(29)
        self.resultLabel.setFont(font1)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setMargin(0)
        self.resultLabel.setIndent(1)

        self.verticalLayout.addWidget(self.resultLabel)


        self.retranslateUi(Form)

        self.delButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.number1.setText(QCoreApplication.translate("Form", u"1", None))
        self.modButton.setText(QCoreApplication.translate("Form", u"%", None))
        self.number0.setText(QCoreApplication.translate("Form", u"0", None))
        self.number6.setText(QCoreApplication.translate("Form", u"6", None))
        self.number2.setText(QCoreApplication.translate("Form", u"2", None))
        self.mulButton.setText(QCoreApplication.translate("Form", u"x", None))
        self.equalButton.setText(QCoreApplication.translate("Form", u"=", None))
        self.subButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.decButton.setText(QCoreApplication.translate("Form", u".", None))
        self.acButton.setText(QCoreApplication.translate("Form", u"AC", None))
        self.number8.setText(QCoreApplication.translate("Form", u"8", None))
        self.number3.setText(QCoreApplication.translate("Form", u"3", None))
        self.delButton.setText(QCoreApplication.translate("Form", u"DEL", None))
        self.number7.setText(QCoreApplication.translate("Form", u"7", None))
        self.number9.setText(QCoreApplication.translate("Form", u"9", None))
        self.number4.setText(QCoreApplication.translate("Form", u"4", None))
        self.number5.setText(QCoreApplication.translate("Form", u"5", None))
        self.divButton.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"None", None))
        self.previewLabel.setText("")
        self.resultLabel.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

