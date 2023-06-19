import socket
import threading
import errno
import subprocess
from threading import Thread
import sys

my_username = "clientTest1"

netscanResult = ""


def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            #print(str(data.decode("utf-8")))
            decodedData = str(data.decode("utf-8"))
            decodedData = decodedData.removeprefix("server > ")
            #print("1 - " + decodedData)
            try:
                messageSplit = decodedData.split(" ", 2)
                Requester = messageSplit[1]
                print("2 - " + decodedData + " - " + Requester + " - " + messageSplit[0] + " - " + messageSplit[1])
                #Vérifie si la requête nous est adressé
                if Requester == my_username:
                    # Traitement de la requête du serveur
                    if "/reboot" in message:
                    # Si reboot, vérifié qu'il nous est adressé
                        # Si il nous est adressé, exécuter le reboot
                        data = "reboot ok!"
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                        #rebootAsked() # Exécute le reboot
                    elif "/ping" in message:
                        # Si il nous est adressé, exécuter le ping
                        t1 = Thread(target=pingAsked) # Attribue un thread pour l'exécution du ping
                        t1.start() # Exécute le ping
                        data = "ping ok!"
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/debit" in message:
                        # Si il nous est adressé, exécuter le test de bit
                        t3 = Thread(target=debitAsked) # Attribue un thread pour l'exécution du test de débit
                        t3.start() # Exécute le test de débit
                        data = "debit ok!"
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/netscan" in message:
                        # Si il nous est adressé, exécuter le netscan
                        portsString = messageSplit[3].split(",") # Récupération des ports saisis
                        portsInt = []
                        for i in portsString:
                            portsInt.append(int(i))
                        ipaddr = messageSplit[2] # Récupération de l'IP saisie
                        t2 = Thread(target=netscanAsked(ipaddr, portsInt)) # Attribue un thread pour l'exécution du netscan
                        t2.start() # Exécute le netscan
                        data = "netscan ok!"
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/viewping" in message:
                        # Transmet les logs du dernier ping effectué
                        pingfile = open("./ping.txt", "r")
                        data = pingfile.read()
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/viewdebit" in message:
                        # Transmet les logs du dernier test de debit effectué
                        pingfile = open("./debit.txt", "r")
                        data = pingfile.read()
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/viewnetscan" in message:
                        # Transmet les logs du dernier netscan effectué
                        nscanfile = open("./netscan.txt", "r")
                        data = nscanfile.read()
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                    elif "/update" in message:
                        data = "update ok!"
                        message = data.encode('utf-8')
                        sock.sendall(str.encode(message))
                        #updateAsked() # Exécute le reboot
                else:
                    data = "nok"
                    message = data.encode('utf-8')
                    sock.sendall(str.encode(message))
                #print("3")
            except:
                continue
        except:
            print("Vous avez été déconnecté par le serveur")
            signal = False
            break

#Hôte et port
host = "10.0.1.21"
port = 5001

#Tente la connexion au serveur
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()


while True:
    message = input()
    #sock.sendall(str.encode(message))
