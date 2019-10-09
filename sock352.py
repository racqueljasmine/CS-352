
import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here 
    pass 
    
class socket:
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

    SOCK352_FIN = 0x02
    SOCK352_ACK = 0x04

    sock

    def __init__(self):  # fill in your code here 
        return
    
    def bind(self,address):
        return 

    def connect(self,address):  # fill in your code here 
        return 
    
    def listen(self,backlog):
        return

    def accept(self):
        (clientsocket, address) = (1,1)  # change this to your code 
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
        sock352PktHdrData = '!BBBBHHLLQQLL'
        udpPkt_hdr_data = struct.Struct(socket352PktHdrData)
        header_len = struct.calcsize(format)
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
