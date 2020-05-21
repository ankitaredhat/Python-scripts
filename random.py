import random

fname1 = r"/filepath/python/abc.txt"

def read_random(fname):
	lines = open(fname).read().splitlines()
	return random.choice(lines)
print(read_random (‘fname1’))
