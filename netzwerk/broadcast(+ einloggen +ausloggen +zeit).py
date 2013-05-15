MYPORT = 50000

import sys, time, datetime, math
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

name=(input("Bitte Name eingeben: ")+": ").encode("UTF-8")

s.sendto(name+("loggte sich ein (").encode("UTF-8")+((datetime.datetime.fromtimestamp(time.time())).strftime('%H:%M:%S')+")").encode("UTF-8"), ('<broadcast>', MYPORT))

time = ((datetime.datetime.fromtimestamp(time.time())).strftime('%H:%M:%S')+")").encode("UTF-8")

print("schreibe +ausloggen zum ausloggen")

while True:
    
    raw = input("Nachricht: ")

    if raw == "+ausloggen":
        s.sendto(name+("loggte sich aus (").encode("UTF-8")+time, ('<broadcast>', MYPORT))
        break
    
    data = (raw + " (").encode("UTF-8")
    
    s.sendto(name+data+time, ('<broadcast>', MYPORT))
    

