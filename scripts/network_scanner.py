import scapy.all as scapy
import argparse
import socket

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    #Check for errors i.e if the user does not specify the target IP Address
    #Quit the program if the argument is missing
    #While quitting also display an error message
    if not options.target:
        #Code to handle if interface is not specified
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options
  
def check_ports(ip, ports):
    with open("output/netscan.txt", "a") as f:
        f.write("-----------------------------------\nAdresse IP\tPort\t\tOuvert/Fermé\n-----------------------------------\n")
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                f.write(f'{ip}\t{port}\t\tOuvert\n')
            else:
                f.write(f'{ip}\t{port}\t\tFermé\n')
            sock.close()
        f.write("-----------------------------------\n")
  
def scan(ip, portsList):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        check_ports(answered_list[i][1].psrc, portsList)
        result.append(client_dict)

    return result

def display_result(result):
    print("-----------------------------------\nAdresse IP\t\tAdresse MAC\n-----------------------------------\n")
    for i in result:
        print("{}\t{}".format(i["ip"], i["mac"]))
        
def create_result(result):
    output = "-----------------------------------\nAdresse IP\t\tAdresse MAC\n-----------------------------------\n"
    for i in result:
        output += "{}\t{}\n".format(i["ip"], i["mac"])
    output += "-----------------------------------"
    return output

def translate_result(result):
    with open("output/netscan.txt", "a") as f:
        f.write("-----------------------------------\nAdresse IP\t\tAdresse MAC\n-----------------------------------\n")
        for i in result:
            f.write("{}\t{}\n".format(i["ip"], i["mac"]))
            
            
# options = get_args()

# portInput = "0"
# portsList = []

# while True:
#     portInput = input("Port à vérifier ('stop' si aucun) :")
#     if portInput == "stop":
#         break
#     newPort = int(portInput)
#     portsList.append(newPort)
#     print("Port ajouté, écrire stop pour lancer le scan")

    
# scanned_output = scan(options.target, portsList)
# display_result(scanned_output)
