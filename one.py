def func():
	print("func() is in ONE.PY")

print("TOP LEVEL in ONE.PY")

if __name__ == '__main__':
	print("ONE.PY is being run directly.")
else:
	print("ONE.PY has been imported")
