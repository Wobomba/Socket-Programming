from email import message
import socket
from server import HEADER
from server import DISCONNECT_MSG
from server import FORMAT

PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#setting up a socket for the client to communicate with the server
#the data will be streaming through IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server
client.connect(ADDR)

def send(msg):
    #encode the string into a byte-size object to send to the socket
    #to send objects other than strings, send json serialized files or pickled files
    message = msg.encode(FORMAT)
    #obtaining the length of the object
    msg_length = len(message)
    #encoding the message to UTF-8 format
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))#ideally you can use the same header number to send a message to the server
    #back to the client

send('Newton10')
send(DISCONNECT_MSG)

