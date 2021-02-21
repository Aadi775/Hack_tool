import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
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
        while True:
            b = input()
            conn.send(b)
            if b=="i gave up":
                break

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def get_shot():
    while True:
        read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

        for sock in read_sockets:

            if sock == server_socket:

                sockfd, client_address = server_socket.accept()
                connected_clients_sockets.append(sockfd)

            else:
                try:

                    data = sock.recv(4096)
                    txt = str(data)

                    if txt.startswith('SIZE'):
                        tmp = txt.split()
                        size = int(tmp[1])

                        print 'got size'

                        sock.send("GOT SIZE")

                    elif txt.startswith('BYE'):
                        server.shutdown()

                    elif data:

                        myfile = open(basename % imgcounter, 'wb')

                        data = sock.recv(40960000)
                        if not data:
                            myfile.close()
                            break
                        myfile.write(data)
                        myfile.close()

                        server.send("GOT IMAGE").encode("utf-8")
                        server.shutdown()
                except:
                    server.close()
                    connected_clients_sockets.remove(sock)
                    continue
            imgcounter += 1
    server_socket.close()


print("[STARTING] server is starting...")
start()
