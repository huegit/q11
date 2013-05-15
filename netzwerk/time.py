MYPORT = 50000

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#name=(input("Bitte Name eingeben: ")+": ").encode("UTF-8")

while True:
    data = (repr(time.time())).encode("UTF-8")
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(.1)

