from socket import *
import threading

MYPORT = 50000
global client_new
client_new= None

class Server(threading.Thread):
    
    def run(self):
        addr = ("", MYPORT)
        server = socket(AF_INET, SOCK_DGRAM)
        server.bind(addr)
        
        while True:
            daten, address = server.recvfrom(1024)
            print(address, daten)
            global client_new
            client_new = address
            self.handle()
            

    def handle(self):
        server = socket(AF_INET, SOCK_DGRAM)
        antwort = "antwort".encode("ascii")
        server.sendto(antwort, (client_new))

def serverstart():
    server = Server()
    server.start()

def serversuche():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
    s.settimeout(3)

    print("Versuche Server zu finden...")

    myname = input("Name:").encode("ascii")
    s.sendto(myname, ("<broadcast>", MYPORT))

    try:
        antwort = s.recvfrom(1024)
        print("Server gefunden")

    except timeout:
        print("Kein Server gefunden, erstelle neuen")
        serverstart()

    s.close

if __name__ == "__main__":

    serversuche()
