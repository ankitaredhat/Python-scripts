import os
import sys
import re

#This script must be run as root! It validate the MAC address format 

def check_privilege():
	
	if os.geteuid()!= 0:
		sys.exit('This script must be run as root!')
	else:
		print("You have root privileges. You can run the script! ")


Search_mac = []

def validate_mac(mac):
		try:
			valid_mac = re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac.lower()).group()
			if (bool(valid_mac)):
				print("MAC Address : {} ".format(valid_mac))
				print("Valid MAC address!!")
				return Search_mac.append(valid_mac)
		except:
			print("MAC: {}".format(mac))
			print("Incorrectly formatted MAC address.  Please check the address")
			
check_privilege()
mac_list = input("Please enter mac address: ")
for item in mac_list.split(","):
	validate_mac(item)
for mac in Search_mac:
	print(mac + " added in valid mac list")
