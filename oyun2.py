from typing import Any
import pygame as pg
import sys,random
import time
pg.init()
ekran=pg.display.set_mode((1370,720))
zaman=pg.time.Clock()
arkaplan_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\arkaplan_müzik.mp3")
arkaplan_music.play()
yesil_isin_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\ışın_yeşil.mp3")
meteor_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\meteor.mp3")
kırmızı_lazer_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\kırmızı_lazer.mp3")
uclu_lazer_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\üçlü_lazer.mp3")
arkaplan=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun/arkaplan.png")
oyunbaslangıc_arkaplan=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\oyunbaslangıcarkaplan_bosluk.jpg")
oyunbaslangıc_uzaygemisi=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\oyunbaslangıcarkaplan.png")
play_yazısı=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\play.png")
imlec=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\imlec.png")
imlec_dörtgeni=imlec.get_rect(center=(683,360))
fare_x_pozisyonu=[(640,300),(630,290)]
class Uzaygemileri(pg.sprite.Sprite): 
    def __init__(self,görselin_yolu,x_koordinati,y_koordinati):
        super().__init__()
        
        self.image=pg.image.load(görselin_yolu)
        self.can_sayısı=3
        self.can=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun\can.png")
        self.hasarlı=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun/araç_hasarlı.png")
    def update(self):
        self.rect.center=pg.mouse.get_pos()
        pg.mouse.set_visible(False)
        self.sınırlandırma()
        self.can_göstergesi()
        self.hasarlı_arac()
        self.manevra()
    def sınırlandırma(self):
        if self.rect.right >= 1370:
            self.rect.right=1370
        elif self.rect.left <= 0:
            self.rect.left=0
        elif self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom >=720:
            self.rect.bottom=720
    def can_göstergesi(self):
        for index in range(self.can_sayısı):
            ekran.blit(self.can,(1370-50*(index+1),15))
    def hasar(self,hasar):
        self.can_sayısı-=hasar
    def hasarlı_arac(self):
        if self.can_sayısı <2:
            self.image=self.hasarlı
        else:
            self.image=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun/araç_düz.png")
            self.image=self.image
    def manevra(self):
        
        a=pg.mouse.get_pos()
        fare_x_pozisyonu.append(a)
        if len(fare_x_pozisyonu)==3:
            fare_x_pozisyonu.pop(0)
        if fare_x_pozisyonu[1][0] >fare_x_pozisyonu[0][0]:
            self.sağa=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun/araç_sağ.png")
            self.image=self.sağa
        if fare_x_pozisyonu[1][0] <fare_x_pozisyonu[0][0]:
            self.sola=pg.image.load("C:\Bilgisayar dersleri\python\projeler/2.oyun/araç_sol.png")
            self.image=self.sola
uzaygemisi=Uzaygemileri("C:\Bilgisayar dersleri\python\projeler/2.oyun/araç_düz.png",690,500)
Uzaygemileri_grubu=pg.sprite.GroupSingle()
Uzaygemileri_grubu.add(uzaygemisi)
class Meteorlar(pg.sprite.Sprite):
    def __init__(self,görselin_yolu,x_koordinati,y_koordinati,x_hizi, y_hizi):
        super().__init__()
        self.image=pg.image.load(görselin_yolu)
        self.rect=self.image.get_rect(center=(x_koordinati,y_koordinati))
        self.x_hizi=x_hizi
        self.y_hizi=y_hizi
    def update(self):
        self.rect.centerx+=self.x_hizi
        self.rect.centery+=self.y_hizi
        if self.rect.centery >=800:
            self.kill()
meteor_grubu=pg.sprite.Group()

METEOR_OLAYI1=pg.USEREVENT+1
pg.time.set_timer(METEOR_OLAYI1,500)
class canlar(pg.sprite.Sprite):
    def __init__(self,canyol,canx,cany,canyhizi):
        super().__init__()
        self.image=pg.image.load(canyol)
        self.rect=self.image.get_rect(center=(canx,cany))
        self.canyhizi=canyhizi
    def update(self):
        self.rect.centery+=self.canyhizi
        if self.rect.centery>=800:
            self.kill()
