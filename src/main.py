from src.ui import Window
from PyQt5.QtWidgets import *
import sys


# start GUI
app = QApplication([])
ui = Window()
ui.show()

sys.exit(app.exec_())

