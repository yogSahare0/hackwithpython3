# File Interceptor

This project contains a Python script that uses `scapy` and `netfilterqueue` to intercept and modify network packets. Specifically, it detects `.exe` file requests and redirects the response to a specified location.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- `scapy`
- `netfilterqueue`

You can install the required Python packages using pip:

```bash
pip install scapy netfilterqueue
```

## Usage

1. Clone the repository or download the script `file-interceptor.py`.
2. Run the script with superuser privileges:

```bash
sudo python3 file-interceptor.py
```

## How It Works

1. The script sets up a netfilter queue to intercept network packets.
2. It checks if the packet contains a request for a `.exe` file.
3. If such a request is detected, it records the acknowledgment number.
4. When a response with a matching sequence number is found, it replaces the payload with a redirect response.

## Code Explanation

### `set_load(packet, load)`

This function modifies the payload of the packet and recalculates the necessary checksums.

### `process_packet(packet)`

This function processes each packet from the netfilter queue:
- If it detects a request for a `.exe` file, it logs the acknowledgment number.
- If it detects a response with a matching sequence number, it replaces the payload with a redirect response.

### Main Execution

The script binds the process_packet function to a netfilter queue and starts processing packets.

## Disclaimer

This script is for educational purposes only. Modifying network packets without permission can be illegal and unethical. Use it responsibly and ensure you have the necessary permissions to intercept and modify network traffic.
