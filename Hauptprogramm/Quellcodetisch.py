# Risiko
# Q11-Projekt
# Spielfeld

from visual import *                                # 3D-Modul

scene.fullscreen = True                             # Fullscreen einschalten
scene.userspin=False
scene.userzoom=False


BILD = materials.texture(data=materials.loadTGA("risikoskaliert.tga"),mapping='sign',interpolate=False)

if __name__=="__main__":
    brett = box(size=(2,100,100),material=BILD,
                axis=(0,0,1))                       # BILD-Platzierung immer auf
    brett.rotate(angle=pi,axis=(0,0,1))           # Ursprungsaxis, deshalb diese

    tisch = box(size=(1,130,140), material=materials.wood,
                axis=(0,0,1))
                
                                                    # geaendert (brett 'flachgelegt')
    scene.lights = [distant_light(direction=(0,0,1),
                            color=color.gray(0.9))] # Beleuchtung von oben
                                                    # fuer bessere Farben 
