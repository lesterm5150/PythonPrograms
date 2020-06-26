import collections
import platform
import socket, subprocess, sys
import threading
from datetime import datetime

'''section 1'''

net = input("Enter the Network Address ")
net1 = net.split('.')
print (net1)
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
print(net2)
st1 = int(input("Enter the starting number "))
en1 = int(input("Enter the last number "))
en1 = en1+1
dic = collections.OrderedDict()
t1 = datetime.now()


'''section 2'''
class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st,self.en)

'''section 3'''
def scan(addr) :
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr,445))
    if result == 0 :
        return 1
    else :
        return 0

def run1(st1,en1) :
    #print("Scanning started...")
    for ip in range(st1,en1):
        #print('.')
        addr = net2+str(ip)
        if(scan(addr)):
            dic[ip] = addr

'''section 4'''

total_ip = en1-st1
tn = 20 #number of ip handled by 1 thread
total_thread = total_ip/tn
total_thread = total_thread+1
threads = []
try:
    for i in range(int(total_thread)):
        en = st1 +tn
        if(en>en1):
            en = en1
        thread = myThread(st1,en)
        thread.start()
        threads.append(thread)
        st1 = en
except :
    print("Error: unable to start thread")
print("\t Number of Threads Active :",threading.activeCount())

for t in threads:
    t.join()
print("Exiting main thread")
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print (dict[key], "--> Live")
    
t2 = datetime.now()
total = t2-t1
print ("Scanning completed in ", total , "s")
       
