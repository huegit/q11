# Q11-Projekt: "Risiko"
# Hauptprogramm, enthält alle anderen Bestandtteile
# aktualisiert am 04.07.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee
# by Alexander Epple

from random import *                    # Importiert Zufallsmodul
from socket import *                    # Importiert Servermodul
from visual import *                    # Importiert 3D Grafik
from visual.controls import *           # Importiert Eingabe
from spielbrett import Spielbrett       # Importiert die Klasse Spielbrett
from spielbrett import Konsole          # Importiert die Klasse Konsole (GUI)
from spielsteine import platzieren      # Importiert die Funktion platzieren()
from wuerfel import Wuerfel             # Importiert die Würfel (wird vill. gebraucht)

class Kontinent():
    "Konstruktor: Name, Wert, Länder inc."
    def __init__(self, name, wert, laenderzahl=None):
        self.name           = name              # Name des K
        self.wert           = wert              # Wertigkeit des K
        self.laenderzahl    = laenderzahl       # Anzahl der benötigten L

    def __repr__(self):
        return self.name        # für Ausgabe         
                                                        
    def __str__(self):                                  
        return self.name        # für Ausgabe
    
class Land():
    "Konstruktor: Name, Kontinent"
    def __init__(self, name, kontinent, pos1,
                 pos2, pos3, pos4, pos5):
        self.name      = name       # Name des L
        self.kontinent = kontinent  # K der zu diesem L gehört
        self.pos1      = pos1       # festlegen der 5 Figurenpositionen
        self.pos2      = pos2
        self.pos3      = pos3
        self.pos4      = pos4
        self.pos5      = pos5

    def __repr__(self):
        return self.name    # für Ausgabe              
                                                        
    def __str__(self):                                  
        return self.name    # für Ausgabe

class Figur():
    "Kontruktor: Wert, Spieler+Farbe"
    def __init__(self, wert, spieler, farbe):
        self.wert    = wert     # Wert der Figur
        self.spieler = spieler  # Zugehöriger S
        self.farbe   = farbe    # Farbe des S

