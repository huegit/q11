# Q11-Projekt: "Risiko"
# Spielbrett
# aktualisiert am 04.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Alexander Epple, Oliver Schmalfuß, Raphael Ditsch

from visual import *                # 3D-Modul
from threading import Thread        # threading, wichtig für parallele Abläufe
from time import sleep              # sleep() für Zeit
from tkinter import *               # tkinter für Ein/Ausgabefelder
from spielsteine import platzieren  # platzieren() Methode zum testen

scene.userspin=False            # kein drehen
scene.userzoom=True            # kein zoomen
scene.width = 1100              # Fensterbreite
scene.height = 1200             # Fensterhöhe
scene.background = color.white  # Hintergrundfarbe
scene.lights = [distant_light(direction=(0,0,1),
                            color=color.gray(0.9))] # Beleuchtung
scene.forward = (0,2,-1)        # Blickwinkel
scene.range = (120,120,120)     # Abstand zur Karte

class Spielbrett(frame, Thread):
    "Klasse Spielbrett, kann sich bewegen"
    def __init__(self, pos=(0,0,0)):
        frame.__init__(self, pos=pos)    # frame Modul (damit zusammen bleibt was zusammen gehört)
        Thread.__init__(self)   # Thread Modul, siehe oben
        
        BILD = materials.texture(data=materials.loadTGA("risikoskaliert.tga"),
                                 mapping='sign',interpolate=False)  # Spielbrett Textur
        
        self.brett = box(frame=self,pos=(0,0,-1.1),size=(2,100,100),material=BILD,
                    axis=(0,0,1)).rotate(angle=pi,axis=(0,0,1))     # Brett Objekt mit Textur von oben, muss gedreht werden

        self.tisch = box(frame=self,pos=(0,0,-1.1),size=(1,130,140), material=materials.wood,
                    axis=(0,0,1))                                   # Tischplatte

        # Länderboxen
        
        self.alaska=box(frame=self, pos=(-45,34,0), size=(1,17,10), axis=(0,0,1), color=color.black, opacity=0)
        self.nordwestterritorium=box(frame=self, pos=(-32,37,0), size=(1,17,16), axis=(0,0,1), color=color.black, opacity=0)
        self.alberta=box(frame=self, pos=(-38,23,0), size=(1,12,14), axis=(0,0,1), color=color.black, opacity=0)
        self.weststaaten=box(frame=self, pos=(-41,13,0), size=(1,10,14), axis=(0,0,1), color=color.black, opacity=0)
        self.mittelamerika=box(frame=self, pos=(-40,1.5,0), size=(1,13,10), axis=(0,0,1), color=color.black, opacity=0)
        self.oststaaten=box(frame=self, pos=(-26,7,0), size=(1,13,15), axis=(0,0,1), color=color.black, opacity=0)
        self.ontario=box(frame=self, pos=(-25,21,0), size=(1,15,12), axis=(0,0,1), color=color.black, opacity=0)
        self.quebeck=box(frame=self, pos=(-15,20,0), size=(1,12,8), axis=(0,0,1), color=color.black, opacity=0)
        self.groenland=box(frame=self, pos=(-12,39,0), size=(1,18,25), axis=(0,0,1), color=color.black, opacity=0)
        self.venezuela=box(frame=self, pos=(-35,-9.5,0), size=(1,9,18), axis=(0,0,1), color=color.black, opacity=0)
        self.brasilien=box(frame=self, pos=(-27,-24,0), size=(1,20,15), axis=(0,0,1), color=color.black, opacity=0)
        self.peru=box(frame=self, pos=(-39,-22.5,0), size=(1,17,8), axis=(0,0,1), color=color.black, opacity=0)
        self.argentinien=box(frame=self, pos=(-40,-40,0), size=(1,17,12), axis=(0,0,1), color=color.black, opacity=0)

        # Liste mit allen Länderboxen

        self.listeLaender=[self.alaska, self.nordwestterritorium, self.alberta,
                           self.weststaaten, self.mittelamerika, self.oststaaten,
                           self.ontario, self.quebeck, self.groenland, self.venezuela,
                           self.brasilien, self.peru, self.argentinien]
        



        
    def animation(self):
        "Coole Animation die in die Karte zoomt"
        zaehler = 0     # def Zähler
        winkel=0.01     # def Winkel
        
        while zaehler <= 110:   # solange Zähler kleiner 110
            scene.forward = scene.forward.rotate(angle=winkel, axis=(-0.1,0,0)) # Blickwinkel wird minimal justiert
            sleep(0.0075)       # kurze Pause
            scene.range -= vector(.42,.42,.42)  # Es wird gezoomt
            zaehler += 1        # und der Zähler hochgestellt
        return          # Ende der Fkt.
    
    def animation_back(self):
        "Coole Animation zurück, funktioniert wie die erste"
        zaehler = 0     
        winkel=-0.01
        
        while zaehler <= 110:
            scene.forward = scene.forward.rotate(angle=winkel, axis=(-0.1,0,0))
            sleep(0.0075)
            scene.range -= vector(-.42,-.42,-.42)
            zaehler += 1
        return

    def land_waehlen(self):
        zaehler = 0
        while True:
            if scene.mouse.events:
                mEvent = scene.mouse.getclick()
                for i in self.listeLaender:

                    def schwarz():
                        for j in self.listeLaender:
                            j.color = color.black
                            j.opacity = 0
                    
                    if mEvent.pick == i and i.color == color.black:
                        schwarz()
                        i.color = color.red
                        i.opacity = 0.5
                        zaehler = 1
                        continue

                    elif mEvent.pick == i and i.color == color.red and zaehler == 1:
                        k = label(frame=self,pos=scene.center, text="Land "+str(i)+" ausgewählt!",
                                  yoffset=400, height=20, box=False, color=color.black, line=0,
                                  opacity=.5)   # Schild mit Kontinent
                        sleep(3)                # kurze Pause
                        k.visible=False         # Schild verschwindet
                        del(k)                  # wird gelöscht
                        return 
                                
    
