MYPORT = 50000

import sys
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
name=(input("Bitte Name eingeben: ")+": ").encode("UTF-8")
asciiart= "           __ __\n
            ,;::\::\ \n
          ,'/' `/'`/ \n
      _\,: '.,-'.-':.\n
     -./"'  :    :  :\/,\n
      ::.  ,:____;__; :-\n
      :"  ( .`-*'o*',);\n
       \.. ` `---'`' /\n
        `:._..-   _.'\n
        ,;  .     `.\n
       /"'| |       \\n
      ::. ) :        :\n
      |" (   \       |\n
      :.(_,  :       ;\n
       \'`-'_/      /\n
        `...   , _,'\n
         |,|  : |\n
         |`|  | |\n
         |,|  | |\n
     ,--.;`|  | '..--.\n
    /;' "' ;  '..--. ))\n
    \:.___(___   ) ))'\n
           SSt`-'-'' \n".encode("UTF-8")

while True:
    data = input("Nachricht: ").encode("UTF-8")
    s.sendto(asciiart, ('<broadcast>', MYPORT))

