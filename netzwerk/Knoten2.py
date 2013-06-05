# Michael Dörsam
# 18.10.2012 sehr spät abends

länge=0

class Knoten:
    "Modelliert einfachen Listenknoten"                 # Modellieren der Klasse "Knoten"
    def __init__(self, nachfolger=None, element=None):
        "Konstruktor"
        self.nachfolger = nachfolger                    # = Nächstes Element der Liste
        self.element    = element                       # = Variable für den Input

    def einfügen(self, neuKnoten):
        "fügt neuen Knoten in die Liste ein"
        if self.nachfolger:                             # wenn Nachfolger vorhanden
            self.nachfolger.einfügen(neuKnoten)         # dann dem Nachfolger die Funktion überreichen
        else:
            self.nachfolger=Knoten(element=neuKnoten)   # wenn letztes Objekt: neues Element erstellen
            print("Neuen Knoten '", self.element,       # und Bestätigung mit Name ausgeben
                  "' eingefügt!")    

    def elemente_zählen(self):                                   
        "zählt Anzahl der Knoten"   
        global länge                                    # definieren von Variable länge
        if self.nachfolger:                             # wenn Nachfolger vorhanden
            länge += 1                                  # dann länge +1 und Funktion übergeben
            self.nachfolger.elemente_zählen()
        else:                                           # wenn letztes Objekt: länge +1 (für letztes Objekt)
            länge += 1
            print("Die Länge der Liste beträgt:",länge) # Länge ausgeben
            länge = 0                                   # und auf Null setzten

    def element_finden(self, element):
        "findet bestimmtes Element in der Liste"
        global länge                                    # definieren von Variable länge
        if self.nachfolger:                             # wenn Nachfolger vorhanden
            if self.element == element:                 # und Name entspricht gesuchtem Objekt
                länge += 1                              # dann länge +1 und Name + Position ausgeben
                print("Das Element '", element, "' befindet sich an der Stelle", länge)
                länge = 0                               # länge auf Null setzen
            else:
                länge += 1                              # wenn Name nicht gesuchtem Objekt entspricht, dann länge +1
                self.nachfolger.element_finden(element) # und Funktion übergeben
        else:
            if self.element == element:                 # wenn Objekt an letzer Stelle dann so verfahren wie sonst
                länge += 1
                print("Das Element '", element, "' befindet sich an der Stelle", länge)
                länge = 0
            else:
                print("Das Element '", element, "' befindet sich nicht auf der Liste!")
                länge = 0

    def letztes_element(self):                                   
        "gibt letztes Element mit Name und Position aus"   
        global länge                                    # definieren von Variable länge
        if self.nachfolger:                             # wenn Nachfolger vorhanden
            länge += 1                                  # dann länge +1 und Funktion übergeben
            self.nachfolger.letztes_element()
        else:                                           # wenn letztes Objekt: länge +1 (für letztes Objekt)
            länge += 1
            print("Das letze Element heißt '", self.element,
                  "' und ist an der Stelle", länge)     # Länge ausgeben
            länge = 0                                   # und auf Null setzten

    def erstes_element(self):
        "findet erstes Element"
        print("Das erste Element heißt '", self.element,
              "'")                                      # Ausgabe des ersten Elements (aKnoten...)


        
        
if __name__ == '__main__':          # wenn Hauptprogramm gestartet
    k=Knoten(element="Michael")                  # dann verschiedene Knoten erstellen
    k.einfügen("Daniel")
    k.einfügen("Maximilian")
    k.einfügen("Alexander")
    
