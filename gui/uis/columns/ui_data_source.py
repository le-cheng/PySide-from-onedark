# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_source.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_data_source(object):
    def setupUi(self, data_source):
        if not data_source.objectName():
            data_source.setObjectName(u"data_source")
        data_source.resize(298, 502)
        self.gridLayout = QGridLayout(data_source)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(data_source)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabBarAutoHide(False)

        self.serial_port = QWidget()
        self.serial_port.setObjectName(u"serial_port")
        self.gridLayout_2 = QGridLayout(self.serial_port)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.serial_port)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(191, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.formLayoutWidget_2 = QWidget(self.widget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 10, 161, 141))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(7)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(102, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.labelStatus.setTextFormat(Qt.TextFormat.AutoText)
        self.pushButton_scan = QPushButton(self.widget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(20, 200, 151, 24))
        self.pushButton_scan_classic = QPushButton(self.widget)
        self.pushButton_scan_classic.setObjectName(u"pushButton_scan_classic")
        self.pushButton_scan_classic.setGeometry(QRect(20, 240, 151, 24))
        self.labelStatus_2 = QLabel(self.widget)
        self.labelStatus_2.setObjectName(u"labelStatus_2")
        self.labelStatus_2.setGeometry(QRect(20, 290, 31, 21))
        self.labelStatus_2.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_2.setTextFormat(Qt.TextFormat.AutoText)
        self.labelStatus_3 = QLabel(self.widget)
        self.labelStatus_3.setObjectName(u"labelStatus_3")
        self.labelStatus_3.setGeometry(QRect(80, 290, 31, 21))
        self.labelStatus_3.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_3.setTextFormat(Qt.TextFormat.AutoText)
        self.labelStatus_4 = QLabel(self.widget)
        self.labelStatus_4.setObjectName(u"labelStatus_4")
        self.labelStatus_4.setGeometry(QRect(140, 290, 31, 21))
        self.labelStatus_4.setStyleSheet(u"QLabel{\n"
"border-radius: 8px;\n"
"background-color: gray;\n"
"}")
        self.labelStatus_4.setFrameShadow(QFrame.Shadow.Plain)
        self.labelStatus_4.setTextFormat(Qt.TextFormat.AutoText)
        self.pushButton_file = QPushButton(self.widget)
        self.pushButton_file.setObjectName(u"pushButton_file")
        self.pushButton_file.setGeometry(QRect(20, 340, 151, 24))

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.serial_port, "")
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.tabWidget.addTab(self.network, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(data_source)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(data_source)
    # setupUi

    def retranslateUi(self, data_source):
        data_source.setWindowTitle(QCoreApplication.translate("data_source", u"Form", None))
        self.label.setText(QCoreApplication.translate("data_source", u"\u4e32\u53e3\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("data_source", u"\u6ce2\u7279\u7387\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("data_source", u"115200", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("data_source", u"57600", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("data_source", u"38400", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("data_source", u"25600", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("data_source", u"19200", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("data_source", u"9600", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("data_source", u"4800", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("data_source", u"2400", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("data_source", u"115200", None))
        self.label_3.setText(QCoreApplication.translate("data_source", u"\u6570\u636e\u4f4d\uff1a", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("data_source", u"8", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("data_source", u"7", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("data_source", u"6", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("data_source", u"5", None))

        self.label_4.setText(QCoreApplication.translate("data_source", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("data_source", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("data_source", u"3", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("data_source", u"2", None))

        self.label_5.setText(QCoreApplication.translate("data_source", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("data_source", u"No", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("data_source", u"Even", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("data_source", u"Odd", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("data_source", u"Space", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("data_source", u"Mark", None))

        self.pushButton.setText(QCoreApplication.translate("data_source", u"\u6253\u5f00\u4e32\u53e3", None))
        self.labelStatus.setText("")
        self.pushButton_scan.setText(QCoreApplication.translate("data_source", u"\u641c\u7d22BLE\u84dd\u7259", None))
        self.pushButton_scan_classic.setText(QCoreApplication.translate("data_source", u"\u641c\u7d22\u7ecf\u5178\u84dd\u7259", None))
        self.labelStatus_2.setText("")
        self.labelStatus_3.setText("")
        self.labelStatus_4.setText("")
        self.pushButton_file.setText(QCoreApplication.translate("data_source", u"\u52a0\u8f7d\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serial_port), QCoreApplication.translate("data_source", u"serial port", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.network), QCoreApplication.translate("data_source", u"network", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("data_source", u"tab", None))
    # retranslateUi

