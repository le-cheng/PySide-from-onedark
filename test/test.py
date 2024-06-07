from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
import sys

class TabWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()

        tab1 = QWidget()
        tab2 = QWidget()

        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        self.setCentralWidget(tab_widget)

        self.setWindowTitle("TabWidget Demo")

        # 设置样式表
        tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid black;
            }

            QTabBar::tab {
                background: lightgray;
                padding: 5px;
            }

            QTabBar::tab:selected {
                background: gray;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TabWidgetDemo()
    demo.show()
    sys.exit(app.exec())