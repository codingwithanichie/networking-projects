import socket
import threading

def scan_port(target, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    sock.close()

def scan_range(target, start_port, end_port):
    open_ports = []
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nScan complete. {len(open_ports)} open port(s): {sorted(open_ports)}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    scan_range(target, start_port, end_port)
