# Risiko
# Q11-Projekt
# Spielfeld

from visual import *                                # 3D-Modul
from threading import Thread
from time import sleep
from tkinter import *

scene.userspin=False
scene.userzoom=False
scene.width = 1100               # Fensterbreite
scene.height = 1200              # Fensterhöhe
scene.background = color.white
scene.lights = [distant_light(direction=(0,0,1),
                            color=color.gray(0.9))]
scene.forward = (0,2,-1)
scene.range = (120,120,120)

class Spielbrett(frame, Thread):
    def __init__(self):
        frame.__init__(self)
        Thread.__init__(self)
        
        BILD = materials.texture(data=materials.loadTGA("risikoskaliert.tga"),
                                 mapping='sign',interpolate=False)
        
        brett = box(size=(2,100,100),material=BILD,
                    axis=(0,0,1))               # BILD-Platzierung immer auf
        brett.rotate(angle=pi,axis=(0,0,1))     # Ursprungsaxis, deshalb diese

        tisch = box(size=(1,130,140), material=materials.wood,
                    axis=(0,0,1))
    def animation(self):
        zaehler = 0
        winkel=0.01
        while zaehler <= 110:
            scene.forward = scene.forward.rotate(angle=winkel, axis=(-0.1,0,0))
            sleep(0.01)
            scene.range -= vector(.42,.42,.42)
            zaehler += 1
        return

class Konsole(frame, Thread):
    def __init__(self, a=None):
        frame.__init__(self)
        Thread.__init__(self)
        self.a = a

    def kontinent_bekommen(self, kontinent):
        k = label(pos=scene.center, text="Sie haben "+kontinent+" erobert!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)
        sleep(3)
        k.visible=False
        del(k)

    def karte_bekommen(self, figur):
        pass

    def karte_anzeigen(self, kanone, reiter, soldat):
        k = label(pos=scene.center, text="Sie haben "+kanone+" Kanonen, "+reiter+" Reiter und "+soldat+" Soldaten!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)
        sleep(3)
        k.visible=False
        del(k)

    def karte_eintauschen(self, grund, armeen):
        k = label(pos=scene.center, text="Sie haben "+armeen+" Armeen für "+grund+" bekommen",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)
        sleep(3)
        k.visible=False
        del(k)

    def meine_armeen(self, armeen):
        self.a = label(pos=scene.center, text="Armeen: "+armeen,
                       yoffset=440, xoffset=440, height=20, box=False, color=color.black, line=0,
                       opacity=.5)
        
    def del_old(self):
        if self.a == None:
            return
        sleep(1)
        self.a.visible=False
        del(self.a)
        


if __name__=="__main__":

    feld = Spielbrett().animation()
    k = Konsole()
    k.del_old()
    k.meine_armeen("2")
    k.del_old()
    k.meine_armeen("3")
    k.kontinent_bekommen("Afrika")
    
