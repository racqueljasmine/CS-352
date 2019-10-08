
import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

#  
def init(UDPportTx,UDPportRx):   # initialize your UDP socket here 
    pass 
    
class socket:
    
    def __init__(self):  # fill in your code here 
        return
    
    def bind(self,address):
        return 

    def connect(self,address):  # fill in your code here 
        return 
    
    def listen(self,backlog):
        return

    # "Cheating" by returning its own socket
    def accept(self):
        (clientsocket, address) = (1,1)  # change this to your code 
        
        return (self.address)
    
    def close(self):   # fill in your code here 
        return 

    def send(self,buffer):
        bytessent = 0     # fill in your code here 
        return bytesent 

    def recv(self,nbytes):
        bytesreceived = 0     # fill in your code here
        return bytesreceived 


    


