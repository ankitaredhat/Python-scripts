import sys

def add(x):
	return x


x = input("Enter number to be added: ")
print("The name of the program is ", sys.argv[0])


if len(x) < 1 	:
	print("No args passed")
else:
	print(add(x))
