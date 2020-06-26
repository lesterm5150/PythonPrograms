import socket

def hexConvert(msg):
    ret_str = '' 
    msg = msg.split()
    for i in msg:
        ret_str += '\\x'+i
    return ret_str

UDP_IP = "10.5.20.101"
UDP_PORT = 2345
while(1):
    msg = int(raw_input('Message : '))
    msg = 'a' * msg #raw_input('Message : ')
    
      
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(msg, (UDP_IP, UDP_PORT))
    ack = sock.recv(1024)
    if ack == 'Good':
        continue
    else:
        break
