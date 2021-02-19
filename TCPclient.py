import socket
from main import get_ip,takeshot

HEADER = 64
port = 5050
server = get_ip()
Addr = (server, port)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Addr)

def send_Shot(a):
    try:
        myfile = open("c:\\WINDOWS\\Temp\\logo.bmp","rb")
        bytes = myfile.read()
        size = len(bytes)

        client.sendall("Size %s"% size)
        answers = client.recv(4094)

         if answer == 'GOT SIZE':
             client.sendall(bytes)

        # check what server send
            answer = client.recv(4096)
            print 'answer = %s' % answer

            if answer == 'GOT IMAGE' :
                client.sendall("BYE BYE ")
                print 'Image successfully send to server'
    except Exception as e:
        print(e)

if client.recv(HEADER).decodecode('utf8') == "take_shot":
    shot = take_shot()



def send(msg):
    message = msg.encode("utf-8")
    msg_lenght= msg.length()
    send_length= str(msg_lenght).encode("utf-8")
    send_length+=b' '* (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(999).decode())

while True:
    a = input()
    send(a)
