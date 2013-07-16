from spielbrett import Spielbrett
from visual import *

class maßbandx(frame):
    def __init__(self, pos, axis, color=color.black):
        frame.__init__(self, pos=pos, axis=axis)
        self.pos = pos
        self.axis = axis
        self.color = color

        self.masunten = box(frame=self, pos=(0,-50,0), size=(100,.5,.5),
                            axis=axis, color=color)

class maßbandy(frame):
    def __init__(self, pos, axis, color=color.black):
        frame.__init__(self, pos=pos, axis=axis)
        self.pos = pos
        self.axis = axis
        self.color = color

        self.masunten = box(frame=self, pos=(0,50,0), size=(.5,100,.5),
                            axis=axis, color=color)
     
    

if __name__ == "__main__":

    my1 = maßbandy((0,0,0), (0,1,0))
    my2 = maßbandy((25,0,0), (0,1,0))
    my3 = maßbandy((50,0,0), (0,1,0))
    my4 = maßbandy((75,0,0), (0,1,0))
    my5 = maßbandy((100,0,0), (0,1,0))
    mx1 = maßbandx((0,0,0), (1,0,0))
    mx2 = maßbandx((0,25,0), (1,0,0))
    mx3 = maßbandx((0,50,0), (1,0,0))
    mx4 = maßbandx((0,75,0), (1,0,0))
    mx5 = maßbandx((0,100,0), (1,0,0))
    s = Spielbrett()
    s.animation()
