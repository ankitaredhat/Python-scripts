'''
This is the progran to check entered nuber is prime number or not
'''

def check_prime(num):
	if num > 1 :
		for item in range(2,num):
			if (num % item) == 0:
				print(" This is not a prime number")
				break
		else:
			print(" This is a prime number")
	else:

		print("The entered number {} is not prime number".format(num))

number = int(input("Please enter any number: "))

check_prime(number)
