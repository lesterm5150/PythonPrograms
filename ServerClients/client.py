import socket
import sys
import threading

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
data = "THIS IS AWESOME"
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    rcv = sock.recv(1024)
    print ("Server : {}".format(rcv.decode()))
    
    data = input()
    sock.send(data.encode())

    # Receive data from the server and shut down
    rcv = sock.recv(1024)
    print ("Server : {}".format(rcv.decode()))

    rcv = sock.recv(1024)
    print ("Server : {}".format(rcv.decode()))
    
    rcv = sock.recv(1024)
    print ("Server : {}".format(rcv.decode()))
            
    data = input();
    sock.send(data.encode())

    rcv = sock.recv(1024)
    print ("Server : {}".format(rcv.decode()))

    while(rcv != 'GameOver' and data != 'quit') :
        rcv = sock.recv(1024)
        print ("Server : {}".format(rcv.decode()))
        
        #rcv = sock.recv(1024)
        #print ("Server : {}".format(rcv.decode()))

        data = input();
        sock.send(data.encode())

        rcv = sock.recv(1024)
        print ("Server : {}".format(rcv.decode()))
    
finally:
    sock.close()

