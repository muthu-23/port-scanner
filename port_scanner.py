import socket
target = input("Enter target IP address: ")
start_port = 1
end_port = 1024
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()