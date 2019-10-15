
import binascii
import socket as syssock
import struct
import sys
import random
import threading

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from


# Global Variables

# struct to format header data
sock352PktHdrData = "!BBBBHHLLQQLL"
udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
 
# packet header data
version = 0x1 
flags = 0
opt_ptr = 0
protocol = 0
header_len = 0
checksum = 0
source_port = 0
dest_port = 0
sequence_no = 0
ack_no = 0
window = 0
payload_len = 0

# flags for packet headers
SOCK352_FIN = 0x02
SOCK352_SYN = 0x01 
SOCK352_ACK = 0x04
SOCK352_RESET = 0x08
SOCK352_HAS_OPT = 0xA0

sockaddr = ()

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here 
    # save the ports globally in the file
    global receiving_port
    receiving_port = UDPportRx 
    global transferring_port
    transferring_port = UDPportTx

    
    pass 
    
class socket:    
    # initializes the socket and its socks. But it's only one sock, so it needs to find its pair
    def __init__(self):  # fill in your code here 
        # set up the socket
        global sock
        self.sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
        global is_connected
        is_connected = False
        sock352PktHdrData = "!BBBBHHLLQQLL"
        self.udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        return    
    
    # binds a server socket to the given address.
    # called by the server
    def bind(self,address): # called in server1.py ONLY, tuple (IP of server, port number)
        self.sock.bind(address)
        print ("bind")
        return 

    # initiates a 3-way handshake with the server to attempt to create a connection
    # argument is the address in (destination, port) form
    # called by the client
    def connect(self,address):  # fill in your code here 
        if (is_connected):
            return
        global sockaddr
        sockaddr = address
        print(sockaddr)
       
        # send a SYN message to the server to establish the first part of the 3-way handshake
        new_flag = SOCK352_SYN
        new_seq = random.randint(0,100)
        header_len = struct.calcsize(sock352PktHdrData)
        send_SYN = udpPkt_hdr_data.pack(version, new_flag, opt_ptr, protocol, header_len, checksum, source_port, dest_port, new_seq, ack_no, window, payload_len)        
        response = self.sock.sendto(send_SYN, address)
        
        print("Connect() send SYN bytes %d" %(response))

	#receive the SYN and ACK from the server, the second part of the 3-way handshake     
        connection = self.sock.recv(header_len)
        recv_buffer = udpPkt_hdr_data.unpack(connection)
        print ("Connect() recvive SYN ACK Flag %d" %(recv_buffer[1]))
        if (recv_buffer[1] != (SOCK352_ACK)):
            print("incorrect packet")
            return
        
        #Send final ACK to server
        new_seq = recv_buffer[8] + 1 #seq_no + 1
        new_ack = recv_buffer[9] + 1 #ack_no + 1
        new_flag = SOCK352_ACK
        send_ACK = udpPkt_hdr_data.pack(version, new_flag, opt_ptr, protocol, header_len, checksum, source_port, dest_port, new_seq, new_ack, window, payload_len)        
        response = self.sock.sendto(send_ACK, address)
        print("Connect() send ACK and connect")

        self.sock.connect(address)
        # 3-way handshake is done! server socket will accept if it receives the last packet
        return 

    # format a packet header for outgoing packets
    # arguments are the only data that are subject to change: flags, sequece_no. ack_no, payload_len
    # returns the header create by the struct
    def format_header(self, new_flags, new_sequence_no, new_ack_no, new_payload_len):
        header = udpPkt_hdr_data.pack(version, new_flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, new_sequence_no, new_ack_no, window, new_payload_len)
        return header
       
    def listen(self,backlog):
        return

    # responds to a 3-way handshake with a server to establish connection
    # called by the server
    def accept(self):
	# receive a SYN from the client socket, the first part of the 3-way handshake
        global sockaddr
        header_len = struct.calcsize(sock352PktHdrData)
        connection, sockaddr = self.sock.recvfrom(header_len)
        recv_buffer = udpPkt_hdr_data.unpack(connection)
        print ("Accept() receive SYN Flag %d" %(recv_buffer[1]))
        if (recv_buffer[1] != (SOCK352_SYN)):
	    # !! must wait for the correct packet. return for now
            print("incorrect packet")
            return
        


        # send a SYN and a ACK to the client, the second part of the 3-way handshake
        new_flag = SOCK352_ACK
        new_seq = recv_buffer[8]+1
        new_ack = random.randint(0,100)
        send_SYN_ACK = udpPkt_hdr_data.pack(version, new_flag, opt_ptr, protocol, header_len, checksum, source_port, dest_port, new_seq, ack_no, window, payload_len)        
        response = self.sock.sendto(send_SYN_ACK, sockaddr)
        print("Accept() send SYN ACK %d" %(response))
 
        # receive the ACK from the client, the last part of the 3-way handshake
        recieveACK= self.sock.recv(header_len) 
        recv_buffer = udpPkt_hdr_data.unpack(recieveACK)
        if (recv_buffer[1] != (SOCK352_ACK)):
	    # !! must wait for the correct packet. return for now
            print("incorrect packet")
            return
        print("Accept() receive ACK flag %d" %(recv_buffer[1]))
        
	# once the last packet is received, the server can accept the connection
        #(clientsocket, address) = (self.sock, sockaddr)
        return self, sockaddr
    

    def close(self):
	#first host  sends a message with FIN
        header_len = struct.calcsize(sock352PktHdrData)
        flags = SOCK352_FIN
        sequence_no = random.randint(0,100)
        ack_no = 0
        send_FIN = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        print(sockaddr)
        response = self.sock.sendto(send_FIN, sockaddr)
        print("Close() send FIN %d" %(response))

	#another side replies with FIN and ACK bit set     
        connection = self.sock.recv(header_len)
        recv_buffer = udpPkt_hdr_data.unpack(connection)
        print("Close() receive flag %d" %(recv_buffer[1]))

	#first host response with ACK set
        flags = SOCK352_ACK
        ack_no = recv_buffer[9]
        sequence_no = recv_buffer[8] + 1 
        send_ACK = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        ack = self.sock.sendto(send_ACK, sockaddr)
        print("Close() send ack %d" %(ack))
        self.sock.close()
        return 

    def send(self,buffer):
        bytessent = 0
	        

        while bytessent < buffer.len():
            sequence_no += 1
            payload_len #TODO: 64k bytes minus size of header	

            header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
       
            #TODO: take a substring of buffer of payload length
            buffer += header
            bytessent = self.sock.send(msg[bytessent:])
            #TODO: Create a thread that passes the packet and sets timer and waits for ACK, if ACK is not recieved then resent packet
            bytessent = bytessent + sent

        return bytesent 

    #TODO must implement Go-Back-N
    def recv(self,nbytes):
        bytesreceived = 0
        sequence_no = 0
        response = []
        while bytesreceived < nbytes:
            response = self.sock.recv(nbytes-bytesreceived)
            response.append(response)
            bytesreceived = bytereceived + len(response)
        sock.unpack(response)
        return bytesreceived
