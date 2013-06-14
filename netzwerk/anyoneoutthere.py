MYPORT = 50000

import sys
from socket import *
import time
from threading import Timer
def serverstart():
        serv.bind(("", 50000))
        while True:	
                daten, addr = serv.recvfrom(1024)
                time.wait(1)
                serv.sendto("", (addr[0], 50000))
def serversuche(name):
        spielername=name.encode("ascii")                # Spielername, der an den Server geschickt wird
        s = socket(AF_INET, SOCK_DGRAM)                 # Client wird gestartet
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)       # Clientoptionen (Broadcast)
        s.sendto(spielername, ('<broadcast>', MYPORT))  # Ein Broadcast wird an alle Netzwerkteilnehmer gesendet
        s.close()                                       # Der Client zur Serversuche wird geschlossen

        sender=socket(AF_INET, SOCK_DGRAM)              # Server zur Rückmeldung wird gestartet

        sender.bind(("", 50000))                        # Der Empfänger wird an Port 50000 gebunden
        def senderclose():                              
                sender.close()
        t=Timer(5.0, senderclose)
        t.start()
        while True:                                     # Der Client wartet 5s auf Antwort von evtl. vorhandenem Server
                daten, addr = sender.recvfrom(1024)
        if addr:                                        # Falls Server vorhanden, wird die IP-Addresse an die gesendet wird, festgelegt
        	ip=addr[0]
        	print("Mit Server verbunden")
        else:                                           # Andernfalls wird der Server gestartet
                serverstart()
	

if __name__=="__main__":
        serversuche("Daniel")
        
