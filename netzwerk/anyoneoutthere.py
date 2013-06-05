MYPORT = 50000

import sys
from socket import *
import time
spielername="test"
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(spielername, ('<broadcast>', MYPORT)

e=socket(AF_INET, SOCK_DGRAM)
try:
	e.bind(("", 50000))
	daten, addr = e.recvfrom(1024)
finally:
	e.close()
if addr:
	ip=addr[0]
	print("Mit Server verbunden")
else:
	e.bind(("", 50000))
	while True:	
		daten, addr = s.recvfrom(1024)
		time.wait(1)
		s.sendto("", (addr[0], 50000))
	