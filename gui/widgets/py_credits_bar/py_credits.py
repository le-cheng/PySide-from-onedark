



# IMPORT QT CORE

# from qt_core import *
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy


# PY CREDITS BAR AND VERSION
class PyCredits(QWidget):
    def __init__(
        self,
        copyright,
        version,
        bg_two,
        font_family,
        text_size,
        text_description_color,
        radius = 8,
        padding = 10
    ):
        super().__init__()

        # PROPERTIES
        self._copyright = copyright
        self._version = version
        self._bg_two = bg_two
        self._font_family = font_family
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        # ADD LAYOUT
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)

        # BG STYLE
        style = f"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._bg_two};
        }}
        .QLabel {{
            font: {self._text_size}pt "{self._font_family}";
            color: {self._text_description_color};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        # BG FRAME
        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        # ADD TO LAYOUT
        self.widget_layout.addWidget(self.bg_frame)

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0,0,0,0) # 小部件内容的边距

        # ADD COPYRIGHT TEXT
        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignVCenter)
        # 对齐方式是对齐方式的标志，可以是以下值之一：
        # Qt.AlignLeft：左对齐
        # Qt.AlignRight：右对齐
        # Qt.AlignHCenter：水平居中
        # Qt.AlignJustify：两端对齐
        # Qt.AlignTop：顶部对齐
        # Qt.AlignBottom：底部对齐
        # Qt.AlignVCenter：垂直居中

        # ADD VERSION TEXT
        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignVCenter)

        # # SEPARATOR 使用PySide6创建了一个水平分隔符，并将它添加到一个布局中。
        # self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # # ADD TO LAYOUT
        # self.bg_layout.addWidget(self.copyright_label)
        # self.bg_layout.addSpacerItem(self.separator)
        # self.bg_layout.addWidget(self.version_label)

        # CREATE HORIZONTAL LAYOUT FOR LABELS
        label_layout = QHBoxLayout()
        label_layout.addWidget(self.copyright_label)
        label_layout.addWidget(self.version_label)
        label_layout.setAlignment(Qt.AlignRight)

        # ADD LABEL LAYOUT TO BG LAYOUT
        self.bg_layout.addLayout(label_layout)
