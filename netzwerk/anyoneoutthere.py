MYPORT = 50000

import sys
from socket import *
import time
spielername="test".encode("ascii")
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(spielername, ('<broadcast>', MYPORT))

sender=socket(AF_INET, SOCK_DGRAM)
try:
	sender.bind(("", 50000))
	daten, addr = sender.recvfrom(1024)
finally:
	sender.close()
if addr:
	ip=addr[0]
	print("Mit Server verbunden")
else:
	serv.bind(("", 50000))
	while True:	
		daten, addr = serv.recvfrom(1024)
		time.wait(1)
		serv.sendto("", (addr[0], 50000))
	
