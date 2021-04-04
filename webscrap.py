#!/usr/bin/python
# -*- coding: utf-8 -*-

#import modules required
import socket
import sys
import os
import subprocess
from bs4 import BeautifulSoup
import requests

#function to find ip address
def findip():
    url=input("Enter the URL : ")
    try:
        ip=socket.gethostbyname(url)
        print("IP Found  : ",ip)
    except:
        print("URL Not Found")

#function for port scanning
def pscan():
    target=input("Enter The host to be scan : ")
    port=80
    port=int(input("Enter the Port You want scan (default is 80)) : "))
    print("*"*50)
    print("Target : ",target,"at port",port)
    ip=socket.gethostbyname(target)
    print("Target IP : ",ip)
    print("Port      : ",port)
    print("*"*50)
    try:
        print("Scanning Started.....\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("[+] Port {} is open".format(port))
        else:
            print("[+] Port {} is closed".format(port))
        s.close()

    except KeyboardInterrupt:
        print("\n Exitting Keyboard Interrupt by User !")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Error !")
        sys.exit()
    except socket.error:
        print("\n Server not responding !")
        sys.exit()

#function to find hidden directories
def dirb():
    url=input("Enter the URL to scan : ")
    path="./directories.txt"
    path=input("Enter the wordlist path :")
    print("*"*50)
    print("Scanning Target : ",url)
    ip=socket.gethostbyname(url)
    print("Target IP : ",ip)
    print("*"*50)
    print("[+] reading the wordlist.....")
    try:
        with open(path) as file:
            check=file.read().strip().split("\n")
            print("[+] SUCCESS ")
            print("[->] TOTAL NUMBER OF PATHS TO BE CHECKED : ",str(len(check)))
    except IOError:
        print('[-] FAILED ')
        print('[-] Could not read the wordlist specified try again')
        sys.exit(1)
    print("[+] Begin scanning....")
    for i in range(len(check)):
        URL='http://'+url+'/'+check[i]
        try:
            r = requests.head(URL)
            code=r.status_code
        except requests.ConnectionError:
            print("Connection Error")
        if(code == 200 or code == 301 or code == 403):
            print("[->]",URL," :[",code,"]")
    print('\n Scan completed....')

#function to find any interesting links or addresses
def interesting():
    url=input("Enter the URL : ")
    print("[+] Fetching interesting links.....")
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        lin=link.get('href')
        if(lin.startswith('http')):
            print("->",lin)
    print("[+] Fetching Completed Succesfully...")

print("-"*50)
print("|           Webscraping tool by Samit            |")
print("-"*50)
print("*"*50)
print('1: Find IP address for a website')
print('2: Check port status')
print('3: Directories Extracter(Wordlist required)')
print('4: Check for any interesting links or contents hidden in webpage')
print("*"*50)

#main function
option=int(input("Enter the Option :"))
if(option == 1 ):
    findip()
elif(option == 2):
    pscan()
elif(option == 3):
    dirb()
elif(option == 4):
    interesting()
else:
    print("Invalid option")
