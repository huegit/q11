from visual import *

class iwas():
    def __init__(self, pos=(0,0,0)):

        s = shapes.rectangle(width=1, height=1)
        p = paths.pointlist([(1,1),(-1,1),(-1,-1),(1,-1)])
        
        self.flaeche=extrusion(pos=p, shape=s)
        self.box=box()

if __name__ == "__main__":
    i = iwas()
    s = shapes.rectangle(width=1, height=1)
    p = paths.pointlist([(1,1),(-1,1),(-1,-1),(1,-1)])
        
    flaeche=extrusion(pos=p, shape=s)

    while True:
        if scene.mouse.clicked:
            m = scene.mouse.getclick()
            if m.pick == i:
                print("goil")
