# Einfach verkettete Liste
# Michael Dörsam
# 18.10.2012 sehr spät abends

#länge=0

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
        #global länge                                    # definieren von Variable länge
        if self.nachfolger:                             # wenn Nachfolger vorhanden
            #länge += 1                                  # dann länge +1 und Funktion übergeben
            return self.nachfolger.elemente_zählen() + 1
        else:                                           # wenn letztes Objekt: länge +1 (für letztes Objekt)
            #länge += 1
            #print("Die Länge der Liste beträgt:",länge) # Länge ausgeben
            #länge = 0                                   # und auf Null setzen
            return 1 

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

class Liste:
    "Modelliere einfaches Listenobjekt"                 # Modellieren der Klasse Liste
    def __init__(self, aKnoten=None):
        "Konstruktor"
        self.aKnoten=aKnoten                            # = erstes Objekt in der Liste

    def einfügen(self, neuKnoten):
        if self.aKnoten:                                # wenn Anfangsknoten vorhanden
            self.aKnoten.einfügen(neuKnoten)            # dann eingegebenen Wert (neuKnoten) überreichen und einfügen() ausführen
        else:
            self.aKnoten=Knoten(element=neuKnoten)      # sonst: neues Objekt aKnoten erstellen

    def elemente_zählen(self):
        if self.aKnoten:                                # wenn Anfangsknoten vorhanden
            return self.aKnoten.elemente_zählen()       # dann elemente_zählen() ausführen
        else:
            print("Die Liste hat keine Knoten!")        # ansonsten: Listenlänge=0 ausgeben
            return 0

    def element_finden(self, element):
        if self.aKnoten:                                # wenn Anfangsknoten vorhanden
            self.aKnoten.element_finden(element)        # dann element_finden() ausführen
        else:
            print("Die Liste hat keine Knoten!")        # ansonsten: Listenlänge=0 ausgeben

    def letztes_element(self):
        if self.aKnoten:                                # wenn Anfangsknoten vorhanden
            self.aKnoten.letztes_element()              # dann letztes_element() ausführen
        else:
            print("Die Liste hat keine Knoten!")        # ansonsten: Listenlänge=0 ausgeben

    def erstes_element(self):
        if self.aKnoten:                                # wenn Anfangsknoten vorhanden
            self.aKnoten.erstes_element()               # dann erstes_element() ausführen
        else:
            print("Die Liste hat keine Knoten!")        # ansonsten: Listenlänge=0 ausgeben
        
        
if __name__ == '__main__':          # wenn Hauptprogramm gestartet
    l=Liste()                       # dann Liste l mit verschiedenen Knoten erstellen
    l.einfügen("Michael")
    l.einfügen("Maximilian")
    l.einfügen("Alexander")
    l.einfügen("Daniel")
