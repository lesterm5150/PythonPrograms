import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port)) #bind server
s.settimeout(5)
data, addr = s.recvfrom(1024)
print(addr,"Now Connected")
print("obtained",data.decode())
s.close()
