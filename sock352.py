
import binascii
import socket as syssock
import struct
import sys
import random
import thread
import time

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

### Functions 

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here 
    # save the ports globally in the class
    global receivingPort
    receivingPort = UDPportRx 
    global transferringPort
    transferringPort = UDPportTx
    pass 
    
class socket:
    

    ### Global variables
    sock352PktHdrData = "!BBBBHHLLQQLL" # used to pack the packet headers 
    SOCK352_SYN = 1
    SOCK352_FIN = 2
    SOCK352_ACK = 4
    SOCK352_RESET = 8
    SOCK352_HAS_OPT = 160


    def __init__(self):  # fill in your code here 
        # set up the socket
        global sock
        sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
        return
    
    # create a packet header for packets that will be sent out. Only the flags and the ack_no will change
    # returns the header struct created
    def create_packet_header(needed_flags, needed_ack):
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        version = 1
        flags = needed_flags
        opt_ptr = 0
        protocol = 0
        header_len = udpPkt_hdr_data.size
        checksum = 0
        source = 0
        dest = 0
        seq = random.randint(0,9) # generate a random sequence number
        ack = needed_ack
        window = 0
        payload_len = header_len
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr,protocol,header_len,checksum,source,dest,seq,ack,window,payload_len)
        return header


    # binds a server socket to the given address.
    # called by the server
    def bind(self,address):
        # called in server1.py
        return 

    # activates a connection between a server and a client socket
    # called by the client
    def connect(self,address):  # fill in your code here 
        init_three_way_handshake()
        return 

    # initiates a three way handshake with a server socket
    # called by the client
    def init_three_way_handshake():

        # send a SYN message to the server to establish the first part of the 3-way handshake
        header = createMessage(SOCK352_SYN, 0)
        response = send(header) # !! SEND THE MESSAGE HERE TEMP !!

        # receive the SYN and ACK from the server, the second part of the 3-way handshake
        response = recv() # !! RECEIVE THE MESSAGE HERE TEMP !!

        # send the SYN and ACK to the server and establish the last part of the 3-way handshake
        seq = seq + 1
        # !! ACK = SEQ GIVEN BY SERVER + 1 !! #
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr,protocol,header_len,checksum,source,dest,seq,ack,window,payload_len)
        response = send(header) # !! SEND THE MESSAGE HERE TEMP !!
        return
    
    # responds to a three way handshake initiated by a client socket
    # called by the server
    def respond_three_way_handshake():
        # receive the SYN and ACK from the client, the first part of the 3-way handshake
        response = recv() # !! RECEIVE THE MESSAGE HERE TEMP !!

        # send the SYN and ACK to the client, the second part of the 3-way handshake
        header = create_packet_header(SOCK352_SYN, 0)
        response = send(header) # !! SEND THE MESSAGE HERE TEMP !!

        # receive the SYN and ACK from the client and establish the last part of the 3-way handshake
        response = recv() # !! RECEIVE THE MESSAGE HERE TEMP !!#

        accept()
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
        return bytessent 

    def recv(self,nbytes):
        bytesreceived = 0     # fill in your code here
        return bytesreceived 


    


