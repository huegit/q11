MYPORT = 50000

import sys
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
name=(input("Bitte Name eingeben: ")+": ").encode("UTF-8")
asciiart= ""  ____  ____  ____  ____                      ______________________
    /\   \/\   \/\   \/\   \                    /\                     \
   /  \___\ \___\ \___\ \___\                  /  \    _________________\
   \  / __/_/   / /   / /   /                  \   \   \                /
    \/_/\   \__/\/___/\/___/                    \   \   \__________    /
      /  \___\    /  \___\                       \   \   \    /   /   /
      \  / __/_  _\  /   /                        \   \   \  /   /   /
       \/_/\   \/\ \/___/                          \   \   \/   /   /
         /  \__/  \___\                             \   \  /   /   /
         \  / _\  /   /                              \   \/   /   /
          \/_/\ \/___/                                \      /   /
            /  \___\                                   \    /   /
            \  /   /                                    \  /   /
             \/___/                                      \/___/"".encode("UTF-8")

while True:
    data = input("Nachricht: ").encode("UTF-8")
    s.sendto(asciiart, ('<broadcast>', MYPORT))

