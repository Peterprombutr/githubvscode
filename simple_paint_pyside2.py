import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import  *
from PySide2.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.setWindowTitle("A Simple paint program")
        self.vb = QVBoxLayout()
        self.canvas = QPixmap(400,300)
        self.label.setPixmap(self.canvas)
        self.ass = QLabel("Drag to draw a line")
        self.vb.addWidget(self.label)
        self.clearButton = QPushButton("Clear")
        self.vb.addWidget(self.ass)
        self.vb.addWidget(self.clearButton)
        self.clearButton.clicked.connect(self.clearCanvas)
        self.setLayout(self.vb)
        self.last_x, self.last_y = None, None

    def clearCanvas(self):
        for i in reversed(range(self.vb.count())): 
            self.vb.itemAt(i).widget().setParent(None)
        self.canvas = QPixmap(400,300)
        self.label.setPixmap(self.canvas)
        self.vb.addWidget(self.label)
        self.vb.addWidget(self.ass)
        self.vb.addWidget(self.clearButton)
    
    def mouseMoveEvent(self, event):
        if self.last_x is None:
            self.last_x = event.x()
            self.last_y = event.y()
            return
        
        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.last_x, self.last_y, event.x(), event.y())
        painter.end()
        self.update()

        self.last_x = event.x()
        self.last_y = event.y()
    
    def mouseReleaseEvent(self, event):
        self.last_x = None
        self.last_y = None

def main():
    app = QApplication(sys.argv)

    w= MainWindow()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