class Spieler():
    "Konstruktor: Name"
    def __init__(self, name, armeen=0, listeLaender=[], listeKontinente=[], listeKarten=[]):
        self.name             = name            # Name des S
        self.armeen           = armeen          # A des S
        self.listeLaender     = listeLaender    # Liste der L von S
        self.listeKontinente  = listeKontinente # Liste der K von S
        self.listeKarten      = listeKarten     # Liste der Karten von S

    def __repr__(self):
        return self.name    # für Ausgabe                          
                                                        
    def __str__(self):                                  
        return self.name    # für Ausgabe

    def armeen_bekommen(self):
        
        laenderarmeen   = round(len(self.listeLaender)/3, 0)    # L/3, abrunden
        
        if laenderarmeen <= 3.0:    # nie weniger als 3 A
            laenderarmeen = 3.0

        kontinentarmeen = 0     # K A = 0, definition von K A
        
        for i in self.listeKontinente:
            kontinentarmeen += i.wert   # iteriert die Liste K und addiert Wertigkeit

        self.armeen += laenderarmeen + kontinentarmeen # K A + L A = A ges

        risk.gui.del_old()                      # Entfernt alte A Anzeige
        risk.gui.meine_armeen(str(self.armeen)) # Erstellt neue anhand der zusätzlichen A

    def karte_bekommen(self):   # Zufallskarte bekommen
        "Methode um zufällig Karte zu bekommen"

        r = choice(["Reiter", "Soldat", "Kanone"])  # zufällige Karte
        self.listeKarten.append(r)                  # wird an Liste der Karten angehängt

    def würfeln(self):
        "schnelle Würfelmethode"
        
        r = random.choice([1,2,3,4,5,6])            # zufällige Zahl

    def karten_eintauschen(self):   # tausche Karten gegen A
        "Methode um Karten einzutauschen"

        kanone = self.listeKarten.count("Kanone")   # zählt Anzahl Kanonen
        reiter = self.listeKarten.count("Reiter")   # zählt Anzahl Reiter
        soldat = self.listeKarten.count("Soldat")   # zählt Anzahl Soldaten
        old_armeen = self.armeen      # def A vor eintauschen
        grund  = " "    # def Grund

        risk.gui.karte_anzeigen(str(kanone),str(reiter),str(soldat))
        print(kanone," Kanonen",reiter," Reiter",soldat," Soldaten")

        if len(self.listeKarten) < 5:   # wenn weniger als 5 Karten

            frage = input("Möchtest du Karten eintauschen (y/n)?")  # Karten tauschen?

            if frage == "y":    # wenn ja

                if kanone >= 1 and reiter >= 1 and soldat >= 1: # wenn jeweils eine Karte
                    grund  = "drei unterschiedliche Figuren"
                    self.armeen += 10                           # dann 10 Armeen
                    self.listeKarten.remove("Kanone")           # Kanone, Reiter, Kanone entfernen 
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Soldat")

                if kanone >= 3 and reiter <= 2 and soldat <= 0\
                   or kanone >= 3 and reiter <= 0 and soldat <= 2:  # wenn 3*Kanone
                    grund  = "drei Kanonen"
                    self.armeen += 8                                # dann 8 Armeen
                    self.listeKarten.remove("Kanone")               # 3*Kanone entfernen
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")

                if kanone <= 2 and reiter >= 3 and soldat <= 0\
                   or kanone <= 0 and reiter >= 3 and soldat <= 2:  # wenn 3*Reiter
                    grund  = "drei Reiter"
                    self.armeen += 6                                # dann 6 Armeen
                    self.listeKarten.remove("Reiter")               # 3*Reiter entfernen
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")

                if kanone <= 2 and reiter <= 0 and soldat >= 3\
                   or kanone <= 0 and reiter <= 2 and soldat >= 3:  # wenn 3*Soldat
                    grund  = "drei Soldaten"
                    self.armeen += 4                                # dann 4 Armeen
                    self.listeKarten.remove("Soldat")               # 3*Soldat entfernen
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")

                else:
                    if old_armeen == self.armeen:                   # wenn keine A bekommen weil nicht mögl
                        print("Du kannst leider nichts eintauschen")# Ausgabe nicht mögl
                        return                                      # abbruch der Funktion
    
                print("Du hast",(self.armeen-old_armeen),"Armeen für",grund,"bekommen")   # Ausgabe wieviele A + Grund

            if frage == "n":    # wenn nein

                print("Du hast keine Karten eingetauscht")  # keine Karten eingetauscht
                return                                      # Abbruch der Fkt

        else:           # mehr als 5 Karten: automatisches Eintauschen, genauso wie oben
            
            if kanone >= 1 and reiter >= 1 and soldat >= 1:
                    grund  = "drei unterschiedliche Figuren"
                    self.armeen += 10
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Soldat")

            if kanone >= 3 and reiter <= 2 and soldat <= 0\
               or kanone >= 3 and reiter <= 0 and soldat <= 2:
                    grund  = "drei Kanonen"
                    self.armeen += 8
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")

            if kanone <= 2 and reiter >= 3 and soldat <= 0\
                or kanone <= 0 and reiter >= 3 and soldat <= 2:
                    grund  = "drei Reiter"
                    self.armeen += 6
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")

            if kanone <= 2 and reiter <= 0 and soldat >= 3\
                or kanone <= 0 and reiter <= 2 and soldat >= 3:
                    grund  = "drei Soldaten"
                    self.armeen += 4
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")

            risk.gui.karte_eintauschen(grund, str(self.armeen-old_armeen))  # Gibt Daten (Grund, Anzahl der A) an GUI weiter
            risk.gui.del_old()                                              # diese entfernt alte A Anzeige
            risk.gui.meine_armeen(str(self.armeen))

    def land_erobern(self):     # Unfertige Methode (hier hinzufügen versch. L)
        "Methode um L zu bekommen"

        # hinzufügen aller vorhandenen L

        self.listeLaender.append(venezuela)
        self.listeLaender.append(brasilien)
        self.listeLaender.append(peru)
        self.listeLaender.append(argentinien)
        self.listeLaender.append(ostaustralien)
        self.listeLaender.append(westaustralien)
        self.listeLaender.append(indonesien)
        self.listeLaender.append(neuguinea)

        # Karten bekommen ( fünf mal )

        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()

        print(self.listeKarten)

        # Nach hinzufügen des/der L wird listeLaender nach K sortiert
        
        self.listeLaender.sort(key=self.sort_l)

    def armeen_setzten(self, armeen, land):
        "Methode um A in Länder zu setzten"
        
        index   = self.listeLaender.index(land)     # L wird bestimmt (erstes vorkommendes Element in listeLaender)
        l = self.listeLaender[index]                # Daten von L werden gespeichert
        platzieren(armeen, l.pos1, l.pos2, l.pos3, l.pos4, l.pos5, color.red)   # und zum platzieren verwendet (Positionen)

    def sort_l(self, c):
        "Sortiermethode, gibt K des L zurück"
        
        return c.kontinent  # gibt K des L zurück, für korrekte Sortierung

    def kontinent_bekommen(self):
        "Methode die prüft, ob S neuen K bekommt"

        zaehler = 0     # definition Zähler

        while zaehler < len(risk.listeKontinente):      # solange der Zähler kleiner als die Anzahl der K ist

            index = risk.listeKontinente[zaehler]   # index = aktueller Kontinent den es zu prüfen gilt
            
            if sum(p.kontinent == index.name for p in self.listeLaender) == index.laenderzahl:
                # Wenn die Anzahl der L mit dem aktuellem K gleich der laenderanzahl des aktuellen k ist
                self.listeKontinente.append(index)                  # so wird er annektiert
                risk.gui.kontinent_bekommen(index.name)             # an die GUI geschickt die ihn anzeigt
                zaehler += 1                                        # Zähler wird hochgestuft
            elif sum(p.kontinent == index.name for p in self.listeLaender) != index.laenderzahl: # wenn dem nicht so ist
                zaehler += 1                                        # Zähler wird hochgestuft

