import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QWidget
from girisekrani_stilsayfasi import Giris_penceresi
from oyunekrani_stilsayfası import Oyun_penceresi
from mydb_kullanıcıbilgileri import get_kullanıcıadı,get_parola
from yeniuye import yeniuye_penceresi
import time
class GirisEkrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(GirisEkrani, self).__init__()
        self.ui = Giris_penceresi()
        self.ui.setupUi(self)
        self.setWindowTitle("Oyun İşletim Sistemi")
        ikon=QIcon("C:\Bilgisayar dersleri\python\projeler\ikon.png")
        self.setWindowIcon(ikon) 
        self.ui.giris_butonu.clicked.connect(self.oyun_ekrani_ac)
        self.ui.uye_ol_button.clicked.connect(self.uyeol_ekrani_ac)
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
    def oyun_ekrani_ac(self): 
        girilen_kullanıcıadı=self.ui.kullanici_adi_text.text()
        girilen_parola=self.ui.parola_text.text()
        kullanıcıadı=get_kullanıcıadı()
        kullanıcıadı_sayısı=len(kullanıcıadı)
        parola=get_parola()
        for i in range(kullanıcıadı_sayısı):
            if (kullanıcıadı[i][0])==girilen_kullanıcıadı and (parola[i][0])==girilen_parola:
                self.oyun_ekran=oyunekrani()
                self.oyun_ekran.show()
                self.close()
    def uyeol_ekrani_ac(self):
        self.close()
        self.yeniüyeekrani=yeniuye_ekrani()
        self.yeniüyeekrani.show()
class yeniuye_ekrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(yeniuye_ekrani,self).__init__()
        self.ui=yeniuye_penceresi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.databasekayit)
        self.ui.pushButton_2.clicked.connect(self.girisekrani)
    def databasekayit(self):
            kullanıcıadı=get_kullanıcıadı()
            kullanıcıadı_sayısı=len(kullanıcıadı)
            import mysql.connector
            mydb=mysql.connector.connect(
            user="root",
            password="mysql123",
            host="localhost",
            database="kullanıcı_bilgileri"
            )
            mydb_update = mydb.cursor()
            for i in range(kullanıcıadı_sayısı):
                    if self.ui.kullaniciadi_text.text()==(kullanıcıadı[i][0]):
                        self.ui.label.setText("!!!!!BU KULLANICI ADINI ZATEN BAŞKASI KULLANIYOR !!!!")
                        self.ui.label.setStyleSheet("background:  rgb(255, 255, 0);")
                        break
                    else:
                        if self.ui.kullaniciadi_text.text() != "" and self.ui.kullaniciadi_text.text() !=kullanıcıadı[i][0]:
                            mydb = mysql.connector.connect(
                            user="root",
                            password="mysql123",
                            host="localhost",
                            database="kullanıcı_bilgileri"
                            )
                            mydb_update = mydb.cursor()
                            update_query = "INSERT INTO kullanıcılar (`kullanıcıadı`, `parola`, `AD`, `Soyad`, `e-posta`) VALUES (%s, %s, %s, %s, %s)"
                            update_values = (self.ui.kullaniciadi_text.text(), self.ui.parola_text.text(), self.ui.ad_text.text(), self.ui.soyad_text.text(),self.ui.eposta_text.text()+self.ui.comboBox.currentText())
                            mydb_update.execute(update_query, update_values)
                            self.ui.parola_text.clear()
                            self.ui.kullaniciadi_text.clear()
                            self.ui.eposta_text.clear()
                            self.ui.ad_text.clear()
                            self.ui.soyad_text.clear()
                            self.ui.kayit_mesaji.setText("KAYIT BAŞARI İLE TAMAMLANMIŞTIR \n GİRİŞ YAP BUTONUNA TIKLAYARAK SİSTEME GİRİŞ YAPABİLİRSİNİZ.")
                            self.ui.kayit_mesaji.setStyleSheet("background: rgb(255, 255, 0);")
                            self.ui.kayit_mesaji.raise_()
                            mydb.commit()
                            mydb.close()
    def girisekrani(self):
        get_kullanıcıadı()
        self.close()
        self.girisekrani_ac=GirisEkrani()
        self.girisekrani_ac.show()              
class oyunekrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(oyunekrani,self).__init__()
        self.ui=Oyun_penceresi()
        self.ui.setupUi(self)
        self.setWindowTitle("OYUNLAR")
        ikon2=QIcon("C:\Bilgisayar dersleri\python\projeler\ikon2.png")
        self.setWindowIcon(ikon2) 
        self.ui.pushButton_5.clicked.connect(self.oyun1_ac)
        self.ui.pushButton_6.clicked.connect(self.oyun2_ac)
        self.ui.pushButton_7.clicked.connect(self.oyun3_ac)
        self.ui.pushButton_4.clicked.connect(self.geridon)
    def oyun1_ac(self):
        import oyun1
        self.close()
    def oyun2_ac(self):
        import oyun2
    def oyun3_ac(self):
        import oyun3  
    def geridon(self):
        self.close()
        self.girisekrani_ac=GirisEkrani()
        self.girisekrani_ac.show()  
def calistir():
    app = QtWidgets.QApplication(sys.argv)
    win = GirisEkrani()
    win.show()
    sys.exit(app.exec_())

calistir()