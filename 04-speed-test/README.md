# Bandwidth / Speed Test Tool

## Goal
A Python tool that measures internet download and upload speed, with
the ability to choose a specific test server instead of relying purely
on automatic server selection.

## What I learned
- How speed tests work: download/upload a known amount of data and
  measure the time it takes to calculate Mbps
- The difference between building a measurement tool from scratch
  (single fixed URL) vs using a library that dynamically finds
  reachable servers
- That "distance" in server selection is calculated geographically,
  not by actual network reachability — the closest server on paper
  isn't always the fastest, or even reachable
- How to debug misleading tool output (a reported "1,800,000 ms ping"
  was actually a disguised timeout, not a real result)
- Installing Python packages system-wide with `sudo` vs user-level,
  and how that can affect whether a script can find a library at runtime

## How to run it
```bash
python3 speed_test.py
```
You'll be shown a list of the 5 nearest test servers and can either
pick one by number, or press Enter to let the tool auto-select.

## Requirements
```bash
sudo pip install speedtest-cli --break-system-packages
```

## Features
- [x] Download speed test (Mbps)
- [x] Upload speed test (Mbps)
- [x] Ping/latency measurement
- [x] Lists 5 nearest servers with distance, lets user choose manually
- [x] Falls back to automatic best-server selection if no choice is made

## Sample Output
**Note:** the test above actually failed silently — `1800000 ms` is
`speedtest-cli`'s internal timeout being misreported as a ping value,
and `0.00 Mbps` confirms no data was actually transferred. This
happened because the nearest registered speedtest.net servers (all in
the Netherlands, ~4,300+ km away) may not be reliably reachable from
my network/ISP. This turned into a useful lesson in not
trusting tool output blindly — a "successful-looking" result can
still represent a failure under the hood.

## Notes / Challenges
- First attempt: custom script downloading a fixed file
  (`speed.hetzner.de`) — failed due to DNS resolution issues specific
  to my network.
- Second attempt: switched the fixed URL to Cloudflare — same DNS-type
  issue persisted.
- Solution: switched to the `speedtest-cli` library, which dynamically
  finds servers instead of depending on one hardcoded domain — more
  resilient across different networks.
- Discovered that the "closest" servers by distance aren't necessarily
  reachable — worth checking `speedtest-cli --list | grep -i <region>`
  to find genuinely local/reachable servers instead of trusting
  auto-selected or distance-sorted results.

## Future improvements
- Detect and clearly flag failed tests (e.g. if download/upload return
  0.00 Mbps, report "test failed — try a different server" instead of
  printing it as a normal result)
- Add a fallback to Cloudflare's speed test API if speedtest.net
  servers are unreachable
- Log results with timestamps to track connection speed over time
- Add a `--server` flag to skip the menu and jump straight to a known
  good server
