import os
import platform
from datetime import datetime

net = raw_input("Enter the Network Address ")
net1 = net.split('.')
print net1
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
print net2
st1 = int(raw_input("Enter the starting number "))
en1 = int(raw_input("Enter the last number "))
en1 = en1+1

oper = platform.system()

if(oper == 'Windows'):
    ping1 = "ping -n 1 "
elif (oper == 'Linux'):
    ping1 = "ping -c 1 "
else :
    ping1 = "ping -c 1 "

print('Scanning now...')
t1  = datetime.now()
for ip in range(st1,en1):
       addr = net2+str(ip)
       comm = ping1+addr
       response = os.popen(comm)
       for line in response.readlines():
           if(line.count("TTL")):
               break
       if (line.count("TTL")):
       	print addr, "--> LIVE"
t2 = datetime.now()
total = t2-t1
print "Scanning completed in ", total , "s"
       
