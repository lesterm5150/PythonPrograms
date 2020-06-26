import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server
s.listen(2)
while True:
	conn, addr = s.accept()
	print(addr,"Now Connected")
	c = "Thanks for connecting"
	conn.send(c.encode())
	c = conn.recv(1024)
	print(c.decode())
	conn.close()
