from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect



class CustomMessageBox(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        margins = 10
        self.layout.setContentsMargins(margins, margins, margins, margins)

        self._bg_color = "#00ff00"
        # self._bg_color = QColor("green")
        # self._bg_color = QColor(0, 255, 0)

        self._radius = 10

        self.message_frame = QFrame()
        self.message_frame.setFixedWidth(500)
        self.message_frame.setFixedHeight(60)
        self.message_frame.setObjectName("message_frame")
        self.message_frame.setStyleSheet(f'''
        #message_frame {{
            background-color: {self._bg_color};
            border-radius: {self._radius}px;
            border: 0px solid #ff0000;
        }}
        ''')
        # 设置窗口阴影
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.message_frame.setGraphicsEffect(self.shadow)

        self.layout.addWidget(self.message_frame)



        self.message_frame_layout = QVBoxLayout(self.message_frame)
        self.message_frame_layout.setContentsMargins(0,0,0,0)


#         def show_popup():
#     # 在按钮附近显示浮出控件
#     popup_menu.exec_(button.mapToGlobal(button.rect().bottomLeft()))

# # 按钮点击时显示浮出控件
# button.clicked.connect(show_popup)

        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("title_label")
        self.label.setStyleSheet(f'''
        #title_label {{
            font-size: 16pt;
            color: #0000ff;
            padding-bottom: 3px;
            background: none;
        }}
        ''')
        self.message_frame_layout.addWidget(self.label)

app = QApplication([])

custom_message = CustomMessageBox("这是一条自定义的消息！")
# custom_message.setWindowTitle("自定义消息框")
custom_message.show()

app.exec()