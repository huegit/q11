# Q11-Projekt Risiko
# Extrusionsobjekte am Beispiel eines Spielsteins
from visual import *

class Vierzack(extrusion):
    "modelliert Spielstein mit 4 Ecken"
    def __init__(self, pos=(0,0,0), höhe=3, color=color.red):
    
        # 1. 2D-Figuren erstellen
        viereck = Polygon([(1,1),(1,-1),(-1,-1),(-1,1)])
        kreis1  = shapes.circle(pos=( 1, 1), radius=0.9)
        kreis2  = shapes.circle(pos=( 1,-1), radius=0.9)
        kreis3  = shapes.circle(pos=(-1,-1), radius=0.9)
        kreis4  = shapes.circle(pos=(-1, 1), radius=0.9)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,höhe,0)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=viereck-kreis1-kreis2-kreis3-kreis4,
                           angle2=pi, material=materials.plastic)

class Kanone(extrusion):
    "modelliert Kanonenrohr bzw. Spielstein"
    def __init__(self, pos=(0,1,0), länge=3, material=materials.silver):

        # 1. 2D-Figur erstellen
        kreisaussen = shapes.circle(pos=(0,0), radius = 0.5)
        kreisinnen  = shapes.circle(pos=(0,0), radius = 0.3)

        # 2. Pfad erzeugen
        pfad = [vector(pos), vector(pos) + vector(länge,0,0)]

        # 3. Object erzeugen
        extrusion.__init__(self, pos=pfad, material=material,
                           shape=kreisaussen-kreisinnen, angle2=pi)

        # 4. Kugel hinten drauf

        ende = sphere(pos=pos, radius=.5, material=material)
        bobbel = sphere(pos=(-.4,1,0),radius=.25, material=material)

        # 5. Räder

        rad1 = ring(pos=(.5,.7,.6),material=materials.wood,axis=(0,0,1),
                    radius=.7, thickness=.2)
        rad2 = ring(pos=(.5,.7,-.6),material=materials.wood,axis=(0,0,1),
                    radius=.7, thickness=.2)
        speiche1 = cylinder(pos=(-.25,.7,.6),material=materials.wood,axis=(1.5,0,0),
                            radius=.15)
        speiche2 = cylinder(pos=(.5,0,.6),material=materials.wood,axis=(0,1.5,0),
                            radius=.15)
        speiche3 = cylinder(pos=(-.25,.7,-.6),material=materials.wood,axis=(1.5,0,0),
                            radius=.15)
        speiche4 = cylinder(pos=(.5,0,-.6),material=materials.wood,axis=(0,1.5,0),
                            radius=.15)


if __name__ == "__main__":
    "Testanweisungen, falls standalone-Aufruf"
    """v1 = Vierzack()
    v2 = Vierzack(pos=(5,0,-3),  color=color.green)
    v3 = Vierzack(pos=(-5,0,5),  color=color.yellow)
    v4 = Vierzack(pos=(4,0,-7),  color=(0.8,0.5,0.2)) #braun
    v5 = Vierzack(pos=(-6,0,-6), color=color.magenta)
    v6 = Vierzack(pos=(-2,0,4),  color=color.blue)"""
    k1 = Kanone()

    while True:
        rate(25)
        pass
        
