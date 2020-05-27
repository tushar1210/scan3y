import socket 
import subprocess
import sys
import os
import re
from datetime import datetime
import shlex
import logging
import time

def check(ports,poison):
    for p in ports:
        if p==poison:
            return True
    return False
    
def scan():
    p1 = 1 #int(input("Initial port range = "))
    p2 = 100 #int(input("Final port range = "))
    ports = []
    remoteServer = "localhost" #str(input("Enter Remote Server : "))
    remoteServerIP = socket.gethostbyname(remoteServer)
    # print("-" * 60)
    f.write("Scanning remote host  {} \n".format(remoteServerIP))
    # print("-" * 60)
    t1 = datetime.now()
    try:
        for port in range(p1,p2):
            sock = socket.socket(socket.AF_INET,
            socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                # print("Port {}: 	 Open".format(port))
                ports.append(port)
                f.write('{} {} {}'.format(ports , t1 ,'\n'))
            sock.close()
    except KeyboardInterrupt:
        f.write('Script Terminated \n')
        f.close()
        sys.exit()
    except socket.gaierror:
        f.write('Hostname could not be resolved. Exiting \n')
        sys.exit()
    except socket.error:
        f.write("Couldnt connect to server \n")
        sys.exit()

    t2 = datetime.now()
    total = t2-t1
    f.write('Scanning completed in : {}  {}'.format(total ,'\n'))
    return ports

f=open('.log','a+')
def main():
    while(True):
        # with open("file.txt", "w") as f:
        f.write('-'*60 + '\n' +' '*25 + 'New Session'+'\n')
        ports = scan()
        if ports==[]:
            f.write('No open ports found \n')
        else:
            f.write('ports found are : {} \n'.format(ports))
        for poison in ports:
            cmd = "lsof -i :{}".format(poison)
            args = shlex.split(cmd)
            output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
            output=str(output)
            pid = ''
            for i in range(len(output)):
                if output[i]>='0' and output[i]<='9':
                    while output[i]>='0' and output[i]<='9':
                        pid+=output[i]
                        i+=1
                    break
                
            
            f.write('\n')
            cmd = "kill -9 {}".format(pid)
            f.write('PID found : {} \n'.format(pid))
            f.write('\n')
            args = shlex.split(cmd)
            output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            if(error):
                f.write('Error found : {}'.format(str(error)))
            os.fsync(f)


if __name__ == "__main__": main()