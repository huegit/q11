# Risiko-Server
# version 0.1 20130710
# Danie Strobl, Michael Dörsam

from socket import *         # Socket Server importieren
from threading import Thread # Threading importieren, mögl. später wichtig
import sys

MYPORT = 50000               # Port def

class Server(socket):
    "Klasse Server, kann neue Clients annehmen"
    def __init__(self):
        socket.__init__(self, socket.AF_INET, socket.SOCK_DGRAM)
        self.port=port
        self.clients=[]
        
    def run(self):
        "Start() Methode"
        self.bind("",self.port)                       # wird an addr gebunden
        
        while True:                                     # Schleife
            daten, address = server.recvfrom(1024)      # Empfängt Daten
            
            print(address[0], daten.decode("UTF-8"))    # Gibt sie aus
            
            
            
