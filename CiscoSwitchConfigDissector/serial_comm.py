import serial
import time
import sys
import os
from commands import *

password = sys.argv[1]

mode = 0

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def need_mode(mode_to_be):
    global mode
    
    if mode == mode_to_be:
        return True
        
    elif mode < mode_to_be:
        if mode == 0:
            ser.write('enable\r')
            throw_response()
            ser.write(str(password) + '\r')
            read_response()
            mode = 1
            return True
            
        elif mode == 1:
            ser.write('configure terminal\r')
            read_response()
            mode = 2
            return True
            
    elif mode > mode_to_be:
        if mode == 1 :
            ser.write('disable\r')
            read_response()
            mode = 0
            return True
            
        elif mode == 2:
            ser.write('exit\r')
            read_response()
            mode = 1           
            return True
    else:
        return False
    
    
def get_config():
    need_mode(1)
    ser.write('terminal length 0\r')
    throw_response()
    ser.write('show running-config\r')
    config = throw_response()
    with open('config.txt', 'wr+') as f:
        for line in config[3:-3]:
            f.write(line)
        f.close()
    print ("-- Config Saved in config.txt --")    

def send_commands(cmds):
    for cmd in cmds:
        cmd = cmd + '\r'
        ser.write(cmd)
        read_response()

def read_response():
    lines = ser.readlines()
    for i in lines:
        print i
    return lines
        
def throw_response():
    lines = ser.readlines()
    return lines

def exit():
    need_mode(1)
    ser.write('exit\r')
    throw_response()
       

cls()
print '---- Connecting ----'
ser = serial.Serial('/dev/ttyUSB0',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,None,False)

ser.timeout = 1
ser.write('\r')
time.sleep(2)
cmd = ''
read_response()


while(True):
        cmd = raw_input('> ')
        if cmd.lower() == 'up':
            need_mode(mode+1)
            continue
            
        if cmd.lower() == 'down':
            need_mode(mode-1)
            continue
            
        if cmd.lower() == 'first':
            send_commands(first)
            continue
            
        if cmd.lower() == 'config':
            get_config()
            continue
                
        if cmd.lower() == 'exit' :
            break
        #for cmd in first:
        cmd = cmd + '\r'
        ser.write(cmd)
        read_response()
exit()
ser.close()

 
