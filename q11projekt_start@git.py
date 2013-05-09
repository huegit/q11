# 2013-04-10
# Willkommen beim Q11-Projekt am IKG, Landsberg'
# Diese erste 'Projektdatei' wollen wir mit Git versionieren

from visual import *

erde = sphere(material=materials.earth)
print("Erde erstellt")

while True:
    rate(25)
    erde.rotate(angle=radians(1), axis=(0,1,0))
