import os
import collections
import platform
import socket, subprocess, sys
import threading
from datetime import datetime

'''section 1'''

net = raw_input("Enter the Network Address ")
net1 = net.split('.')
print (net1)
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
print(net2)
st1 = int(raw_input("Enter the starting number "))
en1 = int(raw_input("Enter the last number "))
response = raw_input("Would you like to run port scan as well? [Y/N]")
en1 = en1+1
dic = collections.OrderedDict()
oper = platform.system()

if(oper == 'Windows'):
    ping1 = "ping -n 1 "
elif (oper == 'Linux'):
    ping1 = "ping -c 1 "
else :
    ping1 = "ping -c 1 "
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


def run1(st1,en1) :
    for ip in range(st1,en1):
        #print('.')
        addr = net2+str(ip)
        comm = ping1+addr
        response = os.popen(comm)
        for line in response.readlines():
            if(line.count("ttl")):
               break
        if (line.count("ttl")):
            print "-- Scanning --"
            dic[ip] = addr

'''section 4'''

total_ip = en1-st1
tn = 4 #number of ip handled by 1 thread
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
    print "Error: unable to start thread"
print "\t Number of Threads Active :",threading.activeCount()

for t in threads:
    t.join()
print "Exiting main thread"
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print dict[key], "--> Live"
    
t2 = datetime.now()
total = t2-t1
print "Scanning completed in ", total , "s"

if (response == 'n' or response == 'N' or len(dict) == 0):
	print "Closing..."
	sys.exit()

'''section 1 '''
subprocess.call('clear',shell=True)

'''section 2 '''
class myPortThread (threading.Thread):
  def __init__(self,rmip,r1,r2):
      threading.Thread.__init__(self)
      self.rmip = rmip
      self.r1 = r1
      self.r2 = r2
    
  def run(self):
      scantcp(self.rmip,self.r1,self.r2)

'''section 3 '''
def scantcp(rmip,r1,r2):
  try:
    for port in range(int(r1),int(r2)):
      sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.setdefaulttimeout(.5)
      result = sock.connect_ex((rmip,port))
      
      if result==0:
        print "Port Open:-->\t", port
        # print desc[port]
      sock.close()

  except KeyboardInterrupt:
    sys.exit()

  except socket.gaierror:
    print ("Hostname could not be resolved")
    sys.exit()

  except socket.error:
    print ("could not connect to server")
    sys.exit()

'''section 4 '''
print "*"*60
print "\t Port Scanning starting ...\n  "

	#r11 = int(raw_input("\t Enter the start port number: "))
	#r21 = int(raw_input("\t Enter the last port number: "))


for port in dict:
	rmip = dict[port]

	#rmip = socket.gethostbyname(rmserver)

	print "*"*60
	print "Scanner working on", rmip
	print "*"*60
	r11 = 0
	r21 = 65535

	tn =20
	# tn number of port handled by one thread
	t1= datetime.now()
	tp=r21-r11
	tn =30
	# tn number of port handled by one thread
	tnum=tp/tn       # tnum number of threads
	if (tp%tn != 0):
	  tnum= tnum+1

	if (tnum > 300):
	  tn = tp/300
	  tn= tn+1
	  tnum=tp/tn
	  if (tp%tn != 0):
	    tnum= tnum+1

	'''section  5'''
	threads= []

	try:
	  for i in range(int(tnum)):
	    #print "i is ",i
	    k=i
	    r2=r11+tn 
	    if(r2 > 65535):
		r2 = 65535
	    # thread=str(i)
	    thread = myPortThread(rmip,r11,r2)
	    thread.start()
	    threads.append(thread)
	    r11=r2

	except:
	  print ("Error: unable to start thread")

	print "\t Number of Threads active:", threading.activeCount()

	for t in threads:
	  t.join()
	print "Exiting Main Thread"
	t2= datetime.now()
	total =t2-t1
	print "scanning complete in " , total
