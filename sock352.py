
import binascii
import socket as syssock
import struct
import sys
import random

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
header_len = udpPkt_hdr_data.size
checksum = 0
source_port = 0
dest_port = 0
sequence_no = 0
ack_no = 0
window = 0
payload_len = 0

# flags for packet headers
 
SOCK352_FIN = 0x02
SOCK352_SYN = 1 
SOCK352_ACK = 4
SOCK352_RESET = 8
SOCK352_HAS_OPT = 160

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
        return
    
    
    # binds a server socket to the given address.
    # called by the server
    def bind(self,address): # called in server1.py ONLY
        self.sock.bind(address)
        print ("bind")
        return 


    # initiates a 3-way handshake with the server to attempt to create a connection
    # argument is the address in (destination, port) form
    # called by the client
    def connect(self,address):  # fill in your code here 
        if (is_connected):
            return
	print(address)
        # send a SYN message to the server to establish the first part of the 3-way handshake
        new_flag = SOCK352_SYN
        new_seq = random.randint(0,100)
        send_SYN = udpPkt_hdr_data.pack(version, new_flag, opt_ptr, protocol, header_len, checksum, source_port, dest_port, new_seq, ack_no, window, payload_len)
        response = self.sock.send(send_SYN, address[1])
        
        print("send syn: response " + response + "header_len " + header_len)	

        if (response < sys.getsizeof(buffer)):
            # !! must resend and try again. return for now
            return

        # receive the SYN and ACK from the server, the second part of the 3-way handshake
        response = sock.recv(header_len) 
        recv_buffer = udpPkt_hdr_data.unpack(response)
        if (recv_buffer[1] != (SOCK352_ACK + SOCK352_SYN)):
            # !! must wait for the correct packet. return for now
            return
 
        # send the ACK to the server and establish the last part of the 3-way handshake
        new_seq = recv_buffer[9] #seq_no
        new_ack = recv_buffer[8] + 1 #ack_no + 1
        buffer = self.format_header(new_flag, new_seq, new_ack, 32)
        response = self.send(buffer)
        if (response < sys.getsizeof(buffer)):
            # !! must resend and try again. return for now
            return

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
        response = self.recv(header_len) 
        if (recv_buffer[1] != (SOCK352_SYN)):
			# !! must wait for the correct packet. return for now
            return

        # send a SYN and a ACK to the client, the second part of the 3-way handshake
        recv_buffer = udpPkt_hdr_data.unpack(response)
        new_flag = SOCK352_SYN + SOCK352_ACK
        new_seq = random.randint(0,100)
        new_ack = recv_buffer[9] + 1 # seq_no + 1
        buffer = format_header(new_flag, new_seq, new_ack, 32)
        response = self.send(buffer)
        if (response < sys.getsizeof(buffer)):
			# !! must resend and try again. return for now
            return

        # receive the ACK from the client, the last part of the 3-way handshake
        response = self.recv(header_len) 
        if (recv_buffer[1] != (SOCK352_SYN)):
			# !! must wait for the correct packet. return for now
            return

        # once the last packet is received, the server can accept the connection
        (clientsocket, address) = (self, receiving_port)  # change this to your code 
        return (clientsocket,address)
    

    def close(self):
	#first one side sends a message with FIN
        format = '!BBBBHHLLQQLL'
        flags = SOCK352_FIN
        header_len = struct.calcsize(format)
        sequence_no = random.randint(0,9)
        ack_no = 0
        payload_len = 0

        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)

        self.sock.send(header);

        self.sock.recv(ack, header_len)
	#another side replies with FIN and ACK bit set
        waitingForAck = true;
        ack = ''
        while waitingForAck:
                response = udpPkt_hdr_data.unpack(ack)
                if response[1] == SOCK352_FIN:
                        #first side replies with ACK set
                        flags = SOCK352_ACK
                        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
                        socket.send(header); 
                        socket.close()
                        waitingForAck = false;
       
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
