import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

from PyQt5 import QtCore, QtGui, QtWidgets

#третья задача

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "создать круг"))


class Git1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 450)
        self.setupUi(self)
        self.btn.clicked.connect(self.gen)
        self.qp = QPainter()
        self.flag = False        


    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            sz = [randint(-10 + i - i, 120) for i in range(0, 2)]
            coords = (tuple([randint(i - i, 400) for i in range(2)]))
            self.qp.setBrush(QColor(*tuple([randint(i-i, 255) for i in range(3)])))
            self.qp.drawEllipse(*coords, sz[0], sz[1])
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
