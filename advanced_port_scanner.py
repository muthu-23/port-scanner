import socket
import re
import time

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip)

def scan_ports(ip, start_port, end_port):
    open_ports = []
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f" Port {port} is OPEN")
                open_ports.append(port)

    end_time = time.time()
    print("\nScan complete.")
    print(f" Total Open Ports: {len(open_ports)}")
    print(f" Time Taken: {round(end_time - start_time, 2)} seconds")


ip = input("Enter the IP address to scan: ")

if not is_valid_ip(ip):
    print(" Invalid IP address format. Exiting.")
else:
    try:
        start_port = int(input("Enter start port (e.g., 20): "))
        end_port = int(input("Enter end port (e.g., 80): "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print(" Invalid port range.")
        else:
            scan_ports(ip, start_port, end_port)
    except ValueError:
        print(" Please enter valid numeric port values.")