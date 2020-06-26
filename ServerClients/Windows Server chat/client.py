import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try : 
    clientsocket.connect(('localhost', 5000))
    print("Server connection succesful...")
except :
    print("Server connection failed...")
    
sendStr = ''
while(sendStr != 'quit') :
    sendStr = input()
    clientsocket.send(sendStr.encode())
