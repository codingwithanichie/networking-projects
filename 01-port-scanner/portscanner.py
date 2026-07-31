import socket

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # wait max 1 second per port
    result = sock.connect_ex((target, port))  # returns 0 if open
    sock.close()
    return result == 0

def scan_range(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    print(f"\nScan complete. {len(open_ports)} open port(s) found: {open_ports}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    scan_range(target, start_port, end_port)
