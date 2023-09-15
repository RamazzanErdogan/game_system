import pygame as pg 
import sys
import random
pg.init()
def zeminyerlestir():
    ekran.blit(zemin,(zemin_x_pozisyonu,450))
    ekran.blit(zemin,(zemin_x_pozisyonu+288,450)) 
def ucagı_dusur(ucak):
    yeni_ucak=pg.transform.rotozoom(ucak,-ucak_haraketi*5,1)  
    return yeni_ucak
def ucak_animasyonu():
    yeni_ucak_sekli=ucak_listesi[ucak_numarası] 
    return yeni_ucak_sekli
def boruları_olustur():
    rastgele_boru_poz=random.choice(boru_yüksekligi)
    alt_boru=boru_yüzeyi.get_rect(midtop=(350,rastgele_boru_poz)) 
    ust_boru=boru_yüzeyi.get_rect(midbottom=(350,rastgele_boru_poz-150))
    return alt_boru,ust_boru
def boruları_yerlestir(borular):
    for boru in borular:
        if boru.bottom>=512: 
            ekran.blit(boru_yüzeyi,boru)
        else:
            boru_döndür=pg.transform.flip(boru_yüzeyi,False,True) 
            ekran.blit(boru_döndür,boru)
def boruları_haraketettir(borular):
    for boru in borular:
        if skor<60:
            boru.centerx-=3
        if skor>=60 and skor<125:
            boru.centerx-=4
        if skor>=125:
            boru.centerx-=5
    return borular
def carpimsa_kontrolu(borular):
    global skor, son_gecilen_boru_indeksi
    for boru in borular:
        if ucak_dortgeni.colliderect(boru) or ucak_dortgeni.top < -50 or ucak_dortgeni.bottom > 450:
            carpma.play()
            return False
    return True
skor = 0
son_gecilen_boru_indeksi = -1
def skor_hesaplama(borular):
    global skor,son_gecilen_boru_indeksi
    for i in range(son_gecilen_boru_indeksi,len(borular)):
        if i-1 > son_gecilen_boru_indeksi:
                gecis.play()
                skor=skor+5
                son_gecilen_boru_indeksi=i
                puansesi.play()
def skor_ekranı():
    toplam_skor=yazı_fontu.render(f"SKOR ={str(skor)}",True,(255,90,90))
    toplam_skor_dortgeni=toplam_skor.get_rect(center=(44,30))
    ekran.blit(toplam_skor,toplam_skor_dortgeni)
yazı_fontu=pg.font.Font(None,20)
def skor_ekranı_son():
    toplam_skor=yazı_fontu2.render(f"SKOR ={str(skor)}",True,(55,10,10))
    toplam_skor_dortgeni=toplam_skor.get_rect(center=(140,210))
    ekran.blit(toplam_skor,toplam_skor_dortgeni)
yazı_fontu2=pg.font.Font(None,50) 
zemin_x_pozisyonu=0
ekran=pg.display.set_mode((288,512))
zaman=pg.time.Clock()
pg.display.set_caption("UÇAK")
ikon=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler/3.oyun\Uçak_düz.png") 
pg.display.set_icon(ikon)
arkaplan=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\arkaplan.png")
zemin=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\yer.png")
ucak=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\Uçak_düz.png")
ucak_yan=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\Uçak_ileri.png")
ucak_ters=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\Uçak_bozulmuş.png")
ucak_numarası=  0
ucak_listesi=[ucak,ucak_yan,ucak_ters]
ucak_yuzeyi=ucak_listesi[ucak_numarası]
ucak_dortgeni=ucak_yuzeyi.get_rect(center=(50,256))
UCAK_ANİMASYONU=pg.USEREVENT + 0
pg.time.set_timer(UCAK_ANİMASYONU,350) 
yer_cekimi=0.125
ucak_haraketi=0
boru_yüzeyi=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\kırmızı_boru.png")
boru_listesi=[] 
BORU_ÜRET=pg.USEREVENT + 1
pg.time.set_timer(BORU_ÜRET,1500)
boru_yüksekligi=[200,250,300,350,400]
baslangıc_ekranı=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\başlangıç.png")
baslangıc_ekranı_dortgeni=baslangıc_ekranı.get_rect(center=(144,256))
zıplama=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\uçma.ogg")
carpma=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\çarpma.wav")
gecis=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\geçme.ogg")
puansesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\3.oyun\artıbir.ogg")
oyun_aktifligi=False
skor=0
while True:
    for olay in pg.event.get():
        if olay.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if olay.type==pg.KEYDOWN:
            if olay.key==pg.K_SPACE and oyun_aktifligi==True:
                ucak_haraketi=0
                ucak_haraketi=-3.125
                zıplama.play()
            if olay.key==pg.K_SPACE and oyun_aktifligi==False:
                oyun_aktifligi=True
                boru_listesi.clear()
                skor=0
                son_gecilen_boru_indeksi=0
                ucak_dortgeni.center=(50,256)
                ucak_haraketi=0
        if olay.type==UCAK_ANİMASYONU:
            if ucak_numarası<2:
                ucak_numarası+=1
            else:
                ucak_numarası=0
            ucak_yuzeyi= ucak_animasyonu() 
        if olay.type==BORU_ÜRET and oyun_aktifligi==True:                
            boru_listesi.extend(boruları_olustur())                     
    ekran.blit(arkaplan,(0,0))
    zemin_x_pozisyonu-=3
    zeminyerlestir()
    if zemin_x_pozisyonu <=-288:
        zemin_x_pozisyonu=0
    if oyun_aktifligi:
        oyun_aktifligi=carpimsa_kontrolu(boru_listesi)
        boruları_yerlestir((boru_listesi))
        boruları_haraketettir(boru_listesi)
        ucak_haraketi+=yer_cekimi 
        dusen_ucak=ucagı_dusur(ucak_yuzeyi)
        ucak_dortgeni.centery+=ucak_haraketi 
        ekran.blit(dusen_ucak ,(ucak_dortgeni))
    else:
        oyun_aktifligi=False
        ekran.blit(baslangıc_ekranı,baslangıc_ekranı_dortgeni)
        skor_ekranı_son()
    skor_hesaplama(boru_listesi)  
    skor_ekranı()
    pg.display.update()
    zaman.tick(60)     