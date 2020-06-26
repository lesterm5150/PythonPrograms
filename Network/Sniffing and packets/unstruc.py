import socket
import struct
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
msg = s.recv(1024)
print(msg.decode())
print (struct.unpack('hhl',msg))
s.close()
