import socket
import requests
import nmap
from datetime import datetime


def port_scan(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} for open ports from {start_port} to {end_port}")
    open_ports = []
    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)

        sock.close() 
    return open_ports

def banner_grab(target_ip, port):
    print(f"Grabbing banner for {target_ip}:{port}")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, port))
        sock.settimeout(2)
        banner = sock.recv(1024).decode('utf-8', errors = 'ignore')
        sock.close()
        return banner.strip()
    except:
        return None
    
def vulnerabilty_scanner(target_ip):
    print(f"Starting Vulnerability Scanning for {target_ip}")
    nm = nmap.PortScanner()

    try:
        nm.scan(hosts=target_ip, arguments="-O -sV --script=vuln")
        return nm[target_ip]
    except Exception as e:
        print(f"Error during vulnerability scan {e}")
        return None

def network_scan(target_ip, start_port, end_port):
    print(f"Starting Port Scan For {target_ip}")
    start_time = datetime.now()
    open_ports = port_scan(target_ip, start_port, end_port)
    if open_ports:
        print(f"The open ports for {target_ip} are {open_ports}")
    else:
        print(f"No open ports are found for {target_ip}")

    for port in open_ports:
        banner = banner_grab(target_ip, port)
        if banner:
            print(f"Banner for {target_ip}:{port} - {banner}")
        else:
            print(f"No banner found for {target_ip}")


    vuln_info = vulnerabilty_scanner(target_ip)
    if vuln_info:
        if 'hostnames' in vuln_info:
            print(f"Hostnames:{vuln_info['hostnames']}")
        if 'osmatch' in vuln_info:
            print(f"Operating System: {vuln_info['osmatch']}")
        if 'vulns' in vuln_info:
            print(f"Vulnerabilities: {vuln_info['vulns']}")
    else:
        print("No Vulnerabilities Found")

    end_time = datetime.now()
    print(f"Scan completed in {end_time - start_time}")


        


if __name__== '__main__':
    target_ip = input("Enter the target ip or hostname: ")
    start_port = int(input("Enter the starting port number:"))
    end_port = int(input("Enter the ending port number:"))
    network_scan(target_ip, start_port, end_port)


