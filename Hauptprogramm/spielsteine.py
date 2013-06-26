# Q11-Projekt Risiko
# Extrusionsobjekt Spielstein
from visual import *
from math import sin, cos

class Vierzack(extrusion):
    "modelliert Spielstein mit 4 Ecken"
    def __init__(self, pos=(0,0,0), hoehe=2.5, color=color.red):
    
        # 1. 2D-Figuren erstellen
        viereck = Polygon([(1,1),(1,-1),(-1,-1),(-1,1)])
        kreis1  = shapes.circle(pos=( 1, 1), radius=0.85)
        kreis2  = shapes.circle(pos=( 1,-1), radius=0.85)
        kreis3  = shapes.circle(pos=(-1,-1), radius=0.85)
        kreis4  = shapes.circle(pos=(-1, 1), radius=0.85)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,hoehe,0)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=viereck-kreis1-kreis2-kreis3-kreis4,
                           angle2=pi, material=materials.blazed)

class Dreizack(extrusion):
    "modelliert Spielstein mit 3 Ecken"
    def __init__(self, pos=(0,0,0), hoehe=2.5, color=color.red):
    
        # 1. 2D-Figuren erstellen
        dreieck = Polygon([(0, 0.5*3**0.5),(1,-0.5*3**0.5),(-1,-0.5*3**0.5)])
        dreieck2 = Polygon([(0, -1.5*3**0.5),(2, 0.5*3**0.5), (-2, 0.5*3**0.5)])
        kreis1  = shapes.circle(pos=(0, -1.5*3**0.5), radius=1.8)
        kreis2  = shapes.circle(pos=(2, 0.5*3**0.5), radius=1.8)
        kreis3  = shapes.circle(pos=(-2, 0.5*3**0.5), radius=1.8)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,hoehe,0)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=dreieck+dreieck2-kreis1-kreis2-kreis3,
                           angle2=pi, material=materials.blazed)

class Fuenfzack(extrusion):
    "modelliert Spielstein mit 5 Ecken"
    def __init__(self, pos=(0,0,0), hoehe=2.5, color=color.red):
    
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
        pfad = [vector(pos),vector(pos) + vector(0,hoehe,0)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=fuenfeck-kreis1-kreis2-kreis3-kreis4-kreis5,
                           angle2=pi, material=materials.blazed)

class Spielstein(Dreizack, Vierzack, Fuenfzack):
    "modelliert Spielstein nach Eingabe der Armeestärke"
    def __init__(self, position=(0,0,0), spieler=color.red, truppenzahl=1):
        if truppenzahl <= 4:
            Dreizack.__init__(self, pos=position, color=spieler)
        else:
            if truppenzahl >= 10:
                Fuenfzack.__init__(self, pos=position, color=spieler)
            else:
                Vierzack.__init__(self, pos=position, color=spieler)

        
if __name__ == "__main__":
    "Testanweisungen, falls standalone-Aufruf"
    v1 = Spielstein(position=(0,0,0), truppenzahl=5, spieler= color.blue)
    v2 = Spielstein(position=(6,0,0), truppenzahl=10, spieler = color.green)
    v3 = Spielstein(position=(-6,0,0), truppenzahl=1)

    while True:
        rate(25)
        pass
        
