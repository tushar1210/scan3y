import socket 
import subprocess
import sys
import os
import re
from datetime import datetime
import shlex

def check(ports,poison):
    for p in ports:
        if p==poison:
            return True
    return False
    
def scan():
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
            # if ports != []:
            #     print(ports)
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
    return ports

def main():
    subprocess.call('clear',shell=True)
    
    #ports = scan()
    poison = 50
    
    cmd = "lsof -i :{}".format(poison)
    args = shlex.split(cmd)
    output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
    output=str(output)
    pid = ''
    # r = list(output.split(' '))
    for i in range(len(output)):
        if output[i]>='0' and output[i]<='9':
            while output[i]>='0' and output[i]<='9':
                pid+=output[i]
                i+=1
            break    
    # print(output)
    
    print(int(pid))
    


if __name__ == "__main__": main()