class Controller():     # Controllerklasse wird bestimmt
    "Konstruktor"
    def __init__(self, karte=None, gui=None, listeSpieler=[], listeKontinente=[]):
        self.karte               = karte                # Zugehörige Karte
        self.gui                 = gui                  # Overlay, GUI
        self.listeSpieler        = listeSpieler         # Liste der S
        self.listeKontinente     = listeKontinente      # Liste aller K im Spiel

    def sort_k(self, c):
        "Sortiermethode, gibt Namen zurück"
        return c.name
                
    def spielstart(self):   # Spielroutine
        "Hauptmethode, steuert Spiel und Zugroutinen"
        c = controls(text="Risiko GUI")
        
        self.listeKontinente.sort(key=self.sort_k)      # Kontinente werden nach Name sortiert

        while True:         # Anfangsschleife für S hinzufügen
            try:            # veruche folgendes

                    def spieler_einfuegen(event):
                        "Methode um S einzufügen"
                        name = spielername.get() # Speichere aktuelle Eingabe unter Name
                        
                        if name == "":          # Wenn keine Eingabe
                            spielerl.insert(END, "Bitte Name eingeben!\n")  # bitte Eingabe erscheint im Fenster
                            return              # Ende der Fkt
                        if name.count(" ") == len(name):    # Wenn nur Leerzeichen (HaHaHa)
                            spielerl.insert(END, "Bitte gültigen Namen eingeben!\n")    # bitte korrekte Eingabe erscheint im Fenster
                            spielername.delete(0,END)       # Eingabe wird entfernt
                            return              # Ende der Fkt.
                        
                        spielername.delete(0,END)   # Eingabe wird entfernt
                        self.listeSpieler.append(Spieler(name)) # wird in listeSpieler integriert
                        spielerl.insert(END, "Spieler "+name+" hinzugefügt!\n") # Erfolgreich eingefügt erscheint im Fenster

                    def weiter():
                        "Wenn keine Spieler mehr eingefügt werden sollen"
                        if len(self.listeSpieler) > 0:  # wenn mehr als ein S vorhanden sind
                            root.destroy()              # Fenster wird zerstört (sehr brutal)
                        else:                           # wenn kein S vorhanden
                            spielerl.insert(END, "Vor Start bitte Name eingeben!\n")    # Bitte S hinzufügen erscheint im Fenster

                    Label(root, text="Name eingeben:").grid(row=1, sticky=W)    # Schriftzug neben dem Eingabefeld
                    spielerl = Text(root, height=5, width=40)                   # Ausgabefenster
                    spielerl.grid(row=0)                                        # wird positioniert
                    spielername = Entry(root)                                   # Eingabefeld
                    spielername.bind("<Return>", spieler_einfuegen)             # wird an Eingabetaste gebunden
                    spielername.grid(row=1, sticky=E)                           # und positioniert

                   
                    starten = Button(root, text="Spiel starten", command = weiter, width=20).grid(row=2, sticky=W)  # Startbutton, ist an weiter() gebunden
                    ende = Button(root, text="Spiel beenden", command = exit, width=20).grid(row=2, sticky=E)       # Endebutton, beendet Spiel

                    root.mainloop()     # Fenster wird erstellt (mit allen Knöpfen Eingabe/Ausgabefeldern etc. , muss immer am Ende stehen
                    
            except TclError:            # wenn Fehler das Fenster nicht mehr existiert (nach Fenster zerstören, siehe weiter())
                    break               # breche Schleife ab, gehe weiter im Programm
        

        zaehler = 0     # definition Zähler
        
        self.karte = Spielbrett()   # Spielbrett ist karte des Controllers
        self.gui   = Konsole()      # Konsole ist GUI des Controllers
        
        
        while True:         # Hauptschleife, Spiel an sich

            self.karte.animation()  # coole Zoom/Schwenkanimation
            
            zaehler = zaehler+1     # Zähler + 1

            aktuellerSpieler = self.listeSpieler[zaehler%(len(self.listeSpieler))-1]    # aktueller S wird bestimmt
            if zaehler == 1:                            # erste Runde
                aktuellerSpieler.land_erobern()         # land_erobern wird ausgeführt (Testzweck)
                self.karte.land_waehlen()               # Methode um bestimmtes L auszuwählen
                aktuellerSpieler.kontinent_bekommen()   # kontinent_bekommen wird ausgeführt (fest)
                aktuellerSpieler.armeen_setzten(29, brasilien)  # 29 Figuren werden in Brasilien positioniert
                aktuellerSpieler.armeen_setzten(100, neuguinea) # 100 Figuren werden in Neu-Guinea positioniert
            print(aktuellerSpieler)                     # Ausgabe aktueller S
            aktuellerSpieler.armeen_bekommen()          # aktueller S bekommt A
            aktuellerSpieler.karten_eintauschen()       # aktueller S kann Karten tauschen ( in entwicklung)

            self.karte.animation_back()                 # coole Animation rückwärts

            if zaehler == 6:                            # nach 6 Spielzügen bricht das Spiel ab
                break
            
