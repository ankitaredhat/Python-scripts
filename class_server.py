import paramiko
import getpass

class Server():
	user = 'userid'

	def __init__(self,hostname):
		self.hostname = hostname


	def check_host(self):

		while True:
			try:
				print("Please wait creating ssh client...")
				ssh_client = paramiko.SSHClient()
				ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
				print("Please wait, connecting with remote server")
				ssh_client.connect(hostname = host, username = self.user)
				print("==============================")
				print("Hostame:{}".format(host))
				print("==============================")
				print("Date & Uptime:")
				cmd = 'date;uptime'
				stdin,stdout,stderr = ssh_client.exec_command(cmd)
				output = stdout.readlines()
				print("\n".join(output))
				cmd1 = 'command'
				stdin1,stdout1,stderr1 = ssh_client.exec_command(cmd1)
				print("Please wait, Executing commnand on remote server")
				stdout_vm = stdout1.readlines()
				print("======================================")
				print("Running VM's status on {}".format(host))
				print("======================================")
				print("\n".join(stdout_vm))
				vmstatus_file.write("\n".join(stdout_vm))
				print("Successfully executed command on a remote server.")
				ssh_client.close()		
			except:
				print("[!] Cannot connect to the SSH Server")
				out_file.write("Could not connect to " + host + "\n")
				break
			else:
				break

in_file = open("filename of host", mode="r")	
vmstatus_file = open("status.txt",'w')
out_file = open("Connection_Failed.txt", mode='w')

for host in in_file:
		host=host.strip()
		print("======================================")
		print ("Checking server",host)
		myserver = Server(host)
		myserver.check_host()


vmstatus_file.close()

