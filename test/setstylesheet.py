from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

app = QApplication([])

widget = QWidget()
main_layout = QVBoxLayout(widget)

label = QLabel("Enter your name:")
label.setStyleSheet("color: darkgreen; font: bold 14px;")

line_edit = QLineEdit()
line_edit.setStyleSheet("""
    QLineEdit {
        border: 2px solid gray;
        border-radius: 4px;
        padding: 5px;
        background-color: white;
    }
    QLineEdit:focus {
        border-color: blue;
    }
""")

button = QPushButton("Submit")
button.setStyleSheet("""
    QPushButton {
        background-color: lightgray;
        border: 1px solid gray;
        border-radius: 4px;
        padding: 5px 15px;
    }
    QPushButton:hover {
        background-color: lightblue;
    }
    QPushButton:pressed {
        background-color: darkblue;
        color: white;
    }
""")

main_layout.addWidget(label)
main_layout.addWidget(line_edit)
main_layout.addWidget(button)

widget.setLayout(main_layout)
widget.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        padding: 20px;
        border: 1px solid gray;
        border-radius: 10px;
    }
""")

widget.resize(300, 200)
widget.show()

app.exec()