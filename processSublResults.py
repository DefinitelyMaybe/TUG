import sys, re

def writeToFile(data):
	sys.stdout.write("Subl refined results:\n\n")
	for i in data:
		sys.stdout.write(i + "\n")

def process(inputArray):
	x = {}
	for i in inputArray:
		x[i] = 1
	writeToFile(x)

def readFile():
	data = []
	for l in sys.stdin:
		x = re.findall("CHANGE_THIS =.*", l)
		if len(x) > 0:
			data += x
	process(data)

readFile()