# Networking Projects

# Port Scanner

## Goal
A Python TCP port scanner that checks a target IP for open ports within a given range.

## What I learned
- How TCP connections work (sockets, connect_ex)
- Well-known ports and what common services run on them
- Multithreading to speed up scans

## How to run it
```bash
python3 port_scanner.py
```
Then enter a target IP/hostname, start port, and end port.

## Requirements
- Python 3
- No external libraries needed (uses built-in `socket` and `threading`)

## Sample Output
Scanned my local machine:
- Port 631 (CUPS/printing) - OPEN
- Port 8000 (test HTTP server) - OPEN

## Notes / Challenges
Learned that scanning without threading was slow for larger port
ranges — added threading to scan all ports concurrently.

## How it works (TCP three-way handshake)

Each port check triggers a TCP three-way handshake:
1. **SYN** — client sends a request to connect
2. **SYN-ACK** — if something is listening, the server acknowledges
3. **ACK** — client confirms, connection is established

Python's `connect_ex()` handles this handshake automatically:
- Returns `0` if all three steps complete → port is **open**
- Returns an error if the server sends a RST (reset) → port is **closed**
- Times out if nothing responds (e.g. blocked by firewall) → port is **filtered**

This is also why threading made the scan faster — each handshake takes
a small amount of round-trip time, so running many at once in parallel
threads is much quicker than doing them one after another.

------------------------------
