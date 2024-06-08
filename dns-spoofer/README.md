# DNS Spoofing Script

This repository contains a Python script for DNS spoofing using `scapy` and `netfilterqueue`. The script intercepts DNS requests and spoofs responses to redirect traffic to a specified IP address.

## Prerequisites

- Python 3.x
- `scapy` library
- `netfilterqueue` library
- Root or administrative privileges to modify iptables rules

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/dns-spoofing.git
cd dns-spoofing
```

2. **Install the required libraries:**

```bash
pip install scapy netfilterqueue
```

## Usage

1. **Set up iptables rules:**

```bash
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
```

2. **Run the script:**

```bash
sudo python3 dns_spoof.py
```


## Important Notes

- This script is for educational purposes only. Unauthorized interception and modification of network traffic is illegal and unethical.
- Ensure you have explicit permission to test and deploy this script in your network environment.


