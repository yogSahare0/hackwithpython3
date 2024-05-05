# HTTP Sniffer

This is a Python script that sniffs HTTP packets on a specified network interface and extracts URLs and login information from HTTP requests.

## Prerequisites

- Python 3.x
- scapy library (`pip install scapy`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/http-sniffer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd http-sniffer
    ```

3. Run the script with root privileges:

    ```bash
    sudo python3 http_sniffer.py
    ```

4. Specify the network interface to sniff (e.g., eth0, wlan0).

## Description

- `http_sniffer.py`: Main Python script containing the HTTP sniffer functionality.
- `sniff(interface)`: Function to start sniffing HTTP packets on the specified interface.
- `get_url(packet)`: Function to extract the URL from an HTTP packet.
- `get_login_info(packet)`: Function to extract login information (e.g., usernames, passwords) from an HTTP packet.
- `process_sniffed_packet(packet)`: Function to process each sniffed HTTP packet, extracting URLs and login information.
- Replace `"eth0"` with the appropriate network interface on which you want to sniff HTTP packets.

## Disclaimer

This script is for educational purposes only. Do not use it on networks or systems without proper authorization.
