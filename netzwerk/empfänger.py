import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try: 
    s.bind(("", 50000)) 
    while True: 
        daten, addr = s.recvfrom(1024) 
        print ("[%s] %s" % (addr[0], daten.decode("UTF-8"))) 
finally: 
    s.close()
