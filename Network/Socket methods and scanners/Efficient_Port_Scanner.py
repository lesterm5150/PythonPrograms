import threading
import time
import socket, subprocess,sys
from datetime import datetime
#import shelve

'''section 1 '''
subprocess.call('clear',shell=True)
#shelf = shelve.open("lester")
#data=(shelf['desc'])

'''section 2 '''
class myThread (threading.Thread):
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
        print ("Port Open:-->\t", port)
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

  #shelf.close()
'''section 4 '''
print ("*"*60)
print ("\t Welcome this is the Port scanner\n  ")

rmip = input("\t Enter the IP Address  to scan:  ")

#rmip = socket.gethostbyname(rmserver)
r11 = int(input("\t Enter the start port number: "))
r21 = int(input("\t Enter the last port number: "))


print("Scanner working on", rmip)
print("*"*60)
t1= datetime.now()
tp=r21-r11

tn =20
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
    # thread=str(i)
    thread = myThread(rmip,r11,r2)
    thread.start()
    threads.append(thread)
    r11=r2

except:
  print ("Error: unable to start thread")

print ("\t Number of Threads active:", threading.activeCount())

for t in threads:
  t.join()
print ("Exiting Main Thread")
t2= datetime.now()

total =t2-t1
print ("scanning complete in " , total)
