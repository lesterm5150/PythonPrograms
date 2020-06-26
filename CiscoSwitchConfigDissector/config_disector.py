from Tkinter import *
def find_line(config, sub):
    for line in range(0,len(config)-1):
        if sub in config[line]:
            return config.pop(line)
  
def find_ports(config,port_name):
    sub = 'interface'
    ports = []
    num_ports = 0
    for line in range(0,len(config)-1):
        if sub in config[line]:
            eth=''
            props = []
            if port_name in config[line]: 
                eth = config[line]
                config[line] =''
                num_ports +=1
                del props[:]
                while config[line+1].strip() != '!':
                    props.append(config[line+1].strip())
                    config[line+1] =''
                    line += 1

                ports.append((eth,props))
    return num_ports,ports

def find_lines(config,sub):
    text=''
    for line in range(0,len(config)-1):
        if sub in config[line]:
            text += config[line]
            config[line] =''
            while config[line+1] != '!':
                text += config[line+1]
                config[line+1] =''
                line+=1
    return text
    
def find_all(config,sub):
    al = []
    for line in range(0,len(config)-1):
        if sub in config[line]:
            al.append(config[line])
            config[line] = ''
    return al

        
def find_con_lines(config,sub):
    lines= []
    
    num_ports = 0
    for line in range(0,len(config)-1):
        eth = ''
        props=[]
        if sub in config[line]:
            eth = config[line]
            config[line] =''
            del props[:]
            while sub not in config[line+1] and '!' not in config[line+1]:
                props.append(config[line+1].strip())
                config[line+1] =''
                line += 1

            lines.append((eth,props))
    return lines

def trim(config):
    
    conf = map(lambda each:each.strip('!'), config)
    conf = filter(None,conf)
    return conf
        
class config_interp:
    def __init__(self,config):
        self.size = config.pop(0) #str
        self.version = find_line(config,'version') # str
        self.hostname = find_line(config, 'hostname') # str
        self.user = find_line(config, 'username') # str
        self.en_secret = find_line(config, 'enable secret') # str
        
        self.num_fast_ports,self.fast_ports =(
            find_ports(config,'FastEthernet')) # int | str, list
            
        self.num_gig_ports,self.gig_ports =( 
            find_ports(config, 'GigabitEthernet')) # int | str, list
            
        self.num_vlans,self.vlans = find_ports(config,'') # int | str, list
        self.default_gateway = find_line(config,'default-gateway') #str
        self.motd = find_lines(config, 'banner motd') # str
        self.lines = find_con_lines(config,'line') # str , list
        self.crypto = find_con_lines(config,'crypto')
        
        self.logging = find_all(config,'log') # list
        self.boot_list = find_all(config,'boot') # list
        self.memory = find_all(config,'memory') # list
        self.clock_opts = find_all(config,'clock') # list 
        self.services = find_all(config,'service') # list
        self.ip_opts = find_all(config,'ip') # list
        self.aaa = find_all(config,'aaa') # list
        self.access_lists = find_all(config,'access-list') # list
        self.extras = trim(config) # list
        
with open('config.txt','r') as f:
    config1 = f.read().splitlines()
    f.close()

def test():
    my_conf = config_interp(config1)

    #attrs = vars(my_conf) #all vars of a class
    #for attribute, value in attrs.items():
    #    print attribute + ': '
    #    print value
    display(my_conf)
    #for i,x in my_conf.crypto:
    #    print i +' : '
    #    print x
    #    print ''
    #print my_conf.services
    #print my_conf.ip_opts
    #for i in my_conf.extras:
    #    print i
    
def display(conf):
    rt = Tk()
    
    
    
    """
    t =[]
    extra_l = Label(rt, text='Extra Settings', fg = 'red').pack()
    
    for j in range(0,len(conf.extras)):
        t.append(Text(rt, height=1, width=50))
        t[j].pack()
        t[j].insert(END, conf.extras[j]+'\n')
     """   
        
    mainloop()
    
    










test()

