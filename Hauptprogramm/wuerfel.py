# Q11-Projekt: "Risiko"
# Würfel
# aktualisiert am 09.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Michael Naum, Maximilian Winkler, Alexander Epple


from visual import *            # Importiert 3D Modul  
import random                   # Importiert Zufall
from time import sleep          # Importiert Zeit (warten)
from threading import Thread    # Importiert Multithreading

# verschönert die Testsequenz
lamp = local_light(pos=(0,10,0), color=color.white)
lamp = local_light(axis=(0,1,0),pos=(15,20,15), color=(0.7,0.7,0.7))
lamp = local_light(axis=(0,1,0),pos=(-15,20,-15), color=(0.7,0.7,0.7))
lamp = local_light(axis=(0,1,0),pos=(-15,20,15), color=(0.7,0.7,0.7))
lamp = local_light(axis=(0,1,0),pos=(15,20,-15), color=(0.7,0.7,0.7))
lamp = local_light(axis=(0,0,-1),pos=(0,5,0), color=(1,1,1))
scene.height=550
scene.width=700
scene.background = color=(0.7,0.9,1)
scene.forward = (0,-1,2)

# Angaben
SpielbrettFarbe=(0.4,0.4,0.4)                
WürfelPosXYZ=(0,100,0)     
SpielbrettPosXYZ=(0,0,0)
ColorAugen=(1,1,1)

class Brett(cylinder):
    "Testbrett, unwichtig"
    def __init__(self,axis=(0,0,1),pos=(SpielbrettPosXYZ),\
                 radius=100,color=SpielbrettFarbe,frame=None):
        cylinder.__init__(self, color=color, pos=pos, frame=frame)
        self.axis=axis
        self.pos=pos
        self.radius=radius
        self.color=color

class Auge():
    "Klasse Auge, macht das erstellen des Würfels leichter"
    def __init__(self, frame, pos, radius=0.7, color=ColorAugen):
        self.auge= sphere(frame=frame, pos=pos, radius=radius, color=color)

class Wuerfel(Thread, frame):
    "Hauptklasse Würfel, kann würfeln"
    def __init__(self, pos, spielfeldpos, color=(1,0,1)):
        # Definitionen
        Thread.__init__(self)
        frame.__init__(self)
        self.pos=pos
        self.spielfeldpos=spielfeldpos
        self.b=box(frame=self,axis=(0,0,1),size=(10,10,10),color=color)

        # Liste der Augenpositionen des Würfels (bei der 5 fehlt eins!!!)
        self.posL=[(0,-5,0),(5,2.5,-2.5),(5,-2.5,2.5),
                   (0,0,5),(-2.5,2.5,5),(2.5,-2.5,5),
                   (-2.5,2.5,-5),(-2.5,-2.5,-5),(2.5,2.5,-5),
                   (2.5,-2.5,-5),(-5,2.5,2.5),(-5,2.5,-2.5),
                   (-5,-2.5,2.5),(-5,0,0),(-2.5,5,-2.5),(-2.5,5,0),
                   (-2.5,5,2.5),(2.5,5,2.5),(2.5,5,0),(2.5,5,-2.5)]
        
    def Auge_machen(self):
        "erstllt die Augenpaare"
        for i in self.posL:     # iteriert Liste der Augenpositionen
            index = self.posL.index(i)  # bestimmt Index des akt. Element 
            a=Auge(pos=self.posL[index], frame=self)    # erstellt Auge mit Position der Liste + eig. Frame
            
    def run(self):
        "würfel-Methode"
        self.Auge_machen()  # erstellt Augen
        
        while self.pos.z > self.spielfeldpos.z+10:
            # lässt würfel bis best. Pos. fallen             
            rate(100)
            self.pos.z=self.pos.z-2
            self.rotate(angle=pi/4,axis=(1,0,0))
            self.rotate(angle=pi/4,axis=(0,1,0))
            self.rotate(angle=pi/4,axis=(0,0,1))
            self.axis=(0,1,0)

        Augenzahl=random.randint(1,6)   # Zufallszahl

        # Was passiert bei den jeweiligen Zahlen (Ausrichtung des Würfels)
        if Augenzahl==1:
            self.rotate(angle=0.75*pi, axis=(0,1,0))
        elif Augenzahl==2:
            self.axis=(0,0,1)
        elif Augenzahl==3:
            self.rotate(angle=-0.75*pi, axis=(0,1,0))
        elif Augenzahl==4:
            self.rotate(angle=0.25*pi, axis=(0,1,0))
        elif Augenzahl==5:
            self.axis=(0,0,-1)
        elif Augenzahl==6:
            self.rotate(angle=-0.25*pi, axis=(0,1,0))

        # Augenzahl ausgeben
        print("Augenzahl:", Augenzahl)

        # sobald man klickt werden die Würfel entfernt
        while True:
            if scene.mouse.events:
                self.visible = False
                del(self)
                return Augenzahl

# hier folgt noch ein kleines Testprogramm
if __name__ == "__main__":

    feld = Brett()
    
    while True:
        if scene.kb.keys:
            w = scene.kb.getkey()
            if w == "1":
                a=Wuerfel(pos=(-15,-15,60),spielfeldpos=feld.pos,color=(0.9,0,0))
                a.start()
                sleep(0.1)
                b=Wuerfel(pos=(15,15,60),spielfeldpos=feld.pos,color=(0.9,0,0))
                b.start()
                sleep(0.1)
