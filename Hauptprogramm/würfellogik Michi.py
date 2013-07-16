from visual import *      
import random               
from time import sleep    

scene.title = "Wuerfel"     
scene.background = color=(176/255,226/255,255/255)     
WürfelFarbe=(0,0,0)        
SpielbrettFarbe=(50/255,205/255,50/255)        
WürfelPosX=0                                    
WürfelPosY=50     
WürfelPosZ=0        
WürfelPosXYZ=(WürfelPosX,WürfelPosY,WürfelPosZ)     
SpielbrettPosX=0
SpielbrettPosY=-50
SpielbrettPosZ=0
SpielbrettPosXYZ=(SpielbrettPosX,SpielbrettPosY,SpielbrettPosZ)
#KugelRadius=9         
Winkel=0.1             
ColorAugen=(1,1,1)      



class Spielbrett(cylinder):         
    def __init__(self,axis=(0,1,0),pos=(SpielbrettPosXYZ),\
                 radius=100,color=SpielbrettFarbe,frame=None):
        cylinder.__init__(self, color=color, pos=pos, frame=frame)
        self.axis=axis
        self.pos=pos
        self.radius=radius
        self.color=color

class Würfel(frame):           
    def __init__(self,pos=(WürfelPosXYZ),color=ColorAugen):
        frame.__init__(self)
        self.pos=pos
        b=box(frame=self,axis=(0,0,1),size=(10,10,10),color=WürfelFarbe)
        #c=sphere(axis=(0,0,1),frame=self,radius=KugelRadius,opacity=0.1)       
        s11=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(0,-5,0))

        s21=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(5,2.5,-2.5))
        s22=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(5,-2.5,2.5))

        s31=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(0,0,5))
        s32=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,2.5,5))
        s33=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,-2.5,5))

        s41=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,2.5,-5))
        s42=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,-2.5,-5))
        s43=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,2.5,-5))
        s44=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,-2.5,-5))

        s51=  sphere(frame=self,radius=0.7, color=ColorAugen,pos=(-5,2.5,2.5))
        s52=  sphere(frame=self,radius=0.7, color=ColorAugen,pos=(-5,2.5,-2.5))
        s53=  sphere(frame=self,radius=0.7, color=ColorAugen,pos=(-5,-2.5,2.5))
        s54=  sphere(frame=self,radius=0.7, color=ColorAugen,pos=(-5,-2.5,-2.5))
        s55=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-5,0,0))

        s61=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,5,-2.5))
        s62=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,5,0))
        s63=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(-2.5,5,2.5))
        s64=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,5,2.5))
        s65=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,5,0))
        s66=  sphere(frame=self,radius=0.7,color=ColorAugen, pos=(2.5,5,-2.5))


 
    def würfeln(self):          
        while self.pos.y > SpielbrettPosY+6.5:              
            sleep(0.005)                    
            AugenOpacity=0                  
            #self.pos.x=self.pos.x+random.randint(0,30000)/100000       
            self.pos.y=self.pos.y-1                                 
            #self.pos.z=self.pos.z+random.randint(-10000,10000)/100000
            self.rotate(angle=pi/2,axis=(1,0,0))      
            self.rotate(angle=pi/2,axis=(0,1,0))    
            self.rotate(angle=pi/2,axis=(0,0,1))     
            #print(self.pos)      
        Augenzahl=random.randint(3,3)  
        print(Augenzahl)              
        scene.center=self.pos          
        if Augenzahl==2:               
            self.axis=(0,1,0)
        elif Augenzahl==5:
            self.axis=(0,-1,0)
            
        elif Augenzahl==3:
           # self.axis=(0,1,0)
           print(self.axis)
        #elif Augenzahl==1:
         #   self.axis=(0,0,2)
        #elif Augenzahl==4:
           # self.axis=(0,0,1)
            #self.rotate(angle=pi, axis=(1,0,0))
        #elif Augenzahl==6:
         #   self.axis=(0,0,-1)
                       
        
        print(self.axis)        

        


        
s=Spielbrett()
w=Würfel(pos=(random.randint(-s.radius/2,s.radius/2),100,random.randint(-s.radius/2,s.radius/2)))
w.würfeln()
#y=Würfel(pos=(random.randint(-s.radius/2,s.radius/2),100,random.randint(-s.radius/2,s.radius/2)))
#y.würfeln()
