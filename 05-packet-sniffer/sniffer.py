from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        if packet.haslayer(TCP):
            sport, dport = packet[TCP].sport, packet[TCP].dport
            print(f"{src_ip}:{sport} -> {dst_ip}:{dport} | TCP | {size} bytes")
        elif packet.haslayer(UDP):
            sport, dport = packet[UDP].sport, packet[UDP].dport
            print(f"{src_ip}:{sport} -> {dst_ip}:{dport} | UDP | {size} bytes")
        else:
            print(f"{src_ip} -> {dst_ip} | OTHER | {size} bytes")

def start_sniffing(packet_count=0, bpf_filter="ip"):
    print(f"Starting packet capture (filter: '{bpf_filter}')... Press Ctrl+C to stop.\n")
    sniff(filter=bpf_filter, prn=process_packet, store=False, count=packet_count)

if __name__ == "__main__":
    # count=0 means capture forever until Ctrl+C
    # try filter="tcp" or filter="udp" or filter="port 443" to narrow results
    start_sniffing(packet_count=0, bpf_filter="ip")
