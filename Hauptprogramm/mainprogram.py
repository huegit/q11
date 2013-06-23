# Hauptprogramm
# 07.06.2013
# K = Kontinent, L = Land, S = Spieler, A = Armee

import random
import socket

class Kontinent():
    "Konstruktor: Name, Wert, Länder inc."
    def __init__(self, name, wert, listeInklusive=[], laenderzahl=None):
        self.name           = name              # Name des K
        self.wert           = wert              # Wertigkeit des K
        self.listeInklusive = listeInklusive    # Liste der benötigten L
        self.laenderzahl    = laenderzahl       # Anzahl der benötigten L

    def __repr__(self):
        return self.name        # für Ausgabe         
                                                        
    def __str__(self):                                  
        return self.name        # für Ausgabe
    
class Land():
    "Konstruktor: Name, Kontinent"
    def __init__(self, name, kontinent, pos1=None,
                 pos2=None, pos3=None, pos4=None, pos5=None):
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

class Spieler():
    "Konstruktor: Name"
    def __init__(self, name, listeLaender=[], listeKontinente=[], listeKarten=[]):
        self.name             = name            # Name des S
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

        armeen = laenderarmeen + kontinentarmeen # K A + L A = A ges
            
        print(armeen)

    def karte_bekommen(self):   # Zufallskarte bekommen

        r = random.choice(["Reiter", "Soldat", "Kanone"])
        self.listeKarten.append(r)

    def karten_eintauschen(self):   # tausche Karten gegen A

        kanone = self.listeKarten.count("Kanone")   # zählt Anzahl Kanonen
        reiter = self.listeKarten.count("Reiter")   # zählt Anzahl Reiter
        soldat = self.listeKarten.count("Soldat")   # zählt Anzahl Soldaten
        armeen = 0      # def Armeen
        grund  = " "    # def Grund

        print("Du hast",kanone,"Kanonen",reiter,"Reiter",soldat,"Soldaten") # Gibt Anzahl der Karten aus

        if len(self.listeKarten) < 5:   # wenn weniger als 5 Karten

            frage = input("Möchtest du Karten eintauschen (y/n)?")  # Karten tauschen?

            if frage == "y":    # wenn ja

                if kanone >= 1 and reiter >= 1 and soldat >= 1: # wenn jeweils eine Karte
                    grund  = "drei unterschiedliche Figuren"
                    armeen = 10                                 # dann 10 Armeen
                    self.listeKarten.remove("Kanone")           # Kanone, Reiter, Kanone entfernen 
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Soldat")

                if kanone >= 3 and reiter <= 2 and soldat <= 0\
                   or kanone >= 3 and reiter <= 0 and soldat <= 2:  # wenn 3*Kanone
                    grund  = "drei Kanonen"
                    armeen = 8                                      # dann 8 Armeen
                    self.listeKarten.remove("Kanone")               # 3*Kanone entfernen
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")

                if kanone <= 2 and reiter >= 3 and soldat <= 0\
                   or kanone <= 0 and reiter >= 3 and soldat <= 2:  # wenn 3*Reiter
                    grund  = "drei Reiter"
                    armeen = 6                                      # dann 6 Armeen
                    self.listeKarten.remove("Reiter")               # 3*Reiter entfernen
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")

                if kanone <= 2 and reiter <= 0 and soldat >= 3\
                   or kanone <= 0 and reiter <= 2 and soldat >= 3:  # wenn 3*Soldat
                    grund  = "drei Soldaten"
                    armeen = 4                                      # dann 4 Armeen
                    self.listeKarten.remove("Soldat")               # 3*Soldat entfernen
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")

                else:
                    if armeen == 0:                                 # wenn keine A bekommen weil nicht mögl
                        print("Du kannst leider nichts eintauschen")# Ausgabe nicht mögl
                        return                                      # abbruch der Funktion
    
                print("Du hast",armeen,"Armeen für",grund,"bekommen")   # Ausgabe wieviele A + Grund

            if frage == "n":    # wenn nein

                print("Du hast keine Karten eingetauscht")  # keine Karten eingetauscht
                return                                      # Abbruch der Fkt

        else:           # mehr als 5 Karten: automatisches Eintauschen, genauso wie oben
            
            if kanone >= 1 and reiter >= 1 and soldat >= 1:
                    grund  = "drei unterschiedliche Figuren"
                    armeen = 10
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Soldat")

            if kanone >= 3 and reiter <= 2 and soldat <= 0\
               or kanone >= 3 and reiter <= 0 and soldat <= 2:
                    grund  = "drei Kanonen"
                    armeen = 8
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")
                    self.listeKarten.remove("Kanone")

            if kanone <= 2 and reiter >= 3 and soldat <= 0\
                or kanone <= 0 and reiter >= 3 and soldat <= 2:
                    grund  = "drei Reiter"
                    armeen = 6
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")
                    self.listeKarten.remove("Reiter")

            if kanone <= 2 and reiter <= 0 and soldat >= 3\
                or kanone <= 0 and reiter <= 2 and soldat >= 3:
                    grund  = "drei Soldaten"
                    armeen = 4
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")
                    self.listeKarten.remove("Soldat")

            print("Du hast",armeen,"Armeen für",grund,"bekommen")

    def land_erobern(self):     # Unfertige Methode (hier hinzufügen versch. L)

        # hinzufügen aller vorhandenen L

        self.listeLaender.append(hawaii)
        self.listeLaender.append(neuguinea)
        #self.listeLaender.append(balkan)
        self.listeLaender.append(westaustralien)
        self.listeLaender.append(madagaskar)
        self.listeLaender.append(indonesien)

        # Karten bekommen

        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()
        self.karte_bekommen()

        print(self.listeKarten)

        # Nach hinzufügen des/der L wird listeLaender nach K sortiert
        
        self.listeLaender.sort(key=self.sort_l)

    def sort_l(self, c):        # Sortiermethode, gibt K des L zurück
        
        return c.kontinent

    def kontinent_bekommen(self):       # Methode die prüft, ob Spieler neuen K bekommt

        zaehler = 0     # definition Zähler
        index = risk.listeKontinente[zaehler]   # index = aktueller Kontinent den es zu prüfen gilt

        for i in self.listeLaender:     # iteriert Liste L mit i

            if len(risk.listeKontinente) >= zaehler:    # wenn Länge der Liste kleiner als Zähler

                if i.kontinent == index.name:       # wenn name = kontinent
                    index.listeInklusive.remove(i)  # aktuelles L i wird aus der Liste der L von K entfernt
                    print(i)
                    
                    if len(index.listeInklusive) == 0:      # wenn Liste der Länder leer ist
                        self.listeKontinente.append(index)  # Liste der K von S wird um aktuellen K erweitert
                        print("2")
                        zaehler += 1
                        
            for n in self.listeLaender:                     # Problem: Methode bricht ab bzw. geht nicht alle K durch                                  
                if n.kontinent == index.name and index.listeInklusive.count(n) != 0: 
                       index.listeInklusive.append(n)
                       print(index.listeInklusive,"1")

                       if len(index.listeInklusive) == index.laenderzahl:
                          zaehler += 1

