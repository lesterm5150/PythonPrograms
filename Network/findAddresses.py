import os
import collections
import platform
import socket, subprocess, sys
import threading
from datetime import datetime



def findAddresses(gatewayIp) :
	class myThread(threading.Thread):
	    def __init__(self,st,en):
		threading.Thread.__init__(self)
		self.st = st
		self.en = en
	    def run(self):
		run1(self.st,self.en)


	def run1(st1,en1) :    
	    for ip in range(st1,en1):
		addr = net2+str(ip)
		comm = ping1+addr
		response = os.popen(comm)
		for line in response.readlines():
		    if(line.count("ttl")):
		       break
		if (line.count("ttl")):
		    dic[ip] = addr

	net = gatewayIp
	net1 = net.split('.')
	a = '.'
	net2 = net1[0]+a+net1[1]+a+net1[2]+a
	st1 = 1
	en1 = 99
	en1 = en1+1
	dic = collections.OrderedDict()
	oper = platform.system()
	print "Scanning started on --> " + gatewayIp
	if(oper == 'Windows'):
	    ping1 = "ping -n 1 "
	elif (oper == 'Linux'):
	    ping1 = "ping -c 1 "
	else :
	    ping1 = "ping -c 1 "
	t1 = datetime.now()

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
	    
	t2 = datetime.now()
	total = t2-t1
	print "Scanning completed in ", total , "s"
	return dic
       
