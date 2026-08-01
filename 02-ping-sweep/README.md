# Networking Projects

# Ping Sweep / Network Discovery Tool

## Goal
A Python tool that scans a subnet (e.g. 192.xxx.x.x/24) and reports
which hosts on the local network are currently online.

## What I learned
- How ICMP ping works to check if a host is alive
- Subnetting and CIDR notation (e.g. /24 = 254 possible hosts)
- Using Python's `ipaddress` module to generate host ranges
- Multithreading to ping many hosts in parallel instead of one at a time

## How to run it
```bash
python3 ping_sweep.py
```
Then enter a subnet in CIDR notation, e.g. `192.xxx.x.x/24`

## Requirements
- Python 3
- No external libraries needed (uses built-in `subprocess`, `ipaddress`,
  and `threading`)
- Must be run on a network you own or have permission to scan

## Sample Output
Swept my home network:

my router and my own machine are visible. Not
every device on the network necessarily shows up — some devices
don't respond to ICMP ping requests even while connected.

## Notes / Challenges
- Pinging 254 addresses one at a time was slow, so I used threading
  to run all the pings concurrently, similar to the port scanner project.
- Learned that a low result count doesn't always mean a bug — some
  devices silently ignore pings for privacy/battery reasons.

## Future improvements
- Resolve IPs to hostnames so devices are labeled by name, not just IP
- Export results to a CSV or JSON file
- Automatically run the port scanner against each discovered host
