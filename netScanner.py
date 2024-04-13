#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import ipaddress
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--range', help='Provide ip range eg. 10.10.10.1/24')
    args = parser.parse_args()
    if not args.range:
        parser.error('[-] Please specify IP range.')
    return args

def validate_ip(ip):
   try:
        ipaddress.ip_network(ip, strict=False)
        return True
   except ValueError:
        return False

def scan(ip):
   try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
        client_list = []
        for element in answered_list:
                client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
                client_list.append(client_dict)
        return client_list
   except Exception as e:
        print(f"Error occurred : {e}")
        sys.exit(1)

def print_result(results_list):
    print('IP\t\t\tMAC Address\n------------------------------------------------')
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

args = get_args()
if not validate_ip(args.range):
   print("[-] Invalid IP address range.")
   sys.exit(1)
scan_result = scan(args.range)
print_result(scan_result)
