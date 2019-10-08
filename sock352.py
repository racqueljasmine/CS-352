
import binascii
import socket as syssock
import struct
import sys
import random;

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

### Global variables
global sock352PktHdrData
sock352PktHdrData = "!BBBBHHLLQQLL" # used to pack the packet headers 

### Functions 

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here 
    # save the ports globally in the class
    global receivingPort
    receivingPort = UDPportRx 
    global transferringPort
    transferringPort = UDPportTx
    pass 
    
class socket:
    
    def __init__(self):  # fill in your code here 
        # set up the socket
        global sock
        sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
        return
    
    # binds a server socket to the given address.
    # called by the server
    def bind(self,address):
        # called in server1.py
        return 

    # activates a connection between a server and a client socket
    # called by the client
    def connect(self,address):  # fill in your code here 
        # create a message to establish the first part of the 3-way handshake
        header_format = struct.Struct(sock352PktHdrData)
        version = 1
        flag = 0
        seq = random.randint(1,100) # generate a random sequence number
        ack = 0
        payload = header_format.size
        default = 0
        header = header_format.pack(version, flag, default, default, default, default, default, seq, ack, default, payload)
        
        # test
        print(header)
        return 
    
    # sets up a listener for a server socket for any incoming messages
    # called by the server
    def listen(self,backlog):
        # called in server.py
        return

    # accepts a connect and waits until connection arrives (blocking)
    # called by the server
    def accept(self):
        (clientsocket, address) = (1,1)  # change this to your code 
        return (clientsocket,address)
    
    # closes a socket
    # called by the server and the client
    def close(self):   # fill in your code here 
        return 

    def send(self,buffer):
        bytessent = 0     # fill in your code here 
        return bytesent 

    def recv(self,nbytes):
        bytesreceived = 0     # fill in your code here
        return bytesreceived 


    


