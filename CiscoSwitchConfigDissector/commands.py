banner_motd = '$  $'

extra_services = {
    'ip scp server enable',
    'no ip http secure-server',
    'no ip http server',
    'no ip finger',
    'ip dhcp bootp ignore',
    'no ip domain-lookup',
    'no service pad',
    'no cdp run',
    'no lldp run',
    'tcp-keepalive-in',
    'tcp-keepalive-out',
    'no service config',
    'no ip redirects',
    'ip options drop',
    'no ip source-route'
}

passwords = {
    'enable secret', #<secret>
    'service password-encryption'
}

aaa = {
    'aaa new-model',
    'aaa authentication attempts login', #<max attempts>
    'aaa authentication login default local',
    'username secret', #<username> .. <secret>
    'no service password-recovery'
}

mem_opts = {
    'memory free low-watermark processor', # <threshold>
    'memory free low-watermark io', # <threshold>
    'memory reserve critical' # <threshold>
}

logging = {
    'logging buffered', # <bytes> <severity>
    'no logging console',
    'no logging monitor'
}

source_guard = {
    'ip dhcp snooping',
    'ip dhcp snooping vlan', #<vlan range>
    'ip arp inspection vlan' #<vlan range>
}

management = {
    'hostname', #<name>
    'ip domain-name', #<example.com>
    'crypto key generate rsa modulus', #<size of key>
    'ip ssh time-out', #<seconds>
    'ip ssh authentication-retries', #<num retries>
    'line vty 0 15',
    'transport input ssh',
    'exec timeout' #<timeout>
}

vlan = {
    'vlan', #<number>
    'name' #<name>
}
    
class ports:
   def __init__(self):
       self.size = 0
       self.port_list = []
       self.fast_eth = []
       self.gig_eth = []

