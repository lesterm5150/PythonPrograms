import socket
host = "192.168.2.10" # server address
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port)) #bind server
data, addr = s.accept()
print(addr,"Now Connected")
print("obtained",data.decode())
s.close()
