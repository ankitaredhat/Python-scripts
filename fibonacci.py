def fibonacci(N):
	a = 0
	b = 1
	for i in range(N):
		yield a
		a,b = b, a+b

	return a

value = int(input("Please enter number: "))
for item in fibonacci(value):
	print(item)
