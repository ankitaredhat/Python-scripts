mac_list = input("Please enter mac address: ")
print(type(mac_list))

for i in mac_list.split(","):
	print(i + " This"	)

Search_mac.append(x)
for mac in Search_mac:
	print(mac)

	Search_mac = []

def validate_mac(*args):
	for mac in args:
		print(mac + " This"	)

validate_mac(mac_list)
