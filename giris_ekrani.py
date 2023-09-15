import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from girisekrani_stilsayfasi import Giris_penceresi

class GirisEkrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(GirisEkrani, self).__init__()
        self.ui = Giris_penceresi()
        self.ui.setupUi(self)
        self.animation_timer = QtCore.QTimer(self) 
        self.animation_timer.timeout.connect(self.animate_background) 
        self.animation_frame = 0 
        self.animation_frames = [
            r"C:\Bilgisayar dersleri\python\projeler\oklar0.1.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar1.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar2.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar3.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar4.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar5.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar6.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar7.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar8.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar9.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar10.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar11.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar12.png",
            r"C:\Bilgisayar dersleri\python\projeler\oklar13.png"
        ]
        self.start_animation() 
    def start_animation(self):
        self.animation_timer.start(350)  
    def animate_background(self): 
        self.animation_frame = (self.animation_frame + 1) % len(self.animation_frames) 
        frame_path = self.animation_frames[self.animation_frame]
        pixmap = QPixmap(frame_path) 
        self.ui.animasyon_kutusu.setPixmap(pixmap)
def calistir():
    app = QtWidgets.QApplication(sys.argv)
    win = GirisEkrani()
    win.show()
    sys.exit(app.exec_())
calistir()


