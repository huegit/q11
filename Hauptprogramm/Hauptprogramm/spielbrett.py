# Q11-Projekt: "Risiko"
# Spielbrett
# aktualisiert am 09.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Alexander Epple, Oliver Schmalfuß, Raphael Ditsch

from visual import *                # 3D-Modul
from threading import Thread        # threading, wichtig für parallele Abläufe
from time import sleep              # sleep() für Zeit
from tkinter import *               # tkinter für Ein/Ausgabefelder
from spielsteine import platzieren  # platzieren() Methode zum testen
from wuerfel import Wuerfel

HOEHE = 600            # Halbe Höhe des Fensters

scene.userspin=True             # kein drehen
scene.userzoom=True             # kein zoomen
scene.width = 1100              # Fensterbreite
scene.height = HOEHE*2          # Fensterhöhe (= 2x HOEHE)
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
        
        self.alaska             = Laenderbox(pos=(-43,35,0),Rand=paths.pointlist([(-3,4),(-6,-2),(-1,-4),(-1,-10),
                                                                                  (1,-10),(4,-5),(4,6),(0,7)]))
        self.nordwestterritorium= Laenderbox(pos=(-33,35,0),Rand=paths.pointlist([(-6,6),(-6,-6),(6,-7),(7,-1),(10,0),(5,9),(0,10)]))
        self.groenland          = Laenderbox(pos=(-13,37,0),Rand=paths.pointlist([(-13,-3),(-14,-9),(-11,-10),(0,-10),
                                                                                  (8,-7),(14,4),(14,12),(4,12),(-8,6)]))
        self.alberta            = Laenderbox(pos=(-37,23,0),Rand=paths.pointlist([(-7,1),(-7,-3),(6,-6),(7,5),(-2,6),(-5,2)])) 
        self.oregano            = Laenderbox(pos=(-26,20,0),Rand=paths.pointlist([(-4,8),(-5,-3),(0,-6),(1,-11),(6,-9),
                                                                                  (7,-1),(6,1),(3,2),(2,7)]))
        self.quebeck            = Laenderbox(pos=(-16,18,0),Rand=paths.pointlist([(-3,7),(-5,-6),(6,0),(2,6),(0,8)]))
        self.weststaaten        = Laenderbox(pos=(-41,13,0),Rand=paths.pointlist([(-4,7),(-7,0),(-5,-5),(-2,-4),(4,-7),(5,-7),
                                                                                  (5,-4),(6,-4),(6,-2),(10,-2),(11,3)]))
        self.oststaaten         = Laenderbox(pos=(-29,8,0),Rand=paths.pointlist([(-2,3),(-6,3),(-6,1),(-7,1),(-7,-2),(-8,-2),(-8,-3),(-3,-4),
                                                                                 (-1,-7),(-1,-4),(0,-2),(14,4),(11,5),(7,3),(6,5),(3,7),(-2,9)]))
        self.mittelamerika      = Laenderbox(pos=(-40,3,0),Rand=paths.pointlist([(-4,6),(-7,5),(-3,-3),(-1,-6),(1,-6),(5,-10),(5,-3),(2,-3),(3,1),(2,4)]))
        self.venezuela          = Laenderbox(pos=(-33,-8,0),Rand=paths.pointlist([(-1,2),(-6,0),(-10,-5),(-6,-7),(1,-3),(4,-6),(9,-4),(6,-2),(1,2)]))
        self.peru               = Laenderbox(pos=(-38,-23,0),Rand=paths.pointlist([(-2,-2),(-2,-4),(2,-7),(5,-9),(6,-9),(5,-1),(1,2),(-2,1),
                                                                                   (-2,6),(0,6),(0,7),(-6,9),(-6,5),(-5,0)]))
        self.argentinien        = Laenderbox(pos=(-39,-37,0),Rand=paths.pointlist([(-1,10),(-7,-9),(-6,-13),(-3,-13),(-4,-10),(7,-1),(5,1),(9,5)]))
        self.brasilien          = Laenderbox(pos=(-28,-19,0),Rand=paths.pointlist([(-1,5),(-3,8),(-8,7),(-8,5),(-10,4),(-10,2),(-13,1),(-12,-3),(-8,-2),(-7,-4),
                                                                                   (-5,-5),(-5,-10),(-3,-13),(-2,-13),(-6,-17),(-4,-18),
                                                                                   (-2,-18),(1,-12),(4,-12),(9,0),(4,6),]))
        self.westaustralien     = Laenderbox(pos=(37,-33,0),Rand=paths.pointlist([(-4,1),(-3,-4),(-1,-5),(5,-3),(3,0),(6,1),(5,7),(2,7)]))
        self.ostaustralien      = Laenderbox(pos=(45,-32,0),Rand=paths.pointlist([(-2,1),(-5,-1),(-4,-4),(1,-6),(4,-4),(5,0),(2,5),(2,7),(-4,7)]))
        self.neuguinea          = Laenderbox(pos=(45,-22,0),Rand=paths.pointlist([(-4,0),(-1,-2),(4,-4),(5,-3),(4,-2),(1,1),(-3,1)]))
        self.indonesien         = Laenderbox(pos=(37,-19,0),Rand=paths.pointlist([(-3,1),(-10,1),(-8,-3),(-4,-5),(3,-6),(4,-4),
                                                                                  (5,1),(5,5),(4,10),(3,10),(2,4)]))
        self.island             = Laenderbox(pos=(-4,26,0),Rand=paths.pointlist([(-3,3),(-4,0),(-1,-3),(2,-2),(3,0),(2,2),(0,3)]))
        self.skandinavien       = Laenderbox(pos=(0,17,0),Rand=paths.pointlist([(-7,-1),(-6,-7),(-1,-6),(3,-5),(4,0),(2,5),(3,10),(-2,8),(-4,1)]))
        self.ukraine            = Laenderbox(pos=(8,13,0),Rand=paths.pointlist([(9,16),(-1,9),(-2,13),(-4,13),(-6,8),(-5,3),(-5,-1),(-7,-2),(-8,-9),
                                                                                (-6,-10),(-4,-12),(-1,-11),(-2,-12),(0,-12),(1,-15),(2,-15),(1,-12),(3,-11),
                                                                                (2,-4),(4,-5),(8,1),(7,6),(10,10),(9,16)]))
        self.mitteleuropa       = Laenderbox(pos=(-2,6,0),Rand=paths.pointlist([(-1,4),(-3,0),(-5,-2),(-2,-4),(0,-3),(1,-4),
                                                                                (2,-4),(2,-1),(3,1),(3,5),(2,5)]))
        self.großbritannien     = Laenderbox(pos=(-10,7,0),Rand=paths.pointlist([(-1,3),(-2,1),(-3,-1),(-1,-3),(0,-3),(3,-2),
                                                                                 (3,0),(2,1),(2,2),(3,4),(2,5),(0,3)]))
        self.westeuropa         = Laenderbox(pos=(-8,-2,0),Rand=paths.pointlist([(-2,0),(-7,-1),(-7,-6),(-4,-7),(0,-7),(1,-2),
                                                                                 (4,-2),(4,2),(4,4),(0,6),(-4,4),(-2,2)]))
        self.suedeuropa         = Laenderbox(pos=(0,0,0),Rand=paths.pointlist([(-4,2),(-5,0),(-4,-3),(-1,-3),(-1,-7),(-4,-8),(-4,-9),
                                                                               (-1,-9),(0,-8),(3,-4),(5,3),(1,4),(-2,3),(-4,2)]))
        self.ural               = Laenderbox(pos=(21,17,0),Rand=paths.pointlist([(-6,1),(-4,-3),(-5,-4),(-1,-7),(1,-10),(3,-14),(4,-13),(4,-7),(3,-3),
                                                                                 (3,1),(3,4),(4,9),(1,12),(1,19),(-1,19),(-2,12),(-3,12),(-2,6),(-6,2)]))
        self.sibirien           = Laenderbox(pos=(29,21,0),Rand=paths.pointlist([(-7,9),(-4,8),(-4,1),(-4,-8),(-4,-17),(-2,-17),(0,-10),(4,-6),(2,-1),
                                                                                 (3,4),(4,5),(5,5),(5,8),(6,10),(7,9),(9,16),(-2,15),(-3,12),(-7,12)]))
        self.jakutien           = Laenderbox(pos=(40,27,0),Rand=paths.pointlist([(-2,9),(-4,4),(-5,4),(-5,-1),(-7,-1),(-8,-5),(-2,-5),(-1,-5),(-1,-6),
                                                                                 (-2,-7),(0,-11),(2,-9),(4,-7),(5,-6),(5,4),(6,7),(2,8),(-2,10)]))
        self.siam               = Laenderbox(pos=(29,-11,0),Rand=paths.pointlist([(2,-7),(0,-7),(-4,0),(-4,2),(-2,3),(1,5),(4,0),(4,-2)]))
        self.indien             = Laenderbox(pos=(20,-10,0),Rand=paths.pointlist([(-2,-3),(0,-8),(2,-9),(6,1),(4,5),(2,5),(1,5),(-4,3),(-6,2),(-4,-2)]))
        self.china              = Laenderbox(pos=(27,-1,0),Rand=paths.pointlist([(0,6),(-6,1),(-7,-1),(-7,-5),(-3,-4),(-1,-8),
                                                                                 (2,-6),(6,-8),(9,-6),(9,0),(7,2),(7,2),(3,4)]))
        self.mongolei           = Laenderbox(pos=(33,4,0),Rand=paths.pointlist([(-2,-2),(2,-3),(2,-4),(6,-7),(3,4),(-5,3),(-5,1)]))
        self.japan              = Laenderbox(pos=(45,1,0),Rand=paths.pointlist([(-3,-1),(-6,-3),(-4,-6),(3,0),(2,9),(-1,9),(-1,2),(-3,0)]))
        self.mittlererosten     = Laenderbox(pos=(10,-8,0),Rand=paths.pointlist([(0,-9),(5,-7),(6,-5),(4,0),(7,1),(6,4),(4,5),(-1,5),
                                                                                 (-3,8),(-7,7),(-7,5),(-1,4),(-3,0),(-5,0)]))
        self.afghanistan        = Laenderbox(pos=(17,2,0),Rand=paths.pointlist([(-6,-6),(-3,-5),(-1,-6),(0,-8),(4,-8),(4,-3),(8,1),
                                                                                (4,7),(-1,11),(-3,7),(-6,5),(-6,-4)]))
        self.irkutsk            = Laenderbox(pos=(35,15,0),Rand=paths.pointlist([(-7,-8),(1,-7),(0,-4),(5,2),(3,5),(4,6),
                                                                                 (4,7),(0,6),(-3,7),(-4,2),(-3,1)]))
        self.kamtschatka        = Laenderbox(pos=(45,17,0),Rand=paths.pointlist([(1,17),(0,5),(-10,-6),(-7,-16),(3,1),(5,2),(5,13),(3,16)]))
        self.nordwestafrika     = Laenderbox(pos=(-10,-17,0),Rand=paths.pointlist([(0,8),(-6,3),(-7,-3),(-4,-6),(0,-8),(0,-8),(5,-8),
                                                                                   (7,-8),(9,-6),(10,-6),(9,-2),(10,-1),(4,3),(7,7),(7,8),(4,7)]))
        self.aegypten           = Laenderbox(pos=(0,-12,0),Rand=paths.pointlist([(-1,-6),(2,-3),(5,-3),(7,-2),(5,4),(4,4),
                                                                                 (0,1),(-2,2),(-5,0),(-6,-3)]))
        self.kongo              = Laenderbox(pos=(0,-25,0),Rand=paths.pointlist([(-2,2),(-4,-1),(-5,-2),(-5,-3),(-2,-3),(0,-5),(2,-4),(3,3)]))
        self.ostafrika          = Laenderbox(pos=(5,-20,0),Rand=paths.pointlist([(-3,5),(-6,1),(-5,-3),(-2,-2),(-3,-7),(-1,-7),(-1,-9),
                                                                                 (0,-10),(0,-9),(1,-8),(5,-8),(5,-2),(8,3),(4,3),(2,6)]))
        self.suedafrika         = Laenderbox(pos=(2,-34,0),Rand=paths.pointlist([(-7,6),(-5,0),(-1,-7),(1,-7),(4,-4),(7,5),
                                                                                 (4,5),(3,4),(2,4),(2,7),(0,7),(0,4),(-3,4),(-4,6)]))
        self.madagaskar         = Laenderbox(pos=(12,-33,0),Rand=paths.pointlist([(-2,0),(-1,-5),(1,-5),(2,-4),(3,2),(2,6),(0,3)]))


        # K als "Darstellung" bzw. Position und L

        self.nordamerika=Screening(listeLaender=[self.alaska,self.nordwestterritorium,
                                                 self.groenland,self.alberta,self.oregano,
                                                 self.quebeck,self.weststaaten,self.oststaaten,
                                                 self.mittelamerika],
                                   center=(-25,22,0),entf=(50,50,50),col=color.red)
        
        self.suedamerika=Screening(listeLaender=[self.venezuela,self.peru,
                                                 self.argentinien,self.brasilien],
                                   center=(-32,-26,0),entf=(40,40,40),col=color.blue)
        
        self.australien=Screening(listeLaender=[self.westaustralien,self.ostaustralien,
                                                self.neuguinea,self.indonesien],
                                  center=(38,-26,0),entf=(30,30,30),col=color.yellow)

        self.europa=Screening(listeLaender=[self.island,self.skandinavien,self.ukraine,
                                            self.großbritannien,self.mitteleuropa,
                                            self.westeuropa,self.suedeuropa],
                              center=(0,11,0),entf=(40,40,40),col=color.red)

        self.asien=Screening(listeLaender=[self.ural,self.sibirien,self.irkutsk,
                                           self.jakutien,self.kamtschatka,
                                           self.afghanistan,self.china,self.mongolei,
                                           self.japan,self.mittlererosten,self.indien,
                                           self.siam],
                             center=(29,10,0),entf=(50,50,50),col=color.red)
        
        self.afrika=Screening(listeLaender=[self.nordwestafrika,self.aegypten,
                                            self.kongo,self.ostafrika,
                                            self.suedafrika,self.madagaskar],
                              center=(0,-26,0),entf=(40,40,40),col=color.green)

        # Liste der K in der richtigen Ordnung
        
        self.listeKontinente=[self.nordamerika,self.europa,self.asien,self.suedamerika,self.afrika,self.australien]

        # Gibt Name gegen Position zurück

        self.dictLaender={(-43,35,0):"Alaska",(-33,35,0):"Nordwest-Territorium",
                          (-13,37,0):"Grönland",(-37,23,0):"Alberta",(-26,20,0):"Oregano",
                          (-16,18,0):"Quebeck",(-41,13,0):"Weststaaten",(-29,8,0):"Oststaaten",
                          (-40,3,0):"Mittelamerika",(-33,-8,0):"Venezuela",(-38,-23,0):"Peru",
                          (-39,-37,0):"Argentinien",(-28,-19,0):"Brasilien",(37,-33,0):"Westaustralien",
                          (45,-32,0):"Ostaustralien",(45,-22,0):"Neuguinea",(37,-19,0):"Indonesien",
                          (-4,26,0):"Island",(0,17,0):"Skandinavien",(8,13,0):"Ukraine",
                          (-2,6,0):"Mitteleuropa",(-10,7,0):"Großbritannien",(-8,-2,0):"Westeuropa",
                          (0,0,0):"Südeuropa",(21,17,0):"Ural",(29,21,0):"Sibirien",(40,27,0):"Jakutien",
                          (29,-11,0):"Siam",(20,-10,0):"Indien",(28,-1,0):"China",(33,4,0):"Mongolei",
                          (45,1,0):"Japan",(10,-8,0):"Mittlerer Osten",(17,2,0):"Afghanistan",
                          (35,15,0):"Irkutsk",(45,17,0):"Kamtschatka",(-10,-17,0):"Nordwestafrika",
                          (0,-12,0):"Ägypten",(0,-25,0):"Kongo",(5,-20,0):"Ostafrika",(2,-34,0):"Südafrika",
                          (12,-33,0):"Madagaskar"}
        
    def animation(self):
        "Coole Animation die in die Karte zoomt"
        zaehler = 0     # def Zähler
        winkel=0.01     # def Winkel
        
        while zaehler <= 110:   # solange Zähler kleiner 110
            # Blickwinkel wird minimal justiert
            scene.forward = scene.forward.rotate(angle=winkel, axis=(-0.1,0,0)) 
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

    def land_suchen(self):
        "Methode um ein Land zu markieren"
        zaehler = 0     # wählt K
        pruefer = False # prüft, ob ein K gewählt ist
        zaehler2= 0     # wählt L
        pruefer2= False # prüft ob K gewählt ist wenn man L wählen will (Keyboard-Lag Problem)
        i=None          # aktueller K als Element

        def schwarz():
            "macht alle Boxen schwarz und unsichtbar"
            for j in i.listeLaender:             # iteriert Liste der L in Spielbrett
                j.umrandung.visible = False         # unsichtbar
                    
        while True:
            if scene.kb.keys:                   # falls Eingabe
                kb = scene.kb.getkey()          # Eingabe speichern

                if pruefer == False:            # sollte kein K gewählt sein
                    
                    if kb == "right":                                   # wenn rechte PfT:
                        zaehler+=1                                      # zaehler +1
                        aktuellerK = zaehler%(len(self.listeKontinente))# aktueller K wird mit Modulo des Zählers bestimmt 
                        i=self.listeKontinente[aktuellerK]              # K wird ausgewählt
                        i.gewaehlt()                                    # und rangezoomt  

                    if kb == "left":                                    # fast wie bei rechter PfT
                        zaehler-=1                                      # zaehler -1
                        aktuellerK = zaehler%(len(self.listeKontinente))
                        i=self.listeKontinente[aktuellerK] 
                        i.gewaehlt() 

                    if kb == "down":                                    # wenn untere PfT:
                        if scene.center == (0,0,0):                     # wenn kein K gewählt
                            continue                                    # Fkt. startet neu
                        else:
                            try:
                                pruefer=True                            # "weiter", pruefer auf True
                                j=i.listeLaender[0]                     # wählt erstes L der Liste aus
                                j.umrandung.visible=True                # macht Umrandung sichtbar
                            except AttributeError:                      # wenn es einen Fehler gibt (ich weis nicht obs den noch gibt)
                                continue                                # Fkt. startet neu
                            
                        
                    if kb == "up":                                      # wenn untere PfT:
                        scene.center = (0,0,0)                          # "zurück", rauszoomen
                        scene.range  = (73.38,73.38,73.38)
                            
                if pruefer == True:
                    # wenn Anzahl der L des ausgewählten K größer/gleich als zaehler2 und pruefer ist True (=K gewählt)
                    if kb == "right":                                   # wenn rechte PfT:
                        zaehler2+=1                                     # zaehler +1
                        schwarz()                                       # alle L-Umrandungen schwarz
                        aktuellesL = zaehler2%(len(i.listeLaender))     # L wird mithilfe von Modulo bestimmt
                        j=i.listeLaender[aktuellesL]                    # L wird ausgewählt
                        j.umrandung.visible=True                        # und Umrandung sichtbar gemacht
                        pruefer2=True                                   # pruefer2 auf True
                                        
                    if kb == "left":                                    # fast wie bei rechter PfT
                        zaehler2-=1                                     # zaehler -1
                        schwarz()
                        aktuellesL = zaehler2%(len(i.listeLaender))
                        j=i.listeLaender[aktuellesL]
                        j.umrandung.visible=True
                        pruefer2=True

                    if kb == "up":                                      # wenn obere PfT:
                        schwarz()
                        pruefer =False                                  # "zurück", pruefer auf False
                        pruefer2=False                                  # pruefer2 ebenfalls auf False
                        scene.center = (0,0,0)                          # rauszoomen
                        scene.range  = (73.38,73.38,73.38)

                    if kb == "down" and pruefer2 == True:               # wenn untere PfT:
                        # "weiter", rauszoomen
                        scene.center = (0,0,0)                  
                        scene.range  = (73.38,73.38,73.38)

                        # Koordinaten zurückgeben
                        aktuellesL = zaehler2%(len(i.listeLaender))
                        pos = tuple(i.listeLaender[aktuellesL].pos)

                        # Position zurückgeben
                        return pos
                            

    def land_waehlen(self):

        # L wird anhand der zuvor erhalten Position aus dem Dictionary bestimmt
        land = self.dictLaender[self.land_suchen()] 

        # ein Ausgabefeld wird erzeugt
        k = label(frame=self,pos=scene.center, text="Sie haben "+land+" ausgewählt!",
                  yoffset=2/3*HOEHE, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Kontinent
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

        # alle L werden schwarz und durchsichtig 
        for i in self.listeKontinente:     
            for j in i.listeLaender:
                j.umrandung.color = color.black
                j.umrandung.visible = False

        # Name des gewählten L wird zurückgegeben   
        return land             

class Laenderbox():
    "Macht das kreieren von Länderboxen einfacher, pos und Polygon-Figur werden übergeben"
    def __init__(self, pos, Rand):
        # Legt "Pfad" und Länge des Pfades (hoehe) fest
        randshape=shapes.rectangle(pos=(0,0), width=.25, height=.25)

        # Extrusionsobjekt wird erzeugt
        self.pos        = pos
        self.u          = frame(pos=pos)
        self.umrandung  =extrusion(frame=self.u,pos=Rand, color=color.black,
                                 shape=randshape, angle2=pi, visible=False)

        # und gedreht
        self.u.rotate(angle=pi, axis=(0,1,1))
        self.u.rotate(angle=pi, axis=(0,1,0))
        self.u.rotate(angle=pi, axis=(1,0,0))

class Screening():
    "Zoomt auf Kontinent"
    def __init__(self, listeLaender=[], center=None, entf=None, col=None):
        self.listeLaender=listeLaender  # Liste aller enthaltenen L
        self.center =center             # Zentrum des K
        self.entf   =entf               # benötigter Zoom
        self.col    =col                # passende Farbe

    def gewaehlt(self):
        "zoomt auf den Kontinent und gibt den L-Umrandungen die passende Farbe"
        scene.center = self.center
        scene.range = self.entf
        
        for i in self.listeLaender:
            i.umrandung.color=self.col
        
    
class Konsole(frame, Thread):
    "GUI, Bildschirmausgabe, HUD"
    def __init__(self, a=None):
        frame.__init__(self)    # siehe oben
        Thread.__init__(self)   # siehe oben
        self.a = a              # def Klassenvariable a       

    def kontinent_bekommen(self, kontinent):
        "Ausgabe des eroberten Kontinents für 3s"
        k = label(frame=self,pos=scene.center, text="Sie haben "+kontinent+" erobert!",
                  yoffset=2/3*HOEHE, height=20, box=False, color=color.black, line=0,
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
                  yoffset=2/3*HOEHE, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Anzahl der Figuren
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

    def karte_eintauschen(self, grund, armeen):
        "zeigt eingetauschte Karten und Anzahl der bekommenen A"
        k = label(frame=self,pos=scene.center, text="Sie haben "+armeen+" Armeen für "+grund+" bekommen",
                  yoffset=2/3*HOEHE, height=20, box=False, color=color.black, line=0,
                  opacity=.5)   # Schild mit Anzahl der Armeen und wieso diese erhalten
        sleep(3)                # kurze Pause
        k.visible=False         # Schild verschwindet
        del(k)                  # wird gelöscht

    def meine_armeen(self, armeen):
        "dauerhafte Anzeige der verfügbaren A"
        self.a = label(frame=self,pos=scene.center, text="Armeen: "+armeen,
                       yoffset=0.7333*HOEHE, xoffset=0.7333*HOEHE, height=20, box=False, color=color.black, line=0,
                       opacity=.5)  # Schild mit Anzahl der A, wird als Klassenvariable a festgelegt (siehe oben)
        
    def del_old(self):
        "entfernt alte Armee Anzeige bei neuer Anzahl"
        if self.a == None:  # wenn a=None (zu Beginn)
            return          # Ende der Fkt.
        sleep(1)            # kurze Pause
        self.a.visible=False# Schild verschwindet
        del(self.a)         # wird gelöscht
                    
        


if __name__=="__main__":

    # kurze Testserie mit Animation und Figuren platzieren und würfeln
    
    feld = Spielbrett()
    feld.animation()
    feld.land_waehlen()
    platzieren(28, (-27.9943460056803, -24.5804013708412, 0), (-24.9217958343251, -25.263190297809, 0), (-31.4082906405193, -27.9943460056803, 0), (-26.2873736882607, -16.3869342472275, 0), (-34.4808408118745, -16.3869342472275, 0), color.red)
    sleep(1)
    w = Wuerfel(spielfeldpos=feld.pos, pos=(-15,-15,60), color=(0.9,0,0)).start()
    sleep(0.2)
    w2= Wuerfel(spielfeldpos=feld.pos, pos=(15,-15,60), color=(0.9,0,0)).start()
