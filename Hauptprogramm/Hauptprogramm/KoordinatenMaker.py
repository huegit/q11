from spielbrett import Spielbrett
from visual import *


if __name__ == "__main__":
    s = Spielbrett()
    s.animation()
    pos = None
    x = None
    y = None
    z = None
    x2 = None
    y2 = None
    z2 = None
    pos2 = None
    zaehler = 0

    name=input("Land:")

    print("self.",name," = Laenderbox(pos=",sep="")

    while True:
        if scene.mouse.clicked and zaehler==0:
            m = scene.mouse.getclick()
            pos = m.pos
            (x,y,z) = pos
            z=0
            x=round(int(x),2)
            y=round(int(y),2)
            print("(",x,",",y,",",z,"),Rand=paths.pointlist([",sep="")
            zaehler = 1
        elif scene.mouse.clicked and zaehler==1:
            m = scene.mouse.getclick()
            pos2 = m.pos
            (x2,y2,z2) = pos2
            x2=round(int(x2),2)
            x2=x2-x
            y2=round(int(y2),2)
            y2=y2-y
            print("(",x2,",",y2,")",sep="",end=",")
            
            
   
