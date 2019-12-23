import socket 
import subprocess
import sys
import os
import re
from datetime import datetime

subprocess.call('clear',shell=True)

p1 = int(input("Initial port range = "))
p2 = int(input("Final port range = "))

ports = []

remoteServer = str(input("Enter Remote Server : "))
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(p1,p2):
        sock = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
            ports.append(port)
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print("Couldnt connect to server")
    sys.exit()
t2 = datetime.now()

total = t2-t1

print('Scanning completed in : ', total)

poison = int(input("Enter port to poision : "))



