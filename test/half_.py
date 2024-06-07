from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtCore import Qt
import sys

class HalfRoundedRectWidget(QWidget):
    def __init__(self, x, y, w, h, r):
        super().__init__()
        self.x_ = x
        self.y_ = y
        self.w_ = w
        self.h_ = h
        self.r_ = r

    def paintEvent(self, event):
        painter = QPainter(self)
        path = QPainterPath()
        path.moveTo(self.x_, self.y_)
        path.lineTo(self.x_ +  self.w_, self.y_)
        path.arcTo(self.x_ +  self.w_ - self.r_*2, self.y_, self.r_*2, self.r_*2, 90, -90)
        path.lineTo(self.x_ +  self.w_+self.r_, self.y_ + self.h_)
        # path.cubicTo(150, 150, 200, 200, 50, 200)
        path.closeSubpath()

        pen = QPen(QColor(Qt.blue))
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawPath(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HalfRoundedRectWidget(100, 100, 100, 100, 10)
    widget.resize(300, 250)
    widget.show()
    sys.exit(app.exec())