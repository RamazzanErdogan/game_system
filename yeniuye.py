# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soblon3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class yeniuye_penceresi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 641)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(800, 641))
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 255);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Users/ramaz/Ramazan/Downloads/Ekran görüntüsü 2023-09-07 15465.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 191, 41))
        self.label_3.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Sitka\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 330, 201, 41))
        self.label_4.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Sitka\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 410, 191, 41))
        self.label_5.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Sitka\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 250, 191, 41))
        self.label_6.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Sitka\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 170, 191, 41))
        self.label_7.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Sitka\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.ad_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ad_text.setGeometry(QtCore.QRect(340, 100, 211, 41))
        self.ad_text.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.ad_text.setObjectName("ad_text")
        self.soyad_text = QtWidgets.QLineEdit(self.centralwidget)
        self.soyad_text.setGeometry(QtCore.QRect(340, 170, 211, 41))
        self.soyad_text.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.soyad_text.setObjectName("soyad_text")
        self.eposta_text = QtWidgets.QLineEdit(self.centralwidget)
        self.eposta_text.setGeometry(QtCore.QRect(340, 250, 211, 41))
        self.eposta_text.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.eposta_text.setObjectName("eposta_text")
        self.kullaniciadi_text = QtWidgets.QLineEdit(self.centralwidget)
        self.kullaniciadi_text.setGeometry(QtCore.QRect(340, 330, 211, 41))
        self.kullaniciadi_text.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.kullaniciadi_text.setObjectName("kullaniciadi_text")
        self.parola_text = QtWidgets.QLineEdit(self.centralwidget)
        self.parola_text.setGeometry(QtCore.QRect(340, 410, 211, 41))
        self.parola_text.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.parola_text.setObjectName("parola_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 470, 461, 61))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 250, 211, 41))
        self.comboBox.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 490, 181, 101))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 380, 421, 20))
        self.label.setStyleSheet("background: transparent;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.kayit_mesaji = QtWidgets.QLabel(self.centralwidget)
        self.kayit_mesaji.setGeometry(QtCore.QRect(130, 460, 471, 91))
        self.kayit_mesaji.setToolTipDuration(2)
        self.kayit_mesaji.setStyleSheet("background: transparent;")
        self.kayit_mesaji.setText("")
        self.kayit_mesaji.setObjectName("kayit_mesaji")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.ad_text.raise_()
        self.soyad_text.raise_()
        self.eposta_text.raise_()
        self.kullaniciadi_text.raise_()
        self.parola_text.raise_()
        self.comboBox.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.kayit_mesaji.raise_()
        self.pushButton.raise_()
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
        self.label_3.setText(_translate("MainWindow", "AD:"))
        self.label_4.setText(_translate("MainWindow", "KULLANICI ADI:"))
        self.label_5.setText(_translate("MainWindow", "PAROLA:"))
        self.label_6.setText(_translate("MainWindow", "E-POSTA:"))
        self.label_7.setText(_translate("MainWindow", "SOYAD:"))
        self.pushButton.setText(_translate("MainWindow", "KAYDOL"))
        self.comboBox.setItemText(0, _translate("MainWindow", "@gmail.com"))
        self.comboBox.setItemText(1, _translate("MainWindow", "@icloud.com"))
        self.comboBox.setItemText(2, _translate("MainWindow", "@outlook.com"))
        self.pushButton_2.setText(_translate("MainWindow", "GİRİŞ YAP"))
