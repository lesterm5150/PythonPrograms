import os
import socket,sys,subprocess
from uuid import getnode as get_mac

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 35093, struct.pack('256s',
                                ifname[:15]))[20:24])
                                
    def get_interface_mask(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 35099, struct.pack('256s',
                                ifname[:15]))[20:24])
                                
def check_len(mac):
    if len(mac) < 12 :
        x = 12 - len(mac)
        mac = '0' *x +mac
    return mac

def plain_mac(mac):
    sor = str(hex(mac))
    sor = sor[:-1]
    if(len(sor) <= 13) :
        sor = '0' + sor[2:]
    else :
        sor = sor[2:]
    sor = check_len(sor)
    return sor

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
  
def get_host_ip(ip):
        ip = str(ip)
        host = ip.split('.')
        host = host[0] +'.'+host[1]+'.'+host[2]+'.1'
        return host

def binary(ls):
        ls2 = []
        for i in ls:
                ls2.append(bin(i)[2:].zfill(8))
        return ls2              

def get_ips(mask):

        net_class = ''

        mask =map(int, mask.split('.'))
        b_mask = binary(mask)
        mask_s = ('').join(b_mask)
        
       
        if mask[0] != 255:
                net_class = 'A'              
        elif mask[0] < 192:
                net_class = 'B'
        else:
                net_class = 'C'
                
        bits_borrowed = mask_s.count('1')
        bits_unborrowed = mask_s.count('0')  
             
        subnets = '/'+str(bits_borrowed)
        hosts = (2**int(bits_unborrowed)) - 2

        return subnets,hosts
