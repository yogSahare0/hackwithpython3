#!/usr/bin/env python3

import subprocess
import argparse
import re

def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("-i", "--interface", type=str, help="interface to change its mac address")
        parser.add_argument("-m", "--mac", type=str, help="new  mac address")

        args = parser.parse_args()

        if not args.interface:
                parser.error("[-] Please specify interface, use -h for information.")
        elif not args.mac:
                parser.error("[-] Please specify a new mac address, use -h for information.")
        return args

def change_mac(interface, new_mac):
        print(f"[+] Changing mac address for {interface} to {new_mac}")
        try:
                subprocess.call(["ifconfig", interface, "down"])
                subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
                subprocess.call(["ifconfig", interface, "up"])
        except subprocess.CalledProcessError:
                print("[-] Error: Failed to change MAC Address.")

def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf8"))

        if mac_address_search:
                return mac_address_search.group(0)
        else:
                print("[-] Could not read mac address")


args = get_args()
#change_mac(args.interface, args.mac)

current_mac = get_current_mac(args.interface)
print(f"Current MAC : {current_mac}")

change_mac(args.interface, args.mac)

current_mac = get_current_mac(args.interface)
if current_mac == args.mac:
        print(f"[+] MAC Address was successfully changed to {current_mac}")
else:
        print("[+] MAC address did not get changed.")
