import socket
host = "127.0.0.1" # server address
port = 2345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)

s.bind((host,port)) #bind server

data, addr = s.recvfrom(1024)
print(addr,"Now Connected")
s.sendto('Good',addr)
print "obtained : " + data 
s.close()
