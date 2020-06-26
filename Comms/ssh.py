#!/usr/bin/python
import paramiko
import getpass
#from paramiko import SSHClient

basic_security_cmds = [
    "no ip http server",
    "no service tcp-small-servers",
    "no service udp-small-servers",
    "no ip domain-lookup",
    "no cdp run",
    "no lldp run",
    "no ip host-routing",
    "exception memory ignore overflow io",
    "exception memory ignore overflow processor"
    ]
def send_and_get_string(command, wait_string, should_print):
    # Send the su command
    shell.send(command + "\n")

    # Create a new receive buffer
    receive_buffer = ""

    while not wait_string in receive_buffer:
        # Flush the receive buffer
        receive_buffer += shell.recv(1024)

    # Print the receive buffer, if necessary
    if should_print:
        print receive_buffer

    return receive_buffer

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip = raw_input("Enter the ip for the switch : ")
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

client.connect(ip, 22, username = user, password = password,allow_agent = False)
shell = client.invoke_shell()
send_and_get_string("", ">", True)
send_and_get_string("enable", ":", True)
send_and_get_string("switch", "#", True)
send_and_get_string("configure terminal","#",True)
for cmd in basic_security_cmds:
    send_and_get_string(cmd,"#",True)

client.close()
