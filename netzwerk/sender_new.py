import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP-Sender\nIP ändern: +ip\nbeenden: +exit")
print("Zur Hlfe bei der IP-Adresse +help")

ip = input("IP-Adresse: ")

if ip=="+help":
    
    raum = str(input("Bitte Computeraum eingeben (1,2): "))
    nummer = str(input("Bitte PC-Nummer eingeben!: "))
    ip = ("10."+raum+".0."+nummer)
    print(ip)
    
while True:
    
    nachricht = input("Nachricht: ")
    
    if nachricht == "+ip":
        
        ip = input("IP-Adresse: ")
        
        if ip=="+help":
            raum = str(input("Bitte Computeraum eingeben (1,2): "))
            nummer = str(input("Bitte PC-Nummer eingeben!: "))
            ip = ("10."+raum+".0."+nummer)
            print("Empfänger IP geändert!")
            
        else:
            print("Empfänger IP geändert!")
                  
    if nachricht == "+exit":
        break
    
    """if nachricht == "+help":
            raum = str(input("Bitte Computeraum eingeben (1,2): "))
            nummer = str(input("Bitte PC-Nummer eingeben!: "))
            ip = ("10."+raum+".0."+nummer)
            print("Empfänger IP geändert!")"""
            
    else:
        s.sendto(nachricht.encode("ascii"), (ip, 50000))
        
s.close()
