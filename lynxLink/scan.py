import scapy.all as scapy
import argparse
import socket

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

def create_result(result):
    with open("./netscan.txt", "a") as f:
        f.write("-----------------------------------\nAdresse IP\t\tAdresse MAC\n-----------------------------------\n")
        for i in result:
            f.write("{}\t{}\n".format(i["ip"], i["mac"]))
            
ppports = [80,443]
create_result(scan("192.168.213.16", ppports))
