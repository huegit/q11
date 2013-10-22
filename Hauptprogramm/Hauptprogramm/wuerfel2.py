# Q11-Projekt: "Risiko"
# Würfel made by Epple, geht besser
# aktualisiert am 20.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Alexander Epple

from visual import *
import random
from time import sleep
from threading import Thread

scene.forward = (0,-1,-2)
scene.background = color.white

class Auge():
    def __init__(self, frame, pos, radius=.5, color=color.white):
        self.auge=sphere(frame=frame, pos=pos, radius=radius, color=color)

class Wuerfel(Thread, frame):
    def __init__(self, pos, spielfeldpos, color):
        Thread.__init__(self)
        frame.__init__(self)
        self.pos=pos
        self.spielfeldpos=spielfeldpos
        self.box=box(frame=self, size=(5,5,5), color=color)

        self.posL=[(0,0,2.5),
                   (1.25,2.5,1.25),(-1.25,2.5,-1.25),
                   (-2.5,0,0),(-2.5,1.25,1.25),(-2.5,-1.25,-1.25),
                   (2.5,1.25,1.25),(2.5,-1.25,1.25),(2.5,1.25,-1.25),(2.5,-1.25,-1.25),
                   (0,-2.5,0),(1.25,-2.5,1.25),(-1.25,-2.5,1.25),(1.25,-2.5,-1.25),(-1.25,-2.5,-1.25),
                   (1.25,0,-2.5),(-1.25,0,-2.5),(1.25,1.25,-2.5),(-1.25,1.25,-2.5),(1.25,-1.25,-2.5),(-1.25,-1.25,-2.5)]

    def auge_machen(self):
        for i in self.posL:
            index = self.posL.index(i)
            auge  = Auge(pos=self.posL[index], frame=self)

    def run(self):
        self.auge_machen()
        xbew = random.randint(-1,1)/1000
        ybew = random.randint(-1,1)/1000
        zaehler = 0

        while self.pos[2] > self.spielfeldpos[2]+2.5:
            rate(25)
            self.pos -= vector(0,0,1)
            self.rotate(angle=pi/4, axis=(0,1,0))
            self.rotate(angle=pi/4, axis=(0,0,1))
            self.rotate(angle=pi/4, axis=(1,0,0))
            self.pos[0] -= xbew*(zaehler^2)
            self.pos[1] -= ybew*(zaehler^2)
            zaehler    += 1

        augenzahl=2

        if augenzahl == 2:
            self.axis=(0,1,0)
            self.axis=(1,0,0)
            self.axis=(0,0,1)
            self.rotate(angle=pi/2, axis=(1,0,0))

        if augenzahl == 3:
            self.axis=(0,1,0)
            self.axis=(1,0,0)
            self.axis=(0,0,-1)
            
        if augenzahl == 4:
            self.axis=(0,1,0)
            self.axis=(1,0,0)
            self.axis=(0,0,1)

if __name__ == "__main__":
    w=Wuerfel(pos=(0,0,0),spielfeldpos=(0,0,-50),color=color.red).start()
    b=box(pos=(0,0,-50), size=(50,50,1))
