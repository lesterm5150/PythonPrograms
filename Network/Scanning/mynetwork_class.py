from network_methods import *
from subprocess import Popen, PIPE
import threading

class My_Network(): 
    def __init__(self):
        self.mac = plain_mac(get_mac())
        self.ip = get_lan_ip()
        self.mask = get_interface_mask("eth0")
        self.host = get_host_ip(self.ip)
        self.CIDR_mask ,self.num_hosts = get_ips(self.mask)
        self.CIDR_notation = self.ip+self.CIDR_mask
        
    def show(self):
            print 'Mac address                   : ' + self.mac
            print 'Ip address                    : ' + self.ip
            print 'Host address                  : ' + self.host
            print 'Subnet mask                   : ' + self.mask
            print 'CIDR notation                 : ' + self.CIDR_notation
            print 'Possible # of hosts in subnet : ' + str(self.num_hosts)
            
    def discover_Network(self):
        pid = Popen(["nmap", "-sS", self.CIDR_mask,'-T4','-p 80'], stdout=PIPE)
        g = pid.communicate()
        save_Scan(self.ip,g)
        
    def scan_Network(self):
        pid = Popen(["nmap", "-sS", self.CIDR_mask,'-T4','-p 0-65535'], stdout=PIPE)
        g = pid.communicate()
        save_Scan(self.ip,g)
        
def save_Scan(name,g):
    f = open(name+'.txt', 'wr+')
    for i in g:
            f.write(str(i))
    f.close()
        
mine = My_Network()
mine.show()
#mine.discover_Network()
