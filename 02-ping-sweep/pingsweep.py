import subprocess
import ipaddress
import threading

def ping_host(ip, alive_hosts):
    # -c 1: send 1 packet, -W 1: wait max 1 second for reply
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print(f"{ip} is UP")
        alive_hosts.append(str(ip))

def sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    alive_hosts = []
    threads = []

    print(f"Sweeping {subnet}...\n")

    for ip in network.hosts():
        t = threading.Thread(target=ping_host, args=(ip, alive_hosts))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nSweep complete. {len(alive_hosts)} host(s) found:")
    for host in sorted(alive_hosts):
        print(f" - {host}")

if __name__ == "__main__":
    subnet = input("Enter subnet (e.g. 192.168.0.0/24): ")
    sweep(subnet)
