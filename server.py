from concurrent.futures import thread
import socket
import threading
#first message to the server
HEADER = 64  
##port to connect to the server
PORT = 5060
#obatining the device ipv4 addr as the server ip
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

#setting up a socket for the server to communicate with the client.
#the data will be streaming through IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#to enable different clients to communicate, store the messages in a list. After send them to each client.


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        #determining how long the incoming message is
        msg_length = conn.recv(HEADER).decode(FORMAT) 
        #converting the message to int to determing if the length is within the header
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f'[{addr}] {msg} ')
            conn.send('Message received'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {server}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS]{threading.active_count() - 1}')

print('[STARTING] server is starting...')
start()
