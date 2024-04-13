# Network Scanner

This Python script is a network scanner that utilizes the Scapy library to discover active devices within a specified IP range. Let's go through it step by step:

1. **Shebang Line**:
    ```python
    #!/usr/bin/env python3
    ```
    This line specifies the path to the Python interpreter to be used to execute the script.

2. **Imports**:
    ```python
    import scapy.all as scapy
    import argparse
    import ipaddress
    import sys
    ```
    - `scapy`: This is a powerful packet manipulation library for Python, which is used for crafting and decoding packets.
    - `argparse`: This module provides a mechanism to parse command-line arguments.
    - `ipaddress`: This module provides classes for working with IP addresses, networks, and interfaces.
    - `sys`: This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

3. **Function Definitions**:
    - `get_args()`: This function is responsible for parsing the command-line arguments using the `argparse` module.
    - `validate_ip(ip)`: This function checks if the provided IP address or IP range is valid.
    - `scan(ip)`: This function performs the actual network scan. It sends ARP requests to the specified IP range and collects the responses.
    - `print_result(results_list)`: This function prints the results of the scan in a formatted manner.

4. **Argument Parsing**:
    ```python
    args = get_args()
    ```
    This line calls the `get_args()` function to parse the command-line arguments.

5. **IP Validation**:
    ```python
    if not validate_ip(args.range):
       print("[-] Invalid IP address range.")
       sys.exit(1)
    ```
    It checks if the provided IP range is valid. If not, it prints an error message and exits the script.

6. **Scanning**:
    ```python
    scan_result = scan(args.range)
    ```
    This line initiates the network scan using the `scan()` function and stores the results in `scan_result`.

7. **Printing Results**:
    ```python
    print_result(scan_result)
    ```
    It prints the results of the scan using the `print_result()` function.

8. **Error Handling**:
    The script includes exception handling to catch and print any errors that may occur during the scanning process.

Overall, this script provides a simple yet effective way to discover active devices on a network using ARP requests. It's a useful tool for network administrators and security analysts.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
   ```
   python3 network_scanner.py -r <ip_range>
   ```
   Replace `<ip_range>` with the IP range you want to scan (e.g., `192.168.1.1/24`).
4. Wait for the script to complete the scan.
5. The script will print out the IP and MAC addresses of active devices on the network.

## Options

- `-r, --range`: Specify the IP range to scan.

## Example

```
python3 network_scanner.py -r 192.168.1.1/24
```

## Note

- Make sure to run the script with appropriate permissions (e.g., as root or with sudo) to allow access to raw sockets.