class Controller():     # Controllerklasse wird bestimmt
    "Konstruktor"
    def __init__(self, listeSpieler=[], spielbrett=[], listeLaenderkarten=[], listeAuftragskarten=[],
                 listeWuerfelRot=[], listeWuerfelBlau=[], listeSpielsteine=[], listeKontinente=[]):
        self.listeSpieler        = listeSpieler         # Liste der S
        self.spielbrett          = spielbrett           # bisher unnütz
        self.listeLaenderkarten  = listeLaenderkarten   # bisher unnütz
        self.listeAuftragskarten = listeAuftragskarten  # bisher unnütz
        self.listeWuerfelRot     = listeWuerfelRot      # bisher unnütz
        self.listeWuerfelBlau    = listeWuerfelBlau     # bisher unnütz
        self.listeSpielsteine    = listeSpielsteine     # bisher unnütz
        self.listeKontinente     = listeKontinente      # Liste aller K im Spiel

    def sort_k(self, c):    # Sortiermethode, gibt Namen zurück
        return c.name

    def spielstart(self):   # Spielroutine

        self.listeKontinente.sort(key=self.sort_k)      # Kontinente werden nach Name sortiert

        while True:         # Anfangsschleife für S hinzufügen

            spielername = input("Spieler hinzufügen:")      # input: S hinzufügen
            self.listeSpieler.append(Spieler(spielername))  # Liste der S wird um "spielername" erweitert
            ende = input("Spiel starten (y/n)?:")           # Soll das Spiel beginnen?
            
            if ende == "y":     # wenn y dann break => Spiel beginnt
                break
        

        zaehler = 0     # definition Zähler
        
        while True:         # Hauptschleife, Spiel an sich
            
            zaehler = zaehler+1     # Zähler + 1

            aktuellerSpieler = self.listeSpieler[zaehler%(len(self.listeSpieler))-1]    # aktueller S wird bestimmt
            if zaehler == 1:                            # erste Runde
                aktuellerSpieler.land_erobern()         # land_erobern wird ausgeführt (Testzweck)
                aktuellerSpieler.kontinent_bekommen()   # kontinent_bekommen wird ausgeführt (fest)
            print(aktuellerSpieler)                     # Ausgabe aktueller S
            aktuellerSpieler.armeen_bekommen()          # aktueller S bekommt A
            aktuellerSpieler.karten_eintauschen()       # aktueller S kann Karten tauschen ( in entwicklung)

            if zaehler == 6:                            # nach 6 Spielzügen bricht das Spiel ab
                break

            

            

            
# bei Start:        
        
if __name__ == "__main__":
    
    # Controller mit dem Namen "risk" wird erstellt

    risk = Controller()

    # L werden erstellt
    
    indonesien = Land("Indonesien", "Australien")
    neuguinea  = Land("Neu-Guinea", "Australien")
    westaustralien = Land("West-Australien", "Australien")
    madagaskar = Land("Madagaskar", "Afrika")
    balkan     = Land("Balkan", "Afrika")
    hawaii     = Land("Hawaii", "Nordamerika")

    # K werden erstellt
    
    afrika     = Kontinent("Afrika", 3, [madagaskar, balkan], 2)
    australien = Kontinent("Australien", 2, [indonesien, neuguinea, westaustralien], 3)
    nordamerika= Kontinent("Nordamerika", 5, [hawaii], 1)

    # K werden eingefügt
    
    risk.listeKontinente.append(australien)
    risk.listeKontinente.append(nordamerika)
    risk.listeKontinente.append(afrika)

    # Spiel wird gestartet
    
    risk.spielstart()
    
