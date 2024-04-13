# MAC Address Changer

## Overview
This Python script provides a command-line interface for changing the MAC (Media Access Control) address of a specified network interface on a Linux system.

### Shebang Line:
```python
#!/usr/bin/env python3
```
This line is a shebang line. It specifies the path to the Python interpreter (`python3`) that will be used to execute the script.

### Import Statements:
```python
import subprocess
import argparse
import re
```
- `subprocess`: This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
- `argparse`: This module makes it easy to write user-friendly command-line interfaces. It parses the command-line arguments passed to the script.
- `re`: This module provides support for regular expressions (regex) in Python. It's used for pattern matching in strings.

### `get_args()` Function:
```python
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
```
- This function defines a command-line argument parser using `argparse`.
- It adds two arguments: `-i` or `--interface` for specifying the network interface and `-m` or `--mac` for specifying the new MAC address.
- If either the interface or the MAC address is not provided, it prints an error message.

### `change_mac()` Function:
```python
def change_mac(interface, new_mac):
    print(f"[+] Changing mac address for {interface} to {new_mac}")
    try:
        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)
    except subprocess.CalledProcessError:
        print("[-] Error: Failed to change MAC Address.")
```
- This function changes the MAC address of a given network interface.
- It uses `subprocess.run()` to execute system commands (`ifconfig`) to bring the interface down, set the new MAC address, and bring it back up.
- If any subprocess call fails, it catches the `CalledProcessError` exception and prints an error message.

### `get_current_mac()` Function:
```python
def get_current_mac(interface):
    ifconfig_result = subprocess.run(["ifconfig", interface], capture_output=True, text=True, check=True )
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.stdout)

    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[-] Could not read mac address")
```
- This function retrieves the current MAC address of a given network interface using the `ifconfig` command.
- It captures the output of `ifconfig` using `subprocess.run()` and then searches for the MAC address pattern using a regular expression.
- If the MAC address is found, it returns it; otherwise, it prints an error message.

## Prerequisites
- Python 3
- Linux Operating System (Tested on Ubuntu)

## Usage
1. **Clone the repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```
2. **Navigate to the directory**: Navigate to the directory containing the script.
    ```bash
    cd your_repository
    ```
3. **Run the script**: Execute the script using the following command:
    ```bash
    python3 mac_changer.py -i [interface] -m [new_mac_address]
    ```
    Replace `[interface]` with the name of the network interface (e.g., eth0, wlan0) and `[new_mac_address]` with the desired MAC address you want to set.

    **Example:**
    ```bash
    python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
    ```

### Options
- `-i, --interface`: Specifies the network interface for which you want to change the MAC address.
- `-m, --mac`: Specifies the new MAC address you want to assign to the interface.

## Notes
- Ensure you have appropriate permissions (e.g., root or sudo) to execute the script and change network configurations.
- Changing MAC addresses can potentially disrupt network connectivity. Use with caution and ensure you have appropriate permissions.