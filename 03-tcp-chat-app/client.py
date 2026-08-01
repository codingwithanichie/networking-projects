import socket
import threading
from colorama import init, Fore, Style

init(autoreset=True)

HOST = "127.0.0.1"
PORT = 5555

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break

            if message.startswith("*"):
                print(f"\n{Fore.YELLOW}{message}{Style.RESET_ALL}")
            elif "[whisper" in message:
                print(f"\n{Fore.MAGENTA}{message}{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.CYAN}{message}{Style.RESET_ALL}")
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    username = input("Enter your username: ")
    client.send(username.encode())

    print(f"{Fore.GREEN}Connected as {username}. Type a message and hit Enter.")
    print(f"{Fore.GREEN}Use /whisper username message for a private message.\n")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    while True:
        message = input()
        client.send(message.encode())

if __name__ == "__main__":
    start_client()
