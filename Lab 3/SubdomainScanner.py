import json
import urllib
import subprocess

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

if __name__ == '__main__':
    target_domain = raw_input("Enter domain to check: ")
    n = checkPing(target_domain)
    if n == True:
        url = "https://www.virustotal.com/vtapi/v2/domain/report"
        parameters = {'domain': target_domain, 'apikey': 'cde2010916d494d60ac2a0588b45d490ae68abc149c6b8ef73232cc7b19339ca'}
        response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
        response_dict = json.loads(response)
        print "Subdomain of " + target_domain +" is: "
        for subdomain in response_dict['subdomains']:
            print subdomain