can_grubu=pg.sprite.Group()
CANOLAYI=pg.USEREVENT+2
pg.time.set_timer(CANOLAYI,10000)
class Lazer(pg.sprite.Sprite):
    def __init__(self,yol,pozisyon,hız):
        super().__init__()
        self.image=pg.image.load(yol)
        self.rect=self.image.get_rect(center=(pozisyon))
        self.hız=hız
    def update(self):
        self.rect.centery=self.rect.centery-self.hız
        if self.rect.centery <= 0:
            self.kill()

class Lazer2(pg.sprite.Sprite):
    def __init__(self,yol,pozisyon,hız):
        super().__init__()
        self.image=pg.image.load(yol)
        self.rect=self.image.get_rect(center=(pozisyon))
        self.hız=hız
    def update(self):
        self.rect.centery=self.rect.centery-self.hız
        if self.rect.centery <= -1:
            self.kill()
class Lazer_sola(pg.sprite.Sprite):
    def __init__(self,yol,pozisyon,hız):
        super().__init__()
        self.image=pg.image.load(yol)
        self.rect=self.image.get_rect(center=(pozisyon))
        self.hız=hız
        self.hız2=hız/2
    def update(self):
        self.rect.centery=self.rect.centery-self.hız
        self.rect.centerx=self.rect.centerx+self.hız2
        if self.rect.centery <= -100:
            self.kill()
class Lazer_saga(pg.sprite.Sprite):
    def __init__(self,yol,pozisyon,hız):
        super().__init__()
        self.image=pg.image.load(yol)
        self.rect=self.image.get_rect(center=(pozisyon))
        self.hız=hız
        self.hız2=hız/2
    def update(self):
        self.rect.centery=self.rect.centery-self.hız
        self.rect.centerx=self.rect.centerx-self.hız2
        if self.rect.centery <= -100:
            self.kill()
lazer_grubu=pg.sprite.Group()
lazer_grubu_yeşil=pg.sprite.Group()
def anaoyun():
    Uzaygemileri_grubu.update()
    Uzaygemileri_grubu.draw(ekran)
    meteor_grubu.draw(ekran)
    meteor_grubu.update()
    can_grubu.draw(ekran)
    can_grubu.update()
    lazer_grubu.update()
    lazer_grubu.draw(ekran)
    lazer_grubu_yeşil.update()
    lazer_grubu_yeşil.draw(ekran)
def oyunbitti():
    global skor
    global imlec_dörtgeni
    global true_false
    ekran.blit(oyunbaslangıc_arkaplan,(0,0))
    if olay.type==pg.MOUSEMOTION:
        imlec_dörtgeni=imlec.get_rect(center=olay.pos)
    ekran.blit(oyunbaslangıc_uzaygemisi,(-400,0))
    ekran.blit(play_yazısı,(700,490))
    skor_=yazı_fontu.render(f"SCORE:{skor}",True,(255,10,100))
    skor_dörtgeni=skor_.get_rect(center=(1000,350))
    ekran.blit(skor_,skor_dörtgeni)
    ekran.blit(imlec,imlec_dörtgeni)
    if play_yazısı.get_rect(topleft=(700,490)).colliderect((imlec_dörtgeni)):
        if olay.type==pg.MOUSEBUTTONDOWN and Uzaygemileri_grubu.sprite.can_sayısı == 0:
                Uzaygemileri_grubu.sprite.can_sayısı=3
                meteor_grubu.empty()
                skor=0
                true_false=True
                
