# Q11-Projekt: "Risiko"
# Programm zur Serversuche bzw. zum verschicken der Spieledaten
# aktualisiert am 29.06.2013
# by Daniel Strobl, Michael Dörsam, Alexander Epple


from socket import *         # Socket Server importieren
from threading import Thread # Threading importieren, mögl. später wichtig

MYPORT = 50000               # Port def
client_new= None             # client_new def

class Server(Thread):
    "Klasse Server, kann neue Clients annehmen"
    def __init__(self):
        Thread.__init__(self)
        
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
        
class Client(Thread):                           # Der client
    "Klasse Client, kann an Server senden und empfangen"
    def __init__(self, ip, name):
        Thread.__init__(self)
        self.ip   = ip
        self.name = name
        
    def run(self):
        client = socket(AF_INET, SOCK_DGRAM)
        while True:
            self.schreiben()
            
    def schreiben(self):
        senden = (myname+":"+input("Nachricht:")).encode("UTF-8")
        self.client.sendto(senden, (self.ip, MYPORT))

    def send(string):
        self.client.sendto(string.encode("UTF-8"),(self.ip, MYPORT)
        

def serverstart():
    "Startet neuen Server der klasse Server"
    serverHost = Server()
    serverHost.start()

def clientstart(ip, name):
    "Startet Client der an Server gebunden ist"
    client1 = Client(ip, name)
    client1.start()

def serversuche():
    "Sucht Server bzw erstellt neuen"
    s = socket(AF_INET, SOCK_DGRAM)                 # Server wird geöffnet
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)    # Option Broadcast wird ausgewählt
    s.settimeout(1)                                 # Timeout wird festgelegt

    print("Versuche Server zu finden...")

    myname = input("Name:").encode("UTF-8")             # Name wird abgefragt
    connector = "conreq ".encode("UTF-8")               # erste Anfrage enthält conreq, siehe oben
    s.sendto(connector+myname, ("<broadcast>", MYPORT)) # erste Anfrage, conreq + Name wird 
                                                        # an alle IPs im Netzwerk über MYPORT geschickt
    try:
        antwort, address = s.recvfrom(1024)     # sollte etwas zurückkommen (binnen 3 sec.)
        ip = address[0]                         # wird die IP gespeichert
        s.close                                 # der Suchserver wird geschlossen
        if antwort.decode("UTF-8") == "12hnisa":
            print("Server gefunden:", ip)
            clientstart(ip, myname)
            
    except timeout:                 # wenn nach 3 sec kein Server gefunden wurde
        print("Kein Server gefunden, erstelle neuen auf Port", MYPORT)
        serverstart()               # wird ein neuer erstellt
        clientstart("127.0.0.1", myname)   # loopback client

    s.close                 # der Server zur Suche wird geschlossen

if __name__ == "__main__":  # Hauptprogramm

    serversuche()       # Serversuche wird ausgeführt
