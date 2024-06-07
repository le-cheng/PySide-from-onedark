
from PySide6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QApplication, QWidget)
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QIntValidator, QPainter, QPainterPath, QPen, QColor
from PySide6.QtCore import Qt, QRectF, QRect

class LabelQLineEditRoundedRectFrame(QFrame):
    def __init__(self, text, w, h, parent=None):
        super().__init__(parent)
        # self.setAutoFillBackground(True)
        self.setFixedSize(w, h)
        # self.setObjectName("LQERRF")
        # self.setStyleSheet(f'''
        #                    QFrame#LQERRF {{
        #                     border-radius: 10px;
        #                     border: 2px solid #d0d6db;
        #                     background-color: white;
        #                    }}
        #     ''')

        self.borderRadius = 10
        self.borderColor = QColor('#d0d6db')
        self.backgroundColor = QColor('#e9ecef')
        self.borderWidth = 2

        self.mid_width = self.width()*0.3

        self.createComponents(text)
        self.layoutComponents()

    def createComponents(self, text):
        self.label = QLabel(text)
        self.label.setStyleSheet("color: black;")

        self.line_edit = QLineEdit()
        self.line_edit.setValidator(QIntValidator(0, 9999))  # 限制为数字输入
        self.line_edit.setStyleSheet("border: None; background-color: white;")

    def layoutComponents(self):
        content_layout = QHBoxLayout(self)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        f1 = QFrame()
        # f1.setObjectName("left_LQERRF")
        # f1.setStyleSheet(f"""
        #                  QFrame#left_LQERRF{{
        #                     border: 1px solid #d0d6db;
        #                     background-color: #e9ecef;
        #                  }}
        #                  """)
        f1_layout = QHBoxLayout(f1)
        f1_layout.addWidget(self.label)

        f2 = QFrame()
        # f2.setObjectName("right_LQERRF")
        # f2.setStyleSheet(f"""
        #                  border: 1px solid #d0d6db;
        #                  background-color: white;
        #                  """)
        f2_layout = QHBoxLayout(f2)
        f2_layout.addWidget(self.line_edit)

        content_layout.addWidget(f1)
        content_layout.addWidget(f2)

        self.mid_width = f1_layout.sizeHint().width()

        # main_layout.addLayout(content_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()

        # 1.
        # 创建带圆角的 QPainterPath
        path = QPainterPath()
        path.addRoundedRect(rect, self.borderRadius, self.borderRadius)
        painter.setClipPath(path)

        # 设置画笔和刷子
        # painter.setPen(QPen(QColor(self.borderColor), self.borderWidth)) # self.borderWidth
        painter.setBrush(QColor(Qt.white))

        # 绘制路径
        painter.drawPath(path)

        # 2.
        rounded_rect = QRect(rect.x(), rect.y() + self.borderWidth/2, self.mid_width, rect.height())
        # Draw the frame
        painter.setBrush(QBrush(self.backgroundColor))
        painter.setPen(QPen(QColor(self.borderColor), self.borderWidth))
        # painter.drawRoundedRect(rounded_rect, self.borderRadius, self.borderRadius)
        painter.drawRect(rounded_rect)

        #3
        painter.setPen(QPen(QColor(self.borderColor), self.borderWidth*2))
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.drawRoundedRect(rect, self.borderRadius, self.borderRadius)


if __name__ == "__main__":
    app = QApplication([])

    win = QWidget()
    win.setGeometry(400, 200, 400, 300)

    layout = QVBoxLayout(win)

    frame = LabelQLineEditRoundedRectFrame("Labeldada:", 160, 40)
    # frame.resize(300, 100)
    layout.addWidget(frame)

    frame2 = LabelQLineEditRoundedRectFrame("Label2:", 160, 40)
    # frame.resize(300, 100)
    layout.addWidget(frame2)

    win.show()

    app.exec()
