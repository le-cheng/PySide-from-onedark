import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QSize, QRectF
from PySide6.QtGui import QPainter, QColor, QFont, QLinearGradient
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPainterPath


class CustomButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        print("enter event")
        self.setStyleSheet("background-color: lightblue")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("")
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.setStyleSheet("background-color: gray")
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setStyleSheet("background-color: lightblue")
        self.animateButton2()
        super().mouseReleaseEvent(event)

    def animateButton(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        start_rect = QRect(self.geometry())
        enlarged_rect = start_rect.adjusted(-10, -10, 10, 10)
        self.animation.setStartValue(enlarged_rect)
        self.animation.setEndValue(start_rect)
        self.animation.start()

    def animateButton1(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.OutBounce) # 这行到终点会弹一下

        start_rect = QRect(self.geometry())
        enlarged_rect = start_rect.translated(100, 100)

        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(enlarged_rect)
        self.animation.start()

    def animateButton2(self):
        opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(opacity_effect)
        self.animation = QPropertyAnimation(opacity_effect, b"opacity")

        self.animation.setDuration(2000)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.isDown():
            painter.setBrush(QColor(200, 200, 200))
        elif self.underMouse():
            painter.setBrush(QColor(173, 216, 230))
        else:
            painter.setBrush(QColor(240, 240, 240))

        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        painter.setPen(QColor(0, 122, 204))
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())


class BasicButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 背景颜色
        painter.setBrush(QColor(200, 200, 200))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        # 文本颜色
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class GradientButton(QPushButton):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(255, 255, 255))
        gradient.setColorAt(1, QColor(100, 100, 255))

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class ShadowButton(QPushButton):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(230, 230, 230))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        # 绘制阴影
        shadow_color = QColor(0, 0, 0, 50)  # 半透明黑色
        shadow_offset = 2
        painter.setPen(shadow_color)
        painter.setFont(QFont("Arial", 16))
        rect_with_offset = self.rect().adjusted(shadow_offset, shadow_offset, shadow_offset, shadow_offset)
        painter.drawText(rect_with_offset, Qt.AlignCenter, self.text())

        # 绘制文本
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class TransparentButton(QPushButton):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置透明度
        painter.setOpacity(0.3)  # 半透明
        painter.setBrush(QColor(200, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        painter.setOpacity(1)  # 恢复不透明
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class ToggleColorButtonTemp(QPushButton):
    def __init__(self, icon, text):
        super().__init__()
        self.setCheckable(True)
        self.setText(text)
        self.setIcon(icon)
        # self.resize(200, 100)
        self.setMinimumHeight(40)
        self.setFixedSize(QSize(220, 60))

        self.color_bg_isdown = QColor(200, 200, 200)
        self.color_bg_under_mouse = QColor(173, 216, 230)
        self.color_bg_other = QColor(13, 110, 253)

        self.rect_radius = 20

        self.color_text_isdown = QColor(13, 110, 253)
        self.color_text_under_mouse = QColor(13, 110, 253)
        self.color_text_other = QColor(255, 255, 255)

    #     self.pressed.connect(self.btn_pressed)
    #     if self.isCheckable():
    #         self.toggled.connect(self.btn_toggled)
    #     self.released.connect(self.btn_released)
    #     self.clicked.connect(self.btn_clicked)

    # @Slot()
    # def btn_pressed(self):
    #     print("btn_pressed")

    # @Slot()
    # def btn_toggled(self):
    #     if self.isChecked():
    #         print("btn_toggled -- checked")
    #     else:
    #         print("btn_toggled -- unchecked")

    # @Slot()
    # def btn_released(self):
    #     print("btn_released")

    # @Slot()
    # def btn_clicked(self):
    #     print("btn_clicked\n")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = event.rect()


        # 背景颜色
        if self.isDown():
            painter.setBrush(self.color_bg_isdown)
        elif self.underMouse():
            painter.setBrush(self.color_bg_under_mouse)
        else:
            painter.setBrush(self.color_bg_other)

        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, self.rect_radius, self.rect_radius)

        # 文本颜色
        if self.isDown():
            painter.setPen(self.color_text_isdown)
        elif self.underMouse():
            painter.setPen(self.color_text_under_mouse)
        else:
            painter.setPen(self.color_text_other)
        painter.setFont(QFont("Arial", 16))
        painter.drawText(rect, Qt.AlignCenter, self.text())

        # 调用基类的 paintEvent 方法，确保其他默认绘制行为仍然存在
        # super().paintEvent(event)


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


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CustomButton Example')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout(self)

        if 0:
            self.label = QLabel('Custom button demo', self)
            layout.addWidget(self.label)


            self.basicbutton = BasicButton("basicbutton", self)
            layout.addWidget(self.basicbutton)

            self.gradientbutton = GradientButton("gradientbutton", self)
            layout.addWidget(self.gradientbutton)

            self.ShadowButton = ShadowButton("ShadowButton", self)
            layout.addWidget(self.ShadowButton)

            self.TransparentButton = TransparentButton("TransparentButton", self)
            layout.addWidget(self.TransparentButton)

        if 0:
            self.custom_button = CustomButton('Custom Button', self)
            self.custom_button.clicked.connect(self.on_custom_button_clicked)
            layout.addWidget(self.custom_button)

        btn = ToggleColorButton(QIcon("source/example.png"), "click me")

        layout.addWidget(btn)



        self.setLayout(layout)

    def on_custom_button_clicked(self):
        print('Custom button clicked!')
        # self.label.setText('Custom button clicked!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())