# Programm zur Serversuche bzw. zum verschicken der Spieledaten
# 29.06.2013
# by Alexander Epple


from socket import *        # Socket Server importieren
import threading            # Threading importieren, mögl. später wichtig

MYPORT = 50000              # Port def
client_new= None            # client_new def

class Server(threading.Thread):
    "Klasse Server, kann neue Clients annehmen"
    def run(self):
        "Start() Methode"
        addr = ("", MYPORT)                     # Addresse wird bestimmt, keine IP und MYPORT
        server = socket(AF_INET, SOCK_DGRAM)    # Server wird geöffnet
        server.bind(addr)                       # wird an addr gebunden
        
        while True:                                     # Schleife
            daten, address = server.recvfrom(1024)      # Empfängt Daten
            
            print(address[0], daten.decode("UTF-8"))    # Gibt sie aus
            
            global client_new       # client_new wird zur Vefügung gestellt
            client_new = address    # wird geändert zur letzten Empfangsaddresse
            
            if daten.decode("UTF-8").split()[0] == "conreq":    # Wenn erste Daten conreq am Anfang enthalten
                self.firststrike()                              # Methode firststrike() wird ausgeführt 

    def firststrike(self):
        "Wird nur bei neuem Client ausgeführt"
        server = socket(AF_INET, SOCK_DGRAM)    # Server wird geöffnet
        antwort = "12hnisa".encode("UTF-8")     # def Antwort
        server.sendto(antwort, (client_new))    # Antwort wird an letzte Empfangsaddresse geschickt

def serverstart():
    "Startet neuen Server der klasse Server"
    server = Server()
    server.start()

def serversuche():
    "Sucht Server bzw erstellt neuen"
    s = socket(AF_INET, SOCK_DGRAM)                 # Server wird geöffnet
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)    # Option Broadcast wird ausgewählt
    s.settimeout(3)                                 # Timeout wird festgelegt

    print("Versuche Server zu finden...")

    myname = input("Name:").encode("UTF-8")             # Name wird abgefragt
    connector = "conreq ".encode("UTF-8")               # erste Anfrage enthält conreq, siehe oben
    s.sendto(connector+myname, ("<broadcast>", MYPORT)) # erste Anfrage, conreq + Name wird 
                                                        # an alle IPs im Netzwerk über MYPORT geschickt
    try:
        antwort, address = s.recvfrom(1024)     # sollte etwas zurückkommen (binnen 3 sec.)
        ip = address[0]                         # wird die IP gespeichert
        print("Server gefunden:", address[0])   # ausgegeben
        s.close                                 # der Suchserver wird geschlossen

        while True:
            server = socket(AF_INET, SOCK_DGRAM)     # ein neuer Server geöffnet
            raw = input("Nachricht:").encode("UTF-8")# man kann eine Nachricht schicken
            server.sendto(raw, (ip, MYPORT))         # wird an gespeicherte IP gesendet

    except timeout:                 # wenn nach 3 sec kein Server gefunden wurde
        print("Kein Server gefunden, erstelle neuen auf Port", MYPORT)
        serverstart()               # wird ein neuer erstellt

    s.close                 # der Server zur Suche wird geschlossen

if __name__ == "__main__":  # Hauptprogramm

    serversuche()       # Serversuche wird ausgeführt
