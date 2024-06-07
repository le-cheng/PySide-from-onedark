# -*- coding: utf-8 -*-

# from turtle import left, right
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QFontDatabase,
    QImage, QKeySequence, QLinearGradient, QPainter, QIntValidator,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget, QPlainTextEdit, QTextEdit,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser, QSpacerItem,
    QVBoxLayout, QWidget, QHBoxLayout)
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QObject, Slot

from gui.widgets.py_label_edit.py_label_edit import LabelQComboBoxRoundedRectFrame, LabelQLineEditRoundedRectFrame
from gui.widgets.py_push_button.py_toggle_color_push_button import ToggleColorButton


class label_combobox_frame(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # 设置内部间距
        layout.setAlignment(Qt.AlignVCenter)

        # 创建文本标签
        text_label = QLabel("选择一个选项:", self)

        # 创建下拉框
        combo_box = QComboBox(self)
        combo_box.addItems(["选项1", "选项2", "选项3", "选项4"])

        # 将文本标签和下拉框添加到布局中
        layout.addWidget(text_label)
        layout.addWidget(combo_box)

        # 设置圆角样式
        self.setStyleSheet("""
            label_combobox_frame {
                background-color: #FFFFFF; /* 背景颜色 */
                border: 2px solid #CCCCCC; /* 边框宽度和颜色 */
                border-radius: 10px; /* 圆角半径 */
                padding: 5px; /* 内边距，让内容和边框有间隔 */
            }
        """)

class label_text_frame(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 设置内部间距
        layout.setAlignment(Qt.AlignVCenter)

        left_frame = QFrame()
        left_frame.setObjectName("left_frame")
        left_frame.setStyleSheet("""
            left_frame {
                background-color: #e9ecef; /* 背景颜色 */
            }
        """)

        # 创建文本标签
        text_label = QLabel("选择一个选项:", self)
        left_layout = QVBoxLayout(left_frame)
        left_layout.addWidget(text_label)

        right_frame = QFrame()
        # right_frame.setObjectName("right_frame")
        # right_frame.setStyleSheet("""
        #     right_frame {
        #         background-color: None; /* 背景颜色 */
        #         border: 2px solid #CCCCCC; /* 边框宽度和颜色 */
        #         /*border-radius: 10px; */  /* 圆角半径 */
        #         padding: 5px; /* 内边距，让内容和边框有间隔 */
        #     }
        #     """)


        # 创建下拉框
        combo_box = QComboBox(self)
        combo_box.addItems(["选项1", "选项2", "选项3", "选项4"])
        right_layout = QVBoxLayout(right_frame)
        right_layout.addWidget(combo_box)

        # 将文本标签和下拉框添加到布局中
        layout.addWidget(left_frame)
        layout.addWidget(right_frame)

        # 设置圆角样式
        # self.setStyleSheet("""
        #     RoundedFrame {
        #         background-color: #FFFFFF; /* 背景颜色 */
        #         border: 2px solid #CCCCCC; /* 边框宽度和颜色 */
        #         border-radius: 10px; /* 圆角半径 */
        #         padding: 5px; /* 内边距，让内容和边框有间隔 */
        #     }
        # """)

class RoundedRectFrame(QFrame):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        # self.setStyleSheet("""
        #     QFrame {
        #         border: 2px solid #d0d6db;
        #         background-color: #e9ecef;  /* 灰色背景 */
        #     }
        # """)
        bg_layout = QVBoxLayout(self)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        # bg_layout.setSpacing(0)

        bg_frame = QFrame()
        bg_frame.setStyleSheet(f'''
                border-radius: 2px;
                border: 1px solid #ff0000;
                background-color: #e9ecef;
            ''')
        bg_layout.addWidget(bg_frame)


        layout = QHBoxLayout(bg_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 创建标签并设置字体颜色
        label = QLabel(text)
        label.setStyleSheet("background-color:#e9ecef; color: black;")
        layout.addWidget(label)

        # 创建一个输入框并限制输入类型为数字
        line_edit = QLineEdit()
        line_edit.setValidator(QIntValidator(0, 9999))  # 限制为数字输入
        label.setStyleSheet("""border: 2px solid #d0d6db;
                            background-color: white;""")
        layout.addWidget(line_edit)



class Ui_SerialPort(object):
    def setupUi(self, parent_pages, show_border = 0):
        if not parent_pages.objectName():
            parent_pages.setObjectName(u"parent_pages")
        sp_bg_layout = QHBoxLayout(parent_pages)
        sp_bg_layout.setContentsMargins(0, 0, 0, 0)
        sp_bg_layout.setSpacing(1)

        sp_logger_frame = QFrame()

        if show_border:
            sp_logger_frame.setObjectName(u"sp_logger_frame")
            sp_logger_frame.setStyleSheet(f'''
            #sp_logger_frame {{
                border-radius: 8px;
                border: 1px solid #ff0000;
            }}
            ''')

        sp_logger_layout = QVBoxLayout(sp_logger_frame)
        sp_logger_layout.setContentsMargins(0, 0, 0, 0)
        sp_logger_layout.setSpacing(3)

        #///////////////////////////////////////////////////
        # top
        #///////////////////////////////////////////////////
        sp_logger_top_widget = QFrame()
        sp_logger_top_widget.setFixedHeight(60)
        if show_border:
            sp_logger_top_widget.setObjectName(u"sp_logger_top_widget")

            sp_logger_top_widget.setStyleSheet(f'''
            #sp_logger_top_widget {{
                border-radius: 8px;
                border: 1px solid #fff000;
            }}
            ''')

        sp_logger_top_h_layout = QHBoxLayout(sp_logger_top_widget)
        sp_logger_top_h_layout.setContentsMargins(0, 0, 0, 0)
        sp_logger_top_h_layout.setSpacing(0)

        sp_logger_layout.addWidget(sp_logger_top_widget)

        # 1
        # 方法一
        # logo_label = QLabel("# 串口日志")
        # logo_label.setTextFormat(Qt.MarkdownText)
        # 方法二
        logo_label = QLabel()
        # HTML 通过 CSS 属性 font-family 可以设置中文字体 格式的文本，包含加粗、字号增大和改变字体的部分
        # SimSun (宋体), SimHei (黑体), Microsoft Yahei (微软雅黑), PingFang SC (苹方), 和 Source Han Sans (思源黑体）
        # 'KaiTi', 'DFKai-SB', 'KaiTi_GB2312', 'STKaiti'
        html_text = '''
        <div style="font-family: 'Microsoft Yahei', 'Arial', sans-serif; font-size: 20pt;">
            <span style="font-size: 28pt; font-family: 'Microsoft Yahei';"><b>串口日志</b></span>
        </div>
        '''
        # 设置 QLabel 的文本内容为 HTML 格式
        logo_label.setText(html_text)
        logo_label.setFixedHeight(60)
        if show_border:
            logo_label.setStyleSheet(f'''
                    border-radius: 8px;
                    border: 1px solid #ff0000;
                ''')
        logo_label.setTextFormat(Qt.TextFormat.RichText)
        logo_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        sp_logger_top_h_layout.addWidget(logo_label)

        # 2
        self.sp_logger_top_subcontracting_timeout = LabelQLineEditRoundedRectFrame("分包超时", 160, 40)
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_subcontracting_timeout)

        # 3
        self.sp_logger_top_logger_type = LabelQComboBoxRoundedRectFrame("日志类型", 160, 40)
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_logger_type)

        # 4
        self.sp_logger_top_toggle_clear = ToggleColorButton(QIcon("source/example.png"), "清空")
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_toggle_clear)

        # 5
        self.sp_logger_top_toggle_auto_scrolling = ToggleColorButton(QIcon("source/example.png"), "自动滚动")
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_toggle_auto_scrolling)

        # 6
        self.sp_logger_top_toggle_documents_accepted = ToggleColorButton(QIcon("source/example.png"), "接收到文件")
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_toggle_documents_accepted)

        # 7
        self.sp_logger_top_toggle_export = ToggleColorButton(QIcon("source/example.png"), "导出")
        sp_logger_top_h_layout.addWidget(self.sp_logger_top_toggle_export)


        # middle
        #////////////////////////////////////////////////////////////
        sp_logger_middle_widget = QFrame()
        # sp_logger_middle_widget.setFixedHeight(80)
        if show_border:
            sp_logger_middle_widget.setObjectName(u"sp_logger_middle_widget")

            sp_logger_top_widget.setStyleSheet(f'''
            #sp_logger_middle_widget {{
                border-radius: 8px;
                border: 1px solid #fff000;
            }}
            ''')

        sp_logger_middle_h_layout = QHBoxLayout(sp_logger_middle_widget)
        sp_logger_middle_h_layout.setContentsMargins(0, 0, 0, 0)
        sp_logger_middle_h_layout.setSpacing(3)

        sp_logger_layout.addWidget(sp_logger_middle_widget)


        # # 创建QTextBrowser实例
        # self.sp_logger_middle_text_browser = QTextBrowser()
        # content = """
        # <h1>Welcome to QTextBrowser</h1>
        # <p>This is an example of using QTextBrowser to display <b>rich text</b>.</p>
        # <ul>
        #     <li>You can use <a href="https://www.example.com">links</a>.</li>
        #     <li>Include <i>italic</i>, <b>bold</b>, and <u>underlined</u> text.</li>
        #     <li>Even add images: <img src="path_to_your_image.png" alt="Image description">
        # </ul>
        # """
        # self.sp_logger_middle_text_browser.setHtml(content)

        # left
        self.sp_logger_middle_reception = QPlainTextEdit()
        self.sp_logger_middle_reception.setReadOnly(True)
        self.sp_logger_middle_reception.setObjectName("sp_logger_middle_plain_RoundQPlainTextEdit")
        self.sp_logger_middle_reception.setStyleSheet("""
            QPlainTextEdit#sp_logger_middle_plain_RoundQPlainTextEdit {
                border-radius: 10px; /* 设置圆角大小 */
                /* background-color: #F0F0F0;  可选：设置背景颜色 */
                border: 2px solid #8f8f91;
                padding: 5px;  /* 可选：设置内边距 */
                font-size: 12pt;
            }
            """)

        self.sp_logger_middle_reception.appendPlainText("logger!")

        sp_logger_middle_h_layout.addWidget(self.sp_logger_middle_reception)

        # right
        self.sp_logger_middle_reception_right = QTextEdit()
        self.sp_logger_middle_reception_right.setReadOnly(True)
        self.sp_logger_middle_reception_right.setObjectName("sp_logger_middle_reception_right")
        self.sp_logger_middle_reception_right.setStyleSheet("""
            QTextEdit#sp_logger_middle_reception_right {
                border-radius: 10px; /* 设置圆角大小 */
                /* background-color: #F0F0F0;  可选：设置背景颜色 */
                border: 2px solid #8f8f91;
                padding: 5px;  /* 可选：设置内边距 */
                font-size: 12pt;
            }
            """)
        sp_logger_middle_h_layout.addWidget(self.sp_logger_middle_reception_right)


        # button
        #/////////////////////////////////////////////////////////////
        sp_logger_button_widget = QFrame()
        sp_logger_button_widget.setFixedHeight(80)
        if show_border:
            sp_logger_button_widget.setObjectName(u"sp_logger_button_widget")

            sp_logger_top_widget.setStyleSheet(f'''
            #sp_logger_button_widget {{
                border-radius: 8px;
                border: 1px solid #fff000;
            }}
            ''')

        sp_logger_button_v_layout = QVBoxLayout(sp_logger_button_widget)
        sp_logger_button_v_layout.setContentsMargins(0, 0, 0, 0)
        sp_logger_button_v_layout.setSpacing(0)

        sp_logger_layout.addWidget(sp_logger_button_widget)

        # 1
        self.sp_logger_button_send = QPlainTextEdit()
        self.sp_logger_button_send.setObjectName("sp_logger_button_send")
        self.sp_logger_button_send.setStyleSheet("""
            QPlainTextEdit#sp_logger_button_send {
                border-radius: 10px; /* 设置圆角大小 */
                /* background-color: #F0F0F0;  可选：设置背景颜色 */
                border: 2px solid #8f8f91;
                padding: 5px;  /* 可选：设置内边距 */
                font-size: 12pt;
            }
            """)

        self.sp_logger_button_send.setPlaceholderText("在此输入要发送的内容，可以是字符串（如：你好，世界！），也可以是HEX(如：49544c4447)")
        sp_logger_button_v_layout.addWidget(self.sp_logger_button_send)

        # 2

        self.sp_logger_button_vh_layout = QHBoxLayout()
        self.sp_logger_button_vh_layout.setObjectName(u"sp_logger_button_vh_layout")
        self.sp_logger_button_vh_layout.setSpacing(3)

        self.checkBox_2 = QCheckBox()
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setText(f"\\n")

        self.sp_logger_button_vh_layout.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox()
        self.checkBox_4.setObjectName(u"checkBox_4")
        # self.checkBox_4.setChecked(False)
        self.checkBox_4.setText(f"Hex")

        self.sp_logger_button_vh_layout.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox()
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setText(f"循环发送")

        self.sp_logger_button_vh_layout.addWidget(self.checkBox_3)

        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFixedWidth(40)
        # self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_2.setText(u"20")
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.sp_logger_button_vh_layout.addWidget(self.lineEdit_2)

        self.label_6 = QLabel()
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 0))
        self.label_6.setText("ms")

        self.sp_logger_button_vh_layout.addWidget(self.label_6)

        spacerItem = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.sp_logger_button_vh_layout.addItem(spacerItem)

        self.pushButton_3 = ToggleColorButton(QIcon("source/example.png"), "发送")
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.sp_logger_button_vh_layout.addWidget(self.pushButton_3)

        sp_logger_button_v_layout.addLayout(self.sp_logger_button_vh_layout)

        sp_bg_layout.addWidget(sp_logger_frame)

        # multi send
        sp_multi_send_frame = QWidget()
        sp_multi_send_frame.setFixedWidth(300)
        if show_border:
            sp_multi_send_frame.setObjectName(u"sp_multi_send_frame")
            sp_multi_send_frame.setStyleSheet(f'''
            #sp_multi_send_frame {{
                border-radius: 8px;
                border: 1px solid #ff00ff;
            }}
            ''')

        sp_multi_send_layout = QVBoxLayout(sp_multi_send_frame)
        sp_multi_send_layout.setContentsMargins(0, 0, 0, 0)

        # qml_widget = qmlwidget(sp_multi_send_frame)
        # sp_multi_send_layout.addWidget(qml_widget)



        sp_bg_layout.addWidget(sp_multi_send_frame)

        # self.retranslateUi(parent_pages)

        QMetaObject.connectSlotsByName(parent_pages)



class qmlwidget(QQuickWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSource(QUrl("gui/uis/pages/json_quick_send.qml"))

        context = self.rootContext()
        context.setContextProperty("app", parent)  # 将 QMainWindow 传递给 QML
        self.rootObject().statusChanged.connect(updateApp)


def updateApp():
        print("Update App Triggered")