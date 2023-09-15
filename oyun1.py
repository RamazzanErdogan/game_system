import pygame as pg
import sys
import random
import datetime
import time
pg.init()

ekran=pg.display.set_mode((1370,720))
zaman=pg.time.Clock()
su_yuksekligi=550
su_degisim_hizi=0.55 
bulut_degisim_hizi=0.10
bulut_degisim_hizi2=0.10
bulut_degisim_hizi3=0.10
bulut_konumu=1050
bulut_konumu2=150
bulut_konumu3=250
arkaplan=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler/1.oyun\göküyüzü.png")
cimenler=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\çim.png")
su=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\su.png")
bulut1=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\bulut1.png")
bulut2=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\bulut2.png")
agac1=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\ağaç1.png")
agac2=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\ağaç2.png")
imlec=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\crosshair.png")
tüfek=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\Lee Enfield Icon.png")
startbuton=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\start_button.png")
skor_button=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\skor_butonu.png")
skorbuton_degisim=1
arkaplan_music=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\orman_arkaplan.mp3")
arkaplan_music.play() 
silah_sesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\silah.mp3")
agackursun_sesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\ağaç_kurşun.mp3")
su_kursun_sesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\su_kurşun.mp3")
dalga_sesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\su_dalga.mp3")
dalga_sesi.play()
gunes_sesi=pg.mixer.Sound(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\bitiş.mp3")
hedef=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\hedef.png")
hedefkoordinatları=[]
start_time=time.time()
def hesapla_skor():
    total_sure = end_time - start_time  
    skor = total_sure  
    skor=int(skor)
    return skor
yazı_fontu=pg.font.Font(None,100)
yazı_yüzeyi=yazı_fontu.render("",True,(250,123,55))
imlec_dörtgeni =imlec.get_rect(center=(683,360)) 
silah_ates_etme_zamanı=0
a=1
oyunsonu_ekran=False
oyun_baslangıcı=True
ontane=0
skor_buttonyukseklgi=550
pg.display.set_caption("AVCI")
ikon=pg.image.load(r"C:\Bilgisayar dersleri\python\projeler\1.oyun\Lee Enfield Icon.png")
pg.display.set_icon(ikon)
while True:
        gerçekzaman=pg.time.get_ticks()
        for olay in pg.event.get(): 
            if olay.type==pg.QUIT: 
                pg.quit()
                sys.exit()
        pg.display.update() 
        zaman.tick(120) 
        ekran.blit(arkaplan,(0,0))
        if oyun_baslangıcı:
            a=0
            ontane=ontane+1
            bulut_konumu=bulut_konumu-bulut_degisim_hizi
            if bulut_konumu>=1070 or bulut_konumu<=1030:
                bulut_degisim_hizi=-1*bulut_degisim_hizi
                bulut_konumu=bulut_konumu-bulut_degisim_hizi
            bulut_konumu2=bulut_konumu2-bulut_degisim_hizi
            if bulut_konumu2>=180 or bulut_konumu<=130:
                    bulut_degisim_hizi2=-1*bulut_degisim_hizi2
                    bulut_konumu2=bulut_konumu2-bulut_degisim_hizi2
            bulut_konumu3=bulut_konumu3-bulut_degisim_hizi
            if bulut_konumu3>=250 or bulut_konumu<=230:
                    bulut_degisim_hizi3=-1*bulut_degisim_hizi3
            if olay.type==pg.MOUSEMOTION: 
                    imlec_dörtgeni=imlec.get_rect(center=olay.pos) 
            pg.mouse.set_visible(False)
            ekran.blit(bulut1,(bulut_konumu2,20))
            ekran.blit(bulut1,(bulut_konumu3,20))
            ekran.blit(bulut2,(bulut_konumu,20))
            for i in hedefkoordinatları:
                    ekran.blit(hedef,i)
            if ontane==10:
                    for i in range(10):
                        x=random.randint(50,1200)
                        y=random.randint(50,550)
                        hedef_dörtgeni=hedef.get_rect(center=(x,y))
                        hedefkoordinatları.append(hedef_dörtgeni)
            if gerçekzaman-silah_ates_etme_zamanı>=100:
                if olay.type==pg.MOUSEBUTTONDOWN: 
                    silah_ates_etme_zamanı=pg.time.get_ticks()
                    silah_sesi.play()
                    for index,vurulacakhedef in enumerate(hedefkoordinatları): 
                        if vurulacakhedef.collidepoint(olay.pos): 
                            del hedefkoordinatları[index]
                                
                        if len(hedefkoordinatları)==0:
                            ontane=0

                            gunes_sesi.play()
                            oyunsonu_ekran=True
                            oyun_baslangıcı=False
                    ağaç_koordinatları = [(0, 290), (100, 300), (150, 300), (200, 290), (300, 300), (850, 300), (900, 300), (1000, 300), (1100, 290), (1200, 300)]
                    for ağaç_x, ağaç_y in ağaç_koordinatları:
                        ağaç_dörtgeni = agac1.get_rect(topleft=(ağaç_x, ağaç_y))
                        if ağaç_dörtgeni.colliderect(imlec_dörtgeni):
                            agackursun_sesi.play()  
                    
                    if su.get_rect(topleft=(0,su_yuksekligi)).colliderect(imlec_dörtgeni): 
                        su_kursun_sesi.play()
            ekran.blit(agac2,(0,290))
            ekran.blit(agac2,(100,300))
            ekran.blit(agac1,(150,300))
            ekran.blit(agac2,(200,290))
            ekran.blit(agac1,(300,300))
            ekran.blit(agac1,(850,300))
            ekran.blit(agac2,(900,300))
            ekran.blit(agac1,(1000,300))
            ekran.blit(agac2,(1100,290))
            ekran.blit(agac1,(1200,300))
            ekran.blit(cimenler,(0,500))
            su_yuksekligi= su_yuksekligi- su_degisim_hizi
            if su_yuksekligi>=570 or su_yuksekligi<=510:
                    su_degisim_hizi *=-1
            ekran.blit(su,(0,su_yuksekligi))
            ekran.blit(tüfek,(0,500))
        if oyunsonu_ekran:
                end_time=time.time()
                if olay.type==pg.MOUSEMOTION:
                    imlec_dörtgeni=imlec.get_rect(center=olay.pos)
                ekran.blit(startbuton,(600,200))
                skor_buttonyukseklgi=skor_buttonyukseklgi-skorbuton_degisim
                if skor_buttonyukseklgi>=650 or skor_buttonyukseklgi<=540:
                     skorbuton_degisim*=-1
                ekran.blit(skor_button,(skor_buttonyukseklgi,290))
                if a==0:
                    total=hesapla_skor()
                    yazı_yüzeyi=yazı_fontu.render(str(total),True,(250,23,200))
                    a+=1
                ekran.blit(yazı_yüzeyi,(800,320))
                if olay.type==pg.MOUSEBUTTONDOWN: 
                    silah_ates_etme_zamanı=pg.time.get_ticks()
                    
                    if startbuton.get_rect(center=(600,200)).colliderect((imlec_dörtgeni)):
                        oyunsonu_ekran=False
                        oyun_baslangıcı=True
                        start_time=time.time()
                        end_time=0
                ekran.blit(imlec,imlec_dörtgeni)               
        ekran.blit(imlec,imlec_dörtgeni)
       