class Konsole(frame, Thread):
    "GUI, Bildschirmausgabe, HUD"
    def __init__(self, a=None):
        frame.__init__(self)    # siehe oben
        Thread.__init__(self)   # siehe oben
        self.a = a              # def Klassenvariable a       

    def kontinent_bekommen(self, kontinent):
        "Ausgabe des eroberten Kontinents für 3s"
        k = label(frame=self,pos=scene.center, text="Sie haben "+kontinent+" erobert!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Kontinent
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

    def karte_bekommen(self, figur):    # momentan keine Ausgabe
        "zeigt Bild der bekommenen Figur"
        pass

    def karte_anzeigen(self, kanone, reiter, soldat):
        "zeigt Anzahl der verfügbaren Karten"
        k = label(frame=self,pos=scene.center, text="Sie haben "+kanone+" Kanonen, "+reiter+" Reiter und "+soldat+" Soldaten!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Anzahl der Figuren
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

    def karte_eintauschen(self, grund, armeen):
        "zeigt eingetauschte Karten und Anzahl der bekommenen A"
        k = label(frame=self,pos=scene.center, text="Sie haben "+armeen+" Armeen für "+grund+" bekommen",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Anzahl der Armeen und wieso diese erhalten
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

    def meine_armeen(self, armeen):
        "dauerhafte Anzeige der verfügbaren A"
        self.a = label(frame=self,pos=scene.center, text="Armeen: "+armeen,
                       yoffset=440, xoffset=440, height=20, box=False, color=color.black, line=0,
                       opacity=.5)  # Schild mit Anzahl der A, wird als Klassenvariable a festgelegt (siehe oben)
        
    def del_old(self):
        "entfernt alte Armee Anzeige bei neuer Anzahl"
        if self.a == None:  # wenn a=None (zu Beginn)
            return          # Ende der Fkt.
        sleep(1)            # kurze Pause
        self.a.visible=False# Schild verschwindet
        del(self.a)         # wird gelöscht
                    
        


if __name__=="__main__":

    # kurze Testserie mit animation und Figuren platzieren
    
    feld = Spielbrett()
    feld.animation()
    feld.land_waehlen()
    #platzieren(28, (-27.9943460056803, -24.5804013708412, 0), (-24.9217958343251, -25.263190297809, 0), (-31.4082906405193, -27.9943460056803, 0), (-26.2873736882607, -16.3869342472275, 0), (-34.4808408118745, -16.3869342472275, 0), color.red)
    sleep(1)
