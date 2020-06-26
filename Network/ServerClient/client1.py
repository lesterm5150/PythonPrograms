import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
c = s.recv(1024)
print(c.decode())
c = "Thanks for letting me"
s.send(c.encode())
s.close()
