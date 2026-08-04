# NETWORKING PROJECT

# Network Traffic Sniffer (Packet Analyzer)

## Goal
A Python tool using Scapy to capture and inspect live network packets —
showing source/destination IPs, ports, protocol type, and packet size
in real time.

## What I learned (so far)
- How packet sniffing works at a conceptual level: capturing raw
  packets as they pass through a network interface
- The difference between TCP and UDP traffic, and how to identify
  each by inspecting packet layers
- Berkeley Packet Filter (BPF) syntax for filtering captured traffic
  (e.g. `tcp`, `udp`, `port 443`) — the same filter language Wireshark uses
- Why packet capture requires elevated (root/sudo) privileges

## How to run it (once working)
```bash
sudo python3 sniffer.py
```
Requires `sudo` since raw packet capture needs elevated permissions.

## Requirements
- Python 3
- Scapy:
```bash
sudo apt install python3-scapy
```
(Currently troubleshooting installation — see Notes below.)

## Features (planned)
- [ ] Live packet capture with source/destination IP and port
- [ ] Protocol identification (TCP/UDP/other)
- [ ] Packet size display
- [ ] Optional BPF filtering (e.g. only TCP, only port 443)
- [ ] Save captures to a `.pcap` file for Wireshark analysis

## Notes / Challenges
- Ran into installation errors trying to install Scapy via pip
  (`sudo pip install scapy --break-system-packages`). Currently
  troubleshooting — likely either a pip/environment conflict or a
  network/DNS issue similar to earlier projects.
- Plan: try installing via `apt` instead (`python3-scapy`), which is
  the more standard approach on Debian-based systems like Mint.

## Ethical note
This tool should only be used on networks you own or have explicit
permission to monitor. Packet sniffing captures traffic from all
devices on a network, not just your own — use responsibly.
