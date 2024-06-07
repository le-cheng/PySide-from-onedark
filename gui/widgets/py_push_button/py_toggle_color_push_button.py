from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QSize, Qt, Slot
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtGui import QIcon, QPainter, QColor, QFont

class ToggleColorButton(QPushButton):
    def __init__(self, icon, text):
        super().__init__()
        self.setCheckable(True)
        self.setText(text)
        self.setIcon(icon)
        # self.resize(200, 100)
        self.setMinimumHeight(40)
        self.setFixedSize(QSize(220, 60))

        self.color_bg_is_down = QColor(200, 200, 200)
        self.color_bg_under_mouse = QColor(173, 216, 230)
        self.color_bg_is_up = QColor(13, 110, 253)

        self.rect_radius = 20

        self.color_text_isdown = QColor(13, 110, 253)
        self.color_text_under_mouse = QColor(13, 110, 253)
        self.color_text_other = QColor(255, 255, 255)

        self.is_pressed = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = not self.is_pressed
            print("mousePressEvent", self.is_pressed)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("mouseReleaseEvent")
        super().mouseReleaseEvent(event)

    def enterEvent(self, event):
        print("enterEvent")
        super().enterEvent(event)

    def leaveEvent(self, event):
        print("leaveEvent")
        super().leaveEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = event.rect()
        bg_color = self.color_bg_is_up
        text_color = self.color_text_other

        # 背景颜色
        if self.isChecked():
            bg_color = self.color_bg_is_down
            text_color = self.color_text_isdown
        else:
            bg_color = self.color_bg_is_up
            text_color = self.color_text_other

        if self.isDown():
            bg_color.setAlpha(150)
        elif self.underMouse():
            bg_color.setAlpha(200)
        else:
            bg_color.setAlpha(255)
        painter.setBrush(bg_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, self.rect_radius, self.rect_radius)

        # 文本颜色
        painter.setPen(text_color)
        painter.setFont(QFont("Arial", 16))
        painter.drawText(rect, Qt.AlignCenter, self.text())

# 正常状态——表示按钮是可交互的，并且可用的。
# 聚焦状态——通过高亮的形式告诉用户，它已经被键盘或者其他的方式所选中
# 悬停状态——当用户使用光标或者其他的元素，置于其上方的时候，显示这样的状态
# 激活状态——表示用户已经按下按钮（且还未结束按按钮的动作）
# 加载状态——表示操作正在加载中，组件正在反映，但是操作还未完成
# 禁用状态——表示当前组件处于非交互状态，但是之后可以被启用