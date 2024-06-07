# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serial_port.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1056, 584)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(191, 300))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.formLayoutWidget_2 = QWidget(self.widget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 10, 161, 141))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(7)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox_2 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)

        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox_3 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_3)

        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBox_4 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBox_4)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBox_5 = QComboBox(self.formLayoutWidget_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox_5)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(45, 160, 133, 22))
        self.labelStatus = QLabel(self.widget)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(20, 160, 16, 21))
        self.labelStatus.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus.setTextFormat(Qt.AutoText)
        self.pushButton_scan = QPushButton(self.widget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(20, 190, 151, 24))
        self.pushButton_scan_classic = QPushButton(self.widget)
        self.pushButton_scan_classic.setObjectName(u"pushButton_scan_classic")
        self.pushButton_scan_classic.setGeometry(QRect(20, 220, 151, 24))
        self.labelStatus_2 = QLabel(self.widget)
        self.labelStatus_2.setObjectName(u"labelStatus_2")
        self.labelStatus_2.setGeometry(QRect(20, 260, 31, 21))
        self.labelStatus_2.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_2.setTextFormat(Qt.AutoText)
        self.labelStatus_3 = QLabel(self.widget)
        self.labelStatus_3.setObjectName(u"labelStatus_3")
        self.labelStatus_3.setGeometry(QRect(80, 260, 31, 21))
        self.labelStatus_3.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_3.setTextFormat(Qt.AutoText)
        self.labelStatus_4 = QLabel(self.widget)
        self.labelStatus_4.setObjectName(u"labelStatus_4")
        self.labelStatus_4.setGeometry(QRect(140, 260, 31, 21))
        self.labelStatus_4.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_4.setFrameShadow(QFrame.Plain)
        self.labelStatus_4.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.widget, 0, 0, 2, 1)

        self.dockWidget = QDockWidget(Form)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_3 = QWidget(self.dockWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(6)
        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 6, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 0))

        self.gridLayout_2.addWidget(self.label_6, 0, 7, 1, 1)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.checkBox_4 = QCheckBox(self.widget_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 5, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.gridLayout_7.addWidget(self.dockWidget, 0, 1, 1, 1)

        self.dockWidget_2 = QDockWidget(Form)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.verticalLayout.addLayout(self.gridLayout_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout.addLayout(self.gridLayout_5)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.gridLayout_7.addWidget(self.dockWidget_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"115200", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"57600", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"38400", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"25600", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"19200", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Form", u"9600", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Form", u"4800", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("Form", u"2400", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("Form", u"115200", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u4f4d\uff1a", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"8", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"7", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"6", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"5", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Form", u"3", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Form", u"2", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"No", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Form", u"Even", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Form", u"Odd", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("Form", u"Space", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("Form", u"Mark", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e32\u53e3", None))
        self.labelStatus.setText("")
        self.pushButton_scan.setText(QCoreApplication.translate("Form", u"\u641c\u7d22BLE\u84dd\u7259", None))
        self.pushButton_scan_classic.setText(QCoreApplication.translate("Form", u"\u641c\u7d22\u7ecf\u5178\u84dd\u7259", None))
        self.labelStatus_2.setText("")
        self.labelStatus_3.setText("")
        self.labelStatus_4.setText("")
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u63a5\u6536\u5230\u6587\u4ef6", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"20", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"ms", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"ff aa 03 08 00 ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Hex", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u63a5\u6536\u533a", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u53d1\u9001", None))
    # retranslateUi