yazı_fontu=pg.font.Font(None,100)
skor=0
gerçekzaman=0
lazer_basma_zamanı=0
lazer_basma_zamanı2=0
lazer_basma_zamanı3=0
r=550
pg.display.set_caption("UZAY")
ikon=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\oyunbaslangıcarkaplan.png")
pg.display.set_icon(ikon)
while True:
    
    gerçekzaman=pg.time.get_ticks()
    for olay in pg.event.get():
        if olay.type==pg.QUIT:
            pg.quit()
            sys.exit()
          
        if olay.type==METEOR_OLAYI1:
            if skor%50==0 and r>=150:
                r=r-30
                METEOR_OLAYI1=pg.USEREVENT+1
                pg.time.set_timer(METEOR_OLAYI1,r) 
            meteorun_yolu=random.choice((r"C:\Bilgisayar dersleri\python\projeler/2.oyun\meteorBüyük.png",r"C:\Bilgisayar dersleri\python\projeler/2.oyun\meteorKüçük.png"))
            rastgele_x_koordinati=random.randint(0,1300)
            rastgele_y_koordinati=random.randint(-10,-5)
            rastgele_x_hizi=random.randint(-2,2)
            rastgele_y_hizi=random.randint(4,8)
            olusan_meteor=Meteorlar(meteorun_yolu,rastgele_x_koordinati,rastgele_y_koordinati,rastgele_x_hizi,rastgele_y_hizi)
            meteor_grubu.add(olusan_meteor)
        if olay.type==CANOLAYI:
            canyol=(r"C:\Bilgisayar dersleri\python\projeler\2.oyun\can.png")
            canx=random.randint(0,1300)
            cany=random.randint(-10,-5)
            canyhizi=random.randint(4,8)
            olusan_can=canlar(canyol,canx,cany,canyhizi)
            can_grubu.add(olusan_can)
        if gerçekzaman-lazer_basma_zamanı3>=150:
            if olay.type==pg.MOUSEBUTTONDOWN and olay.button==1:
                kırmızı_lazer_music.play()
                lazer_basma_zamanı3=pg.time.get_ticks()
                yenilazer=Lazer("C:\Bilgisayar dersleri\python\projeler/2.oyun\lazer_kırmızı.png",olay.pos,15)
                lazer_grubu.add(yenilazer)
        if skor%15==0 and gerçekzaman -lazer_basma_zamanı2 >=750:
            
            if olay.type==pg.MOUSEBUTTONDOWN and olay.button==3:
                    lazer_basma_zamanı2=pg.time.get_ticks()
                    yenilazer=Lazer("C:\Bilgisayar dersleri\python\projeler/2.oyun\laser_yeşil.png",olay.pos,7)
                    yesil_isin_music.play()
                    lazer_grubu_yeşil.add(yenilazer)
        if gerçekzaman -lazer_basma_zamanı >=1250:
            if olay.type==pg.MOUSEBUTTONDOWN and olay.button==2:
                uclu_lazer_music.play()
                lazer_basma_zamanı=pg.time.get_ticks()
                yenilazer=Lazer("C:\Bilgisayar dersleri\python\projeler/2.oyun\lazer_kırmızı.png",olay.pos,15)
                yenilazer2=Lazer_saga("C:\Bilgisayar dersleri\python\projeler/2.oyun\lazer_kırmızı.png",olay.pos,15)
                yenilazer3=Lazer_sola("C:\Bilgisayar dersleri\python\projeler/2.oyun\lazer_kırmızı.png",olay.pos,15)
                lazer_grubu.add(yenilazer,yenilazer2,yenilazer3)
        for lazer in lazer_grubu:
            for Meteor in meteor_grubu:
                if pg.sprite.spritecollide(Meteor,lazer_grubu,True): 
                    skor=skor+5
                pg.sprite.spritecollide(lazer,meteor_grubu,True)
        if pg.sprite.spritecollide(Uzaygemileri_grubu.sprite,meteor_grubu,True):
            Uzaygemileri_grubu.sprite.hasar(1)
            meteor_music.play()
        if pg.sprite.spritecollide(Uzaygemileri_grubu.sprite,can_grubu,True) and Uzaygemileri_grubu.sprite.can_sayısı<3:
            Uzaygemileri_grubu.sprite.hasar(-1)
        for lazer in lazer_grubu_yeşil:
            for meteor in meteor_grubu:
                if pg.sprite.spritecollide(lazer,meteor_grubu,True):
                    skor=skor+10
    pg.display.update()
    zaman.tick(120)
    ekran.blit(arkaplan,(0,0))
    if Uzaygemileri_grubu.sprite.can_sayısı > 0:
        anaoyun()
    else:
        r=500
        oyunbitti()
        