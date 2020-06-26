import socket
host = "192.168.100.2" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server
s.listen(2)
while 1:
    conn, addr = s.accept()
    print(addr,"Now Connected")
    c = conn.recv(1024)
    print(c.decode())
    h = "Thanks for connecting  \r"
    conn.send(h.encode())
    conn.close()
