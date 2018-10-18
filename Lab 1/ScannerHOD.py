import os
import subprocess
import datetime
import ipaddress
import threading
import time

def checkPing(target_ip):
    flag = False
    cmd = subprocess.Popen(["ping",target_ip,"-c","1"], stdout= subprocess.PIPE)
    stdout = cmd.communicate()
    if stdout[0].find("0% packet loss") != -1:
        print target_ip + " is live xD"
        flag = True
    else:
        print target_ip + " is down :("
    return flag

def convertCIDRToIPList(cidr):
    ip_object = ipaddress.ip_network(u''+cidr)
    ip_list = []
    for ip in ip_object:
        ip_list.append(str(ip))
    return ip_list

def scanPort(ip):
    start_time = time.time()
    print "Opening TCP ports: "
    for x in range(1,65536):
        cmd_TCP = subprocess.Popen(["nc","-z","-v","-w","1",ip,str(x)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = cmd_TCP.communicate()[1]
        if "open" in output:
            output = output.split(" ")
            print "Port " + output[8] + " " + output[9] + " open."
    end_time = time.time()
    print "Duration: " + str(end_time - start_time)

if __name__ == '__main__':
    target_ip = raw_input("Enter IP to check: ")
    ip_list = []
    if target_ip.find("/") != -1:
        ip_list = convertCIDRToIPList(target_ip)
    else:
        ip_list.append(target_ip)
    for ip in ip_list:    
        n = checkPing(ip)
        if n == True:
            scanPort(ip)


