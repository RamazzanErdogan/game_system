import sys
import typing
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from oyunekrani_stilsayfası import Oyun_penceresi

class oyunekrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(oyunekrani,self).__init__()
        self.ui=Oyun_penceresi()
        self.ui.setupUi(self)
def calistir():
    app = QtWidgets.QApplication(sys.argv)
    win=oyunekrani()
    win.show()
    sys.exit(app.exec_())

calistir()
