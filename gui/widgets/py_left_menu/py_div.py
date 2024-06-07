
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame


# CUSTOM LEFT MENU
class PyDiv(QWidget):
    def __init__(self, color):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5,0,5,0)
        self.frame_line = QFrame()
        self.frame_line.setStyleSheet(f"background: {color};")
        self.frame_line.setMaximumHeight(2)
        self.frame_line.setMinimumHeight(2)
        self.layout.addWidget(self.frame_line)
        self.setMaximumHeight(2)
