import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server
s.listen(1)
conn, addr = s.accept()
print(addr,"Now Connected")
c = "Thanks"
conn.send(c.encode())
conn.close()