# bei Start:        
        
if __name__ == "__main__":

    
    # Controller mit dem Namen "risk" wird erstellt
    
    risk = Controller()

    # L werden erstellt
    
    groenland=Land("Grönland","Amerika",(-15.1432182270731, 35.1475467776392, 0), (-17.9825716446493, 40.3545907446969, 0), (-24.1345040493978, 32.0706571607415, 0), (-6.6251579743445, 45.5616347117545, 0), (-6.38854518954648, 37.9877525778525, 0))
    ontario=Land("Ontario","Amerika", (-27.6836958213681, 23.0766721267328, 0), (-29.5765980997522, 25.6801941102616, 0), (-26.26401911258, 24.7334588435239, 0), (-25.7907935429839, 16.9228928929374, 0), (-22.0049889862156, 16.9228928929374, 0))
    quebeck=Land("Quebeck","Amerika", (-17.5093460750533, 20.7098339598884, 0), (-17.9825716446493, 23.7867235767861, 0), (-14.9066054422751, 21.1832015932573, 0), (-15.8530565814672, 16.4495252595685, 0), (18.4557972142454, 15.5027899928308, 0))
    oststaaten=Land("Oststaaten","Amerika", (-32.4159515173284, 7.45554022555983, 0), (-29.5765980997522, 11.0057974758264, 0), (-29.5765980997522, 14.556054726093, 0), (-35.7285305045007, 6.98217259219095, 0), (-29.8132108845502, 7.21885640887539, 0))
    mittelamerika=Land("Mittelamerika","Amerika", (-40.697398985259, 1.53844480844885, 0), (-40.460786200461, -1.06507717507998, 0), (-36.9115944284908, -3.19523152523993, 0), (-44.2465907572293, 7.21885640887539, 0), (-40.460786200461, 6.74548877550651, 0))
    weststaaten=Land("Weststaaten","Amerika", (-41.4072373396531, 11.7158489258797, 0), (-38.0946583524808, 11.2424812925109, 0), (-45.6662674660174, 11.7158489258797, 0), (-45.1930418964214, 17.3962605263063, 0), (38.8044967068749, 16.9228928929374, 0))
    alberta=Land("Alberta","Amerika", (-38.8044967068749, 20.9465177765729, 0), (-42.5903012636432, 22.6033044933639, 0), (-39.750947846067, 27.1002970103683, 0), (-34.7820793653086, 20.473150143204, 0), (-34.3088537957126, 26.8636131936838, 0))
    nordwestterritorium=Land("Nordwest-Territorium","Amerika", (-34.7820793653086, 34.9108629609548, 0), (-38.3312711372789, 35.6209144110081, 0), (-26.973857466974, 37.9877525778525, 0), (-30.0320544771298, 41.023028714996, 0), (-34.1215257250794, 43.5789806598556, 0))
    alaska=Land("Alaska","Amerika", (-43.322836032966, 33.6107680749033, 0), (-42.0448762679818, 31.5660065190156, 0), (-43.322836032966, 27.7320786017263, 0), (-44.6007957979503, 38.4670767701365, 0), (-42.3004682209786, 40.7674335205101, 0))
    brasilien=Land("Brasilien","Südamerika", (-27.9943460056803, -24.5804013708412, 0), (-24.9217958343251, -25.263190297809, 0), (-31.4082906405193, -27.9943460056803, 0), (-26.2873736882607, -16.3869342472275, 0), (-34.4808408118745, -16.3869342472275, 0))
    argentinien=Land("Argentinien","Südamerika", (-38.5775743736813, -36.187813129294, 0), (-39.6017577641331, -32.7738684944549, 0), (-41.6501245450365, -40.2845466911009, 0), (-43.6984913259399, -43.357096862456, 0), (-40.9673356180687, -36.187813129294, 0))
    peru=Land("Peru","Südamerika", (-38.2361799101974, -23.2148235169056, 0), (-35.8464186658101, -28.6771349326481, 0), (-38.2361799101974, -22.8734290534217, 0), (-42.6743079354882, -21.84924566297, 0), (-43.357096862456, -16.0455397837436, 0))
    venezuela=Land("Venezuela", "Südamerika", (-33.4566574214228, -7.85207266012983, 0), (-30.0427127865837, -9.90043944103326, 0), (-39.943152227617, -11.6074117584528, 0), (-27.6529515421964, -12.2902006854206, 0), (-41.3087300815526, -12.9729896123884, 0))
    nordwestafrika=Land("Nordwestafrika","Afrika", (-10.2777506604518, -16.1712130463209, 0), (-12.5338422688436, -21.6869756357636, 0), (-5.76556744366808, -21.6869756357636, 0), (-13.5365496503511, -13.1626152702612, 0), (-9.2750432789443, -12.1597493449079, 0))
    kongo=Land("Kongo","Afrika", (0, -24.9462898931616, 0), (1.50406107226124, -23.6927074864701, 0), (-1.75473791763811, -24.1941404491467, 0), (-1.00270738150749, -27.9548876692213, 0), (1.00270738150749, -28.4563206318979, 0))
    suedafrika=Land("Südafrika","Afrika", (2.25609160839186, -35.9778150720472, 0), (-1.50406107226124, -31.4649184079576, 0), (6.01624428904495, -31.9663513706343, 0), (0, -37.2313974787387, 0), (4.01082952602997, -37.2313974787387, 0))
    madagaskar=Land("Madagaskar","Afrika", (11.0297811965824, -35.2256656280323, 0), (11.2804580419593, -33.2199337773258, 0), (12.0324885780899, -31.2142019266193, 0), (13.5365496503511, -36.2285315533855, 0), (14.0379033411049, -33.2199337773258, 0))
    ostafrika=Land("Ostafrika","Afrika", (6.01624428904495, -22.6898415611169, 0), (4.51218321678371, -25.9491558185149, 0), (7.77098220668306, -25.4477228558383, 0), (2.25609160839186, -17.926228415689, 0), (6.01624428904495, -17.6755119343507, 0))
    aegypten=Land("Ägypten","Afrika", (-0.752030536130619, -15.1683471209676, 0), (-4.51218321678371, -13.9147647142761, 0), (-2.50676845376873, -12.6611823075846, 0), (3.00812214452247, -10.9061669382164, 0), (4.76286006216058, -13.1626152702612, 0))
    ukraine=Land("Ukraine", "Europa",(13.9971730028401, 23.5562179803895, 0), (9.21765051406545, 18.093906564647, 0), (5.8037058792264, 21.84924566297, 0), (8.87625605058155, 6.1451003427103, 0), (3.41394463483906, 7.85207266012983, 0))
    skandinavien=Land("Skandinavien", "Europa", (1.02418339045172, 24.9217958343251, 0), (1.79945190030866, 17.7146811825506, 0), (1.79945190030866, 17.7146811825506, 0), (-5.20893971141981, 12.9781354118152, 0), (-0.852371952777787, 13.7359827351328, 0))
    island=Land("Island", "Europa", (-0.284123984259262, 13.7359827351328, 0), (-3.12536382685189, 29.650776524804, 0), (-7.67134757500008, 29.4613146939745, 0), (-8.05017955401244, 25.6720780773862, 0), (-5.20893971141981, 24.7247689232391, 0))
    großbritannien=Land("Großbritannien", "Europa", (-2.93594783734571, 25.4826162465568, 0), (-8.42901153302478, 11.6519025960092, 0), (-8.05017955401244, 8.43105147190911, 0), (-13.1644112706792, 8.05212781025028, 0), (-10.5125874175927, 5.39966217863842, 0))
    westeuropa=Land("Westeuropa", "Europa", (-7.48193158549391, 5.96804767112668, 0), (-9.75492345956801, 1.61042556205006, 0), (-6.34543564845686, 0.852578238732382, 0), (-9.94433944907418, -4.07342936283249, 0), (-11.2702513756174, -7.48374231776202, 0))
    suedeuropa=Land("Südeuropa", "Europa", (-14.3009072077162, -3.88396753200308, 0), (0.284123984259262, -5.77858584029726, 0), (2.36769986882719, 1.98934922370889, 0), (2.55711585833336, -1.98934922370889, 0), (-3.50419580586424, 0.852578238732382, 0))
    mitteleuropa=Land("Mitteleuropa", "Europa", (-0.284123984259262, 1.98934922370889, 0), (-0.0947079947530875, 9.75728428771504, 0), (-3.69361179537041, 9.56782245688562, 0), (-5.58777169043216, 4.83127668615017, 0), (-0.852371952777787, 3.69450570117366, 0))
    mittlererosten=Land("MittlererOsten", "Asien",( 6.42772915652102, -1.8794590012399, 0), (9.59214966434676, -6.0340525829281, 0), (13.5476752991289, -6.4297281621365, 0), (9.19659710086854, -11.7713484814499, 0), (12.5587938904334, -13.5518885878877, 0))
    afghanistan=Land("Afghanistan", "Asien", (17.305424652172, 1.6816212116357, 0), (16.7120958069547, 9.5951327958037, 0), (21.8542791321715, 4.0556746868861, 0), (17.7009772156502, -2.0772967908441, 0), (12.9543464539116, 0.0989188948021, 0))
    indien=Land("Indien", "Asien", (20.4698451599977, -11.3756729022415, 0), (23.6342656678234, -7.6167548997617, 0), (20.8653977234759, -15.5302664839297, 0), (17.5032009339111, -10.9799973230331, 0), (17.5032009339111, -7.6167548997617, 0))
    china=Land("China", "Asien",(27.5897913026056, -3.0664857388651, 0), (23.0409368226061, -1.6816212116357, 0), (27.3920150208665, 2.0772967908441, 0), (33.720856036518, -2.2751345804483, 0), (25.0186996399972, 1.0881078428231, 0))
    siam=Land("Siam","Asien", (29.3697778382576, -8.2102682685743, 0), (28.3808964295621, -12.3648618502625, 0), (27.3920150208665, -9.3972950061995, 0), (30.160882965214, -16.5194554319507, 0), (28.3808964295621, -8.8037816373869, 0))
    mongolei=Land("Mongolei", "Asien",( 33.1275271913006, 3.2643235284693, 0), (29.1720015565185, 5.8362147933239, 0), (32.3364220643442, 6.6275659517407, 0), (35.50084257217, 6.4297281621365, 0), (36.6875002626046, 1.0881078428231, 0))
    ural=Land("Ural", "Asien",(20.8653977234759, 19.0913466968053, 0), (23.6342656678234, 9.5951327958037, 0), (18.2943060608675, 13.7497263774919, 0), (20.8653977234759, 30.7637762834531, 0), (23.4364893860843, 25.2243181745355, 0))
    sibirien=Land("Sibirien", "Asien", (28.5786727113012, 19.0913466968053, 0), (27.5897913026056, 9.5951327958037, 0), (27.5897913026056, 27.2026960705775, 0), (30.7542118104313, 34.3248564963287, 0), (32.9297509095615, 28.5875605978069, 0))
    irkutsk=Land("Irkutsk", "Asien", (31.7430932191269, 9.9908083750121, 0), (35.1052900086917, 13.9475641670961, 0), (33.5230797547789, 19.8826978552221, 0), (38.6652630799957, 16.9151310111591, 0), (37.2808291078219, 20.4762112240347, 0))
    jakutien=Land("Jakutien", "Asien", (40.4452496156477, 25.8178315433481, 0), (35.1052900086917, 24.6308048057229, 0), (43.8074464052125, 31.1594518626615, 0), (42.818564996517, 22.2567513304725, 0), (39.4563682069521, 34.3248564963287, 0))
    kamtschatka =Land("Kamtschatka", "Asien", (45.1918803773863, 16.5194554319507, 0), (47.1696431947773, 20.6740490136389, 0), (39.0608156434739, 9.0016194269911, 0), (47.7629720399947, 23.2459402784935, 0), (47.7629720399947, 30.5659384938489, 0))
    japan =Land("Japan", "Asien", (44.9941040956472, 3.0664857388651, 0), (41.4341310243432, -1.8794590012399, 0), (46.3785380678209, 9.3972950061995, 0), (44.9941040956472, -1.0881078428231, 0), (47.1696431947773, 5.4405392141155, 0))
    indonesien =Land("Indonesien", "Australien", (37.8947854467135, -18.093906564647, 0), (30.3027074277503, -20.4985329103113, 0), (41.9340496727454, -15.1954298688377, 0), (34.3838801452924, -23.5580154342383, 0), (40.5056392216056, -21.5183604182869, 0))
    westaustralien =Land("Westaustralien", "Australien", (37.6488183193261, -34.1642215171854, 0), (39.0772287704659, -28.0452564693313, 0), (41.9340496727454, -31.1047389932584, 0), (36.2204078681864, -36.8157730379222, 0), (39.8934633139743, -36.6118075363271, 0))
    neuguinea =Land("Neuguinea", "Australien", (46.8314569337959, -22.5381879262626, 0), (42.9543428521309, -21.3143949166918, 0), (48.872043292567, -22.7421534278578, 0), (49.6882778360754, -25.3937049485945, 0), (43.158401488008, -23.5580154342383, 0))
    ostaustralien =Land("Ostaustralien", "Australien", (46.2192810261646, -31.5126699964486, 0), (43.3624601238851, -36.2038765331368, 0), (44.994929210902, -27.637325466141, 0), (48.872043292567, -31.7166354980438, 0), (47.4436328414272, -36.8157730379222, 0))

    # K werden erstellt
    
    afrika     = Kontinent("Afrika", 3, 6)
    australien = Kontinent("Australien", 2, 4)
    amerika    = Kontinent("Amerika", 5, 9)
    asien      = Kontinent("Asien", 7, 12)
    europa     = Kontinent("Europa", 5, 7)
    suedamerika= Kontinent("Südamerika", 2, 4)

    # K werden eingefügt
    
    risk.listeKontinente.append(australien)
    risk.listeKontinente.append(amerika)
    risk.listeKontinente.append(afrika)
    risk.listeKontinente.append(asien)
    risk.listeKontinente.append(europa)
    risk.listeKontinente.append(suedamerika)

    # Spiel wird gestartet

    risk.spielstart()
