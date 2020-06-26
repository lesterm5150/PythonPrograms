import socket
import struct
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print("Connected by", addr)
msz = struct.pack('hhl',1,2,3)
conn.send(msz)
conn.close()
