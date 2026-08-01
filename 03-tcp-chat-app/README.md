# Networking Projects


# Simple TCP Chat App

## Goal
A multi-user chat application built with raw TCP sockets — a server
that accepts multiple client connections and broadcasts messages
between them in real time.

## What I learned
- Client-server architecture over TCP sockets
- How to handle multiple simultaneous connections using threading
  (one thread per connected client)
- Broadcasting messages to all clients except the sender
- Encoding/decoding data for network transmission (`.encode()` / `.decode()`)
- Running two things at once on the client side (receiving messages
  while also waiting for user input) using a background thread

## How to run it

Start the server first:
```bash
python3 server.py
```

Then start one or more clients (each in its own terminal):
```bash
python3 client.py
```

Enter a username when prompted, then type messages and hit Enter to send.

## Requirements
- Python 3
- `colorama` for colored terminal output:
```bash
pip install colorama --break-system-packages
```

## Features
- [x] Real-time multi-client messaging
- [x] Usernames — messages are prefixed with the sender's name
- [x] Private messaging via `/whisper username message`
- [x] Join/leave notifications broadcast to all connected clients
- [x] Colored terminal output (join/leave = yellow, whispers = magenta,
      messages = cyan)

## Sample Output
## Notes / Challenges
- Initially the server could only handle one client at a time — adding
  a new thread per connection in `accept()` fixed this and let multiple
  people chat simultaneously.
- Had to track clients in a dictionary (socket → username) instead of
  just a list, so messages could be labeled and private messaging
  could look up the right socket by name.
- Learned that `recv()` blocks (pauses) until data arrives, which is
  why the client needs its own background thread just for receiving —
  otherwise it couldn't listen for incoming messages while also
  waiting for you to type.

## Future improvements
- Message history / logging to a file
- Support for group/room-based chats, not just one global room
- Encrypt messages instead of sending plain text
- Reconnect logic if the client's connection drops
