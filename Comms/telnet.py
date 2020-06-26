#!/usr/bin/python
import telnetlib 
import getpass


ip = raw_input("Enter the ip for the switch : ")
hostname = raw_input("Enter the switch's hostname : ")
user = raw_input("Enter your user name : ")
password = getpass.getpass()
##telnetCmds = ["aaa new-model",
##              "aaa authentication attempts login 3",
##              "username "+user+" secret "+password,
##              "ip domain-name switch.com",
##              "crypto key generate rsa usage-keys modulus 1024",
##              "ip ssh time-out 120",
##              "ip ssh authentication-retries 3",
##              "ip ssh version 2",
##              "line vty 0 15",
##              "transport input ssh"]
##"ip domain-name " + hostname,
##            "enable secret",
##            "line vty 0 15",
##            "password " +password,
##            "login",
##            "service password-encryption",
##            "no ip domain-lookup"
telnetCmds = [
            "aaa new-model",
            "aaa authentication attempts login 3",
            "username "+user+" secret "+password,
            "ip domain-name "+hostname,
            "crypto key generate rsa usage-keys modulus 1024",
            "ip ssh time-out 120",
            "ip default-gateway 10.0.0.1",
            "ip ssh authentication-retries 3",
            "ip ssh version 2",
            "interface vlan 1",
            "ip address 10.0.0.6 255.255.255.0",
            "no shutdown",  
            "exit",
            "service password-encryption",
            "enable secret " +password ,            
            "line vty 0 15",
            "transport input ssh",
            "password " +password,
            "exit",
            "exit",
            "copy running-config startup-config",
            "",
              ]
tn = telnetlib.Telnet(ip)
#tn.read_until("login: ")
#tn.write(user + "\r\n")
##if password:
##   print tn.read_until("Password: ")
##   tn.write(password + "\n")
#tn.write("vt100\r\n")
##print tn.write("enable\n")
##print tn.read_until(":")
##tn.write("cisco\n")
print tn.read_until("#")
tn.write("configure terminal\n")
for cmd in telnetCmds :
   print (tn.read_until ("#"))
   tn.write(cmd+"\n")
print tn.read_until("#")
tn.write("exit")
