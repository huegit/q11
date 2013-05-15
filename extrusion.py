# Q11-Projekt Risiko
# Extrusionsobjekte am Beispiel eines Spielsteins
from visual import *

class Vierzack(extrusion):
    "modelliert Spielstein mit 4 Ecken"
    def __init__(self, pos=(0,0,0), höhe=3, color=color.red):
    
        # 1. 2D-Figuren erstellen
        viereck = Polygon([(1,1),(1,-1),(-1,-1),(-1,1)])
        kreis1  = shapes.circle(pos=( 1, 1), radius=0.9)
        kreis2  = shapes.circle(pos=( 1, 1), radius=0.6)
        #kreis3  = shapes.circle(pos=(-1,-1), radius=0.9)
        #kreis4  = shapes.circle(pos=(-1, 1), radius=0.9)

        # 2. Pfad erzeugen (hier entlang y-Achse)
        # Tupel lassen sich elementweise addieren, Vektoren schon!
        pfad = [vector(pos),vector(pos) + vector(0,höhe,50)]

        # 3. Extrusionsobjekt erzeugen
        extrusion.__init__(self, pos=pfad, color=color,
                           shape=kreis1-kreis2,
                           angle2=pi, material=materials.plastic)


if __name__ == "__main__":
    "Testanweisungen, falls standalone-Aufruf"
    v1 = Vierzack()
    #v2 = Vierzack(pos=(5,0,-3),  color=color.green)
    #v3 = Vierzack(pos=(-5,0,5),  color=color.yellow)
    #v4 = Vierzack(pos=(4,0,-7),  color=(0.8,0.5,0.2)) #braun
    #v5 = Vierzack(pos=(-6,0,-6), color=color.magenta)
    #v6 = Vierzack(pos=(-2,0,4),  color=color.blue)

    while True:
        rate(25)
        pass
        
