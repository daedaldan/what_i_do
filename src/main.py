from src.ui import Window
from PyQt5.QtWidgets import *
import sys

# stylesheet for UI
stylesheet = """
QWidget {
    background: white;
}    

QLineEdit {
    outline: 0;
    border: 0px solid transparent;
    border-bottom: 1px solid gray;
    font-family: Avenir;
    font-size: 84px;
}

QPushButton {
    border-radius: 25%;
    font-family: Avenir;
    font-size: 84px;
}

QLabel {
    font-family: Avenir;
    font-size: 84px;
}
"""

# start UI
app = QApplication([])
app.setStyleSheet(stylesheet)
ui = Window("What I Do Everyday")
ui.show()

sys.exit(app.exec_())

