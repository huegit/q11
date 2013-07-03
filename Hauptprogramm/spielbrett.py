# Risiko
# Q11-Projekt
# Spielfeld

from visual import *                                # 3D-Modul
from threading import Thread
from time import sleep
from tkinter import *

scene.userspin=False
scene.userzoom=True
scene.width = 1100               # Fensterbreite
scene.height = 1200              # Fensterhöhe
scene.lights = [distant_light(direction=(0,0,1),
                            color=color.gray(0.9))] # Beleuchtung von oben
                                                    # fuer bessere Farben 

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

class Konsole(frame, Thread):
    def __init__(self):
        frame.__init__(self)
        Thread.__init__(self)

    def kontinent_bekommen(self, kontinent):
        k = label(pos=scene.center, text="Sie haben "+kontinent+" erobert!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)
        sleep(3)
        k.visible=False
        del(k)

    def karte_bekommen(self, figur):
        pass

    def meine_armeen(self, armeen):
        k = label(pos=scene.center, text="Sie haben "+armeen+" Armeen zur Verfügung!",
                  yoffset=400, height=20, box=False, color=color.black, line=0,
                  opacity=.5)
        sleep(3)
        pass


if __name__=="__main__":

    feld = Spielbrett()
    k = Konsole()
    k.kontinent_bekommen("Afrika")
    k.meine_armeen("3")
