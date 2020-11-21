import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Git1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 450)
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.gen)
        self.qp = QPainter()
        self.flag = False        


    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            sz = [randint(-10 + i - i, 120) for i in range(0, 2)]
            coords = (tuple([randint(i - i, 400) for i in range(2)]))
            self.qp.setBrush(QColor(255, 204, 0))
            self.qp.drawEllipse(*coords, sz[0], sz[0])
            self.qp.end()

    def gen(self):
        self.flag = True
        self.repaint()
        
def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Git1()
    ex.show()
    sys.exit(app.exec_())
