#mrpilot 
#https://github.com/pilot-hack
#install => pip install -r requirements.txt

import socket
import os
import platform
import colorama
import time
class colorma:

    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

	
def clear():

   plat = platform.uname()[0]

   if plat == "Linux":
        os.system("clear")
   elif plat == "Windows":
        os.system("cls")
plat = platform.uname()[0]



print(colorma.YELLOW+"\n\t [wating...]")
time.sleep(2)

clear()

# print red color for all texts
print(colorma.RED)
print("\n[#10٪]")
time.sleep(0.2)
print("\n[##15٪]")
time.sleep(0.2)
print("\n[###20٪]")
time.sleep(0.2)
print("\n[####25٪]")
time.sleep(0.2)
print("\n[#####30٪]")
time.sleep(0.2)
print("\n[######35٪]")
time.sleep(0.2)
print("\n[#######40٪]")
time.sleep(0.2)
print("\n[########45٪]")
time.sleep(0.2)
print("\n[#########50٪]")
time.sleep(0.2)
print("\n[##########55٪]")
time.sleep(0.2)
print("\n[###########60٪]")
time.sleep(0.2)
print("\n[############65٪]")
time.sleep(0.2)
print("\n[#############70٪]")
time.sleep(0.2)
print("\n[##############75٪]")
time.sleep(0.2)
print("\n[###############80٪]")
time.sleep(0.2)
print("\n[################85٪]")
time.sleep(0.2)
print("\n[#################90٪]")
time.sleep(0.2)
print("\n[##################95٪]")
time.sleep(0.2)
print("\n[###################100٪]")
time.sleep(0.2)

clear()

#--------------------Baner-------------------#	

print(f"""{colorma.RED} 
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│                ██████╗ ██╗██╗      ██████╗ ████████╗               │
│                ██╔══██╗██║██║     ██╔═══██╗╚══██╔══╝               │
│                ██████╔╝██║██║     ██║   ██║   ██║                  │
│                ██╔═══╝ ██║██║     ██║   ██║   ██║                  │
│                ██║     ██║███████╗╚██████╔╝   ██║                  │
│                ╚═╝     ╚═╝╚══════╝ ╚═════╝    ╚═╝                  │
│                                                 Boot Script 2.0    │
└────────────────────────────────────────────────────────────────────┘

             ╭ ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╮                  
            ◄ https://github.com/pilot-hack  ► 
             ╰ ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╯             
""")

#------------------Script------------------#

domain = input(f"{colorma.CYAN} address site [ org-com-ir-net ] > {colorma.RED}").lower()
print(f"{colorma.CYAN}")
domain = domain.replace("http://","")
domain = domain.replace("https://","")
domain = domain.replace("www.","")

if domain[-3:] == "ir" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server =  "whois.iana.org"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((whois_server,43))

s.send((domain+"\r\n").encode())

msg = s.recv(10000)

print(msg.decode())
