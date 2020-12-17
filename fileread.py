def readFile(filename):
	with open(filename) as f:
		lines = f.read().splitlines()
		return lines