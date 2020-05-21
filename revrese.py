file_path = r"filepath/abc.txt"

count = 0

with open(file_path,'r') as f:
	for l in f:
		count = count + 1

print("Total: ", count)
