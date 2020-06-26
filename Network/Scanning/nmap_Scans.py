from subprocess import Popen, PIPE
import threading

scans = ['half_open','tcp','udp','SCTP','ip_scan','version']
list(enumerate(scans,start = 1))


def scanner(scan_List,port_Range,ip_Range):
    threads =[]
    for scan_type in scan_List:
        t = threading.Thread(target = __nmap_Scan,args =(scan_type,port_Range,ip_Range))
        print '--- Starting : ' + scans[scan_type-1] + ' scan on '+ ip_Range +'---'
        threads.append(t)
        t.start()


def __nmap_Scan(scan_type,port_Range,ips):
    scans = ['half_open','tcp','udp','SCTP','ip_scan','version']
    list(enumerate(scans,start = 1))
    
    if scan_type == 1:
        lpid = Popen(["nmap", "-sS", ips,'-T4','-p '+port_Range], stdout=PIPE)  
    elif scan_type == 2:
        pid = Popen(["nmap", "-sT", ips,'-T4','-p '+port_Range], stdout=PIPE)
    elif scan_type == 3:
        pid = Popen(["nmap", "-sU", ips,'-T4','-p '+port_Range], stdout=PIPE)
    elif scan_type == 4:
        pid = Popen(["nmap", "-sY", ips,'-T4','-p '+port_Range], stdout=PIPE)
    elif scan_type == 5:
        pid = Popen(["nmap", "-sO", ips,'-T4','-p 0-255'], stdout=PIPE)
    elif scan_type == 6:
        pid = Popen(["nmap", "-sV", ips,'-T4','-p '+port_Range], stdout=PIPE)
    else:
        return False
    g = pid.communicate()
    save_Scan(ips+'_'+str(scans[scan_type-1]),g)   
    return True
    
def save_Scan(name,g):
    f = open(name+'.txt', 'wr+')
    for i in g:
            f.write(str(i))
    f.close()
