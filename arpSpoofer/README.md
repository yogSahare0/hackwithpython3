# ARP Spoofing Tool

This Python script implements an ARP (Address Resolution Protocol) spoofing tool using the Scapy library. ARP spoofing, also known as ARP poisoning, is a type of attack where an attacker sends falsified ARP messages over a local area network, leading to potential interception, modification, or redirection of network traffic.

## Table of Contents
1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Script Explanation](#script-explanation)
4. [Dependencies](#dependencies)
5. [Disclaimer](#disclaimer)

## Introduction

ARP Spoofing is a common technique used in network security assessments and sometimes maliciously by attackers. It involves sending forged ARP messages to the local area network, associating the attacker's MAC address with the IP address of a legitimate device on the network, such as the default gateway or another host.

This script automates the process of ARP spoofing between a target device and the gateway. It continuously sends ARP packets to the target and gateway, associating the attacker's MAC address with each other's IP addresses. Additionally, it handles restoring ARP tables when interrupted by the user.

## Usage

1. **Clone the Repository:**
   ```
   git clone https://github.com/yogSahare0/hackwithpython3.git
   ```

2. **Navigate to the Directory:**
   ```
   cd hackwithpython3/arpSpoofer
   ```

3. **Run the Script:**
   ```
   python3 arpSpoofer.py -t [target IP] -g [gateway IP]
   ```
   Replace `[target IP]` and `[gateway IP]` with the IP addresses of the target device and the gateway, respectively.

4. **To Stop the Attack:**
   Press `Ctrl+C`. The script will automatically restore ARP tables and exit.

## Script Explanation

- **`parse_arguments()`:** Function to parse command-line arguments. It requires specifying the target IP address (`-t` or `--target`) and the gateway IP address (`-g` or `--gateway`).

- **`get_mac(ip)`:** Function to retrieve the MAC address associated with a given IP address using ARP requests.

- **`spoof(target_ip, spoof_ip)`:** Function to send spoofed ARP packets to associate the attacker's MAC address with the IP address of the target or gateway.

- **`restore(destination_ip, source_ip)`:** Function to restore ARP tables by sending legitimate ARP packets.

- **Main Execution:** The script continuously performs ARP spoofing between the target and gateway IP addresses in an infinite loop. It also handles keyboard interrupts (`Ctrl+C`) to gracefully exit the loop and restore ARP tables.

## Dependencies

- **Python 3:** The script is written in Python 3.
- **Scapy:** Scapy library is used for crafting and sending ARP packets.

## Notes
- Ensure you have appropriate permissions (e.g., root or sudo) to execute the script and change network configurations.

## Disclaimer

This tool is meant for educational and security assessment purposes only. Misuse of this tool for unauthorized access to networks or systems is illegal and unethical. Use it responsibly and with proper authorization.