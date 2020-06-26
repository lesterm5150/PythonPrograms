import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
buf = bytearray(b"-" * 30)
#c = s.recv(1024)
print("Num of bytes", s.recv_into(buf))
print(buf.decode())
s.close()
