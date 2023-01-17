import pickle 
from hashlib import sha1
from socket import IP_TOS
from string import hexdigits

# from matplotlib.colors import hexColorPattern
# from termcolor import colored

class Packet_reciever:
    def __init__(self, ack, seq_num): 
        self.seq_num = seq_num
        self.ack = ack
        self.type = 'has_ack'
        self.checksum = sha1(ack).hexdigest()
              
    def check(self):
        return self.checksum == sha1(self.ack).hexdigest()

class Packet_sender:
    def __init__(self, data, type, seq_num, ip, port): 
        self.data = data
        self.seq_num = seq_num
        self.ip = ip
        self.port = port
        self.type = type
        self.checksum = sha1(data).hexdigest()    
              
    def check(self):
        return self.checksum == sha1(self.data).hexdigest()

# if __name__ == '__main__':
#     msg = "Helloo I am data"
#     msg = msg.encode('utf-8')

#     pk = Packet("found", msg, 'ACK', 1)
#     print("Status : {}".format(pk.status))
#     print("Ack : {}".format(pk.ack))
#     print("seq_num : {}".format(pk.seq_num))
#     print("data : {}".format(pk.data))
#     print("checksum : {}".format(pk.checksum))
#     print("******CHECK SUM ******")
#     cal_checksum = pk.check()
#     print("Claculated sum : {}".format(sha1(pk.data.decode('utf-8')).hexdigest()))

#     if cal_checksum:
#         print("data not corrupted")
#     else:
#         print("corrupted !!")