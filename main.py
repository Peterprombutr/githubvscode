from program8 import *

def main():
    app = QApplication(sys.argv)

    w= Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
