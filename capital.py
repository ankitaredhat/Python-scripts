file_path = r"filepath/python/abc.txt"

count = 0

text = countletter.read()
for character in text:
	if character.isupper():
		count += 1
print("Total: ", count)
