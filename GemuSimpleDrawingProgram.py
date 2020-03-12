import sys

import PySide2
from PySide2.QtCore import *
from PySide2.QtWidgets import  *
from PySide2.QtGui import *

from program8 import Simple_drawing_window

class GemuWindow(Simple_drawing_window):
    def __init__(self):
        super().__init__()
        self.rabbit = QPixmap("Jesus.png")


GemuWindow()
