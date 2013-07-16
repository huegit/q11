# Q11-Projekt: "Risiko"
# Spielsteine und platzieren() Methode
# aktualisiert am 04.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Alexander Epple, Frank Berschneider, Paulo Rohla

from visual import *            # 3D Modul
from threading import Thread    # threading, siehe Spielbrett
from math import sin, cos       # Mathematik für Spielsteine

scene.background = color.white

class Vierzack(extrusion):
    "modelliert Spielstein mit 4 Ecken"
    def __init__(self, pos=None, hoehe=2.5, color=None):
        
        # 1. 2D-Figuren erstellen
        viereck = Polygon([(1,1),(1,-1),(-1,-1),(-1,1)])
        kreis1  = shapes.circle(pos=( 1, 1), radius=0.85)
        kreis2  = shapes.circle(pos=( 1,-1), radius=0.85)
        kreis3  = shapes.circle(pos=(-1,-1), radius=0.85)
        kreis4  = shapes.circle(pos=(-1, 1), radius=0.85)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,0,hoehe)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=viereck-kreis1-kreis2-kreis3-kreis4,
                           angle2=pi, material=materials.blazed)

class Dreizack(extrusion):
    "modelliert Spielstein mit 3 Ecken"
    def __init__(self, pos=None, hoehe=2.5, color=None):
    
        # 1. 2D-Figuren erstellen
        dreieck = Polygon([(0, 0.5*3**0.5),(1,-0.5*3**0.5),(-1,-0.5*3**0.5)])
        dreieck2 = Polygon([(0, -1.5*3**0.5),(2, 0.5*3**0.5), (-2, 0.5*3**0.5)])
        kreis1  = shapes.circle(pos=(0, -1.5*3**0.5), radius=1.8)
        kreis2  = shapes.circle(pos=(2, 0.5*3**0.5), radius=1.8)
        kreis3  = shapes.circle(pos=(-2, 0.5*3**0.5), radius=1.8)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,0,hoehe)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=dreieck+dreieck2-kreis1-kreis2-kreis3,
                           angle2=pi, material=materials.blazed)

class Fuenfzack(extrusion):
    "modelliert Spielstein mit 5 Ecken"
    def __init__(self, pos=None, hoehe=2.5, color=None):
    
        # 1. 2D-Figuren erstellen
        fuenfeck = Polygon([(cos(radians(18)), sin(radians(18))),
                            (0,1),
                            (cos(radians(162)), sin(radians(162))),
                            (cos(radians(234)), sin(radians(234))),
                            (cos(radians(306)), sin(radians(306)))])
        kreis1  = shapes.circle(pos=(cos(radians(radians(18)))/2, (sin(radians(18)) +1)/2), radius=0.3)
        kreis2  = shapes.circle(pos=(cos(radians(162))/2, (sin(radians(162))+1)/2), radius=0.3)
        kreis3  = shapes.circle(pos=((cos(radians(162))+cos(radians(234)))/2, (sin(radians(162))+sin(radians(234)))/2), radius=0.3)
        kreis4  = shapes.circle(pos=((cos(radians(306))+cos(radians(234)))/2, (sin(radians(306))+sin(radians(234)))/2), radius=0.3)
        kreis5  = shapes.circle(pos=((cos(radians(306))+cos(radians(18)))/2, (sin(radians(306))+sin(radians(18)))/2), radius=0.3)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,0,hoehe)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=fuenfeck-kreis1-kreis2-kreis3-kreis4-kreis5,
                           angle2=pi, material=materials.blazed)

def platzieren(armeen, pos1, pos2, pos3, pos4, pos5, farbe):
    "platziert Armeen anhand der Anzahl auf dem Land"
    
    armeen_old = armeen     # Anzahl der Armeen wird gespeichert
    zaehler = 0             # def Zähler
    
    try:        # versuche Armeen an den Positionen zu erstellen
        
        while armeen >= 10:     # solange mehr als 10 A
            posliste = [pos1, pos2, pos3, pos4, pos5]# Liste der Positionen
            pos=posliste[zaehler]                    # Position wird Anhand des Zählers bestimmt(daher nicht mehr als eine Figur an einer Postion) 
            Fuenfzack(pos=pos, color=farbe)          # Fünfzack wird an der Position erstellt (Wert 10)
            armeen -= 10                             # Von den A werden 10 abgezogen (Da Fünfzack erstellt)
            zaehler += 1                             # Zähler wird hochgestellt

        while armeen >= 5 and armeen < 10:      # solange mehr als 5 aber weniger als 10 A (wenn alle mogl. Fünfzacke erstellt sind)
            posliste = [pos1, pos2, pos3, pos4, pos5]# so wie oben
            pos=posliste[zaehler]
            Vierzack(pos=pos, color=farbe)           # Vierzack wird an der Position erstellt (Wert 5)
            armeen -= 5                              # Von den A werden 5 abgezogen (Da Vierzack erstellt)
            zaehler += 1                             # Zähler wird hochgestellt
                
        while armeen > 0 and armeen < 5:    # solange mehr als 0 aber weniger als 5 A (wenn alle mögl. Fünf-/Vierzacke erstellt sind) 
            posliste = [pos1, pos2, pos3, pos4, pos5]# so wie oben
            pos=posliste[zaehler]
            Dreizack(pos=pos, color=farbe)           # Dreizack wird an Position erstellt (Wert 1)
            armeen -= 1                              # Von den A wird 1 abgezogen (Da Dreizack erstellt)
            zaehler += 1                             # Zähler wird hochgestellt
            
    except IndexError:      # wenn mehr Figuren als Positionen erstellt werden müssten
        mx = (pos1[0]+pos2[0]+pos3[0]+pos4[0]+pos5[0])/5    # bestimme mittlere x Koordinate
        my = (pos1[1]+pos2[1]+pos3[1]+pos4[1]+pos5[1])/5    # bestimme mittlere y Koordinate
        mz = (pos1[2]+pos2[2]+pos3[2]+pos4[2]+pos5[2])/5    # bestimme mittlere z Koordinate
        label(pos=(mx, my, mz), text=str(armeen_old), linecolor=color.black,
              color=color.black, opacity=.5, yoffset=10)    # erstellt in der Mitte ein Schild mit den tatsächlichen A
              

        
if __name__ == "__main__":
    # kleiner Test mit 49 Armeen (=> 9 Figuren)
    platzieren(49, (0,0,3), (0,0,6), (0,0,9), (0,0,12), (0,0,15), color.red)    

    while True:
        rate(25)
        pass
        
