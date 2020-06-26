from scapy.all import *

interface = 'mon0'
def info(fm):
	if fm.haslayer(Dot11):
		if((fm.type == 0) & (fm.type ==12)):
			global i 
			print "Deauth Detected ", i
			i = i+1

sniff(iface=interface,prn = info)





