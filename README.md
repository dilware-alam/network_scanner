# Network Vulnerability Scanner

A simple Python-based network reconnaissance tool that combines TCP port scanning, banner grabbing, and Nmap-powered vulnerability/OS detection into a single script.

## Features

- **Port Scanning** – Scans a target host over a specified port range using raw TCP sockets.
- **Banner Grabbing** – Attempts to read service banners from open ports to help identify running services/versions.
- **Vulnerability Scanning** – Uses [Nmap](https://nmap.org/) (via the `python-nmap` wrapper) with OS detection (`-O`), service/version detection (`-sV`), and the NSE `vuln` script category (`--script=vuln`) to identify known vulnerabilities.
- **Scan Summary** – Prints open ports, banners, hostnames, OS matches, detected vulnerabilities, and total scan duration.

## Requirements

- Python 3.7+
- [Nmap](https://nmap.org/download.html) installed and available on your system `PATH`
- Python packages:
  - `python-nmap`
  - `requests`

### Install dependencies

```bash
pip install python-nmap requests
```

### Install Nmap

Download and install Nmap for your OS from [nmap.org/download.html](https://nmap.org/download.html).

- **Windows:** After installing, make sure the Nmap install directory (e.g. `C:\Program Files (x86)\Nmap`) is added to your system `PATH` environment variable. Restart your terminal/IDE after updating `PATH`.
- **macOS:** `brew install nmap`
- **Linux (Debian/Ubuntu):** `sudo apt install nmap`

Verify the install:

```bash
nmap --version
```

## Usage

Run the script and follow the prompts:

```bash
python networkscanner.py
```

You'll be asked for:

- **Target IP or hostname** – the system to scan
- **Starting port** – beginning of the port range to scan
- **Ending port** – end of the port range to scan

### Example

```
Enter the target ip or hostname: 192.168.1.10
Enter the starting port number: 1
Enter the ending port number: 1024
```

The script will then:

1. Scan the given port range for open TCP ports
2. Attempt to grab service banners on each open port
3. Run an Nmap vulnerability/OS scan against the target
4. Print a summary of results and total time taken

## Important: Permissions & Elevated Privileges

- **OS detection (`-O`)** and most **NSE vulnerability scripts** require **administrator/root privileges** to run correctly. Run your terminal/IDE as Administrator (Windows) or with `sudo` (macOS/Linux) if results seem incomplete.
- Only scan hosts and networks you **own or have explicit written authorization** to test. Unauthorized scanning of systems you don't control may violate laws such as the Computer Fraud and Abuse Act (CFAA) or local equivalents, even if no exploitation occurs. This tool is intended for use in authorized penetration testing, lab environments (e.g. your own VMs), and CTF/practice ranges.

## Project Structure

```
networkscanner.py   # Main script: port scanning, banner grabbing, vulnerability scanning
```

## How It Works

| Function | Purpose |
|---|---|
| `port_scan(target_ip, start_port, end_port)` | Iterates over the given port range using raw sockets to detect open TCP ports. |
| `banner_grab(target_ip, port)` | Connects to an open port and attempts to read the service banner. |
| `vulnerabilty_scanner(target_ip)` | Runs an Nmap scan with `-O -sV --script=vuln` to detect OS, service versions, and known vulnerabilities. |
| `network_scan(target_ip, start_port, end_port)` | Orchestrates the full scan: ports → banners → vulnerabilities → summary. |

## Disclaimer

This tool is provided for educational and authorized security-testing purposes only. The author is not responsible for misuse or damage caused by this tool. Always obtain proper authorization before scanning any network or host you do not own.

## License

MIT License — feel free to use, modify, and distribute with attribution.
