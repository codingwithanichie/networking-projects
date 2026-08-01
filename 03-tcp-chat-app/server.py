import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

clients = {}  # socket -> username

def broadcast(message, sender_socket=None):
    for client in list(clients.keys()):
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        del clients[client_socket]
        client_socket.close()
        broadcast(f"* {username} has left the chat *".encode())
        print(f"[DISCONNECTED] {username} left.")

def send_private(sender_socket, target_name, message):
    for client, name in clients.items():
        if name.lower() == target_name.lower():
            sender_name = clients[sender_socket]
            client.send(f"[whisper from {sender_name}] {message}".encode())
            sender_socket.send(f"[whisper to {name}] {message}".encode())
            return
    sender_socket.send(f"* User '{target_name}' not found *".encode())

def handle_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode().strip()
        clients[client_socket] = username
        print(f"[NEW CONNECTION] {username} ({address}) connected.")
        broadcast(f"* {username} has joined the chat *".encode(), client_socket)

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            text = message.decode()

            if text.startswith("/whisper "):
                parts = text.split(" ", 2)
                if len(parts) == 3:
                    _, target, private_msg = parts
                    send_private(client_socket, target, private_msg)
                else:
                    client_socket.send(b"* Usage: /whisper username message *")
            else:
                full_message = f"{username}: {text}"
                print(full_message)
                broadcast(full_message.encode(), client_socket)
    except:
        pass
    finally:
        remove_client(client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
