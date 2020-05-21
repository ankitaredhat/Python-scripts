def check_vowel(string,vowel):
	final = [each for each in string if each in vowel] 
	if len(final) > 0:
		print("Vowel Found")
	else:
		print("Not found")

name = input("Enter your name: ")
print(name)
vowel = "AEIOUaeiou"
check_vowel(name,vowel)


#mystring = [ letter for letter in name.lower() ]
#print(mystring)
'''for char in mystring:
	if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
		print("Vowel found")
	else:
		print("Not found")	'''
