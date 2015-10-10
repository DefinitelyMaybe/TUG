import re, pathlib

#set the following to your own desire
#To reduce the scope of the data change the path to just the folder you're interested in
myTUGpathToData = "C:/Program Files (x86)/Steam/steamapps/common/TUG/Game/Core/Data/"
outputFileName = "test.txt"
includeValues = False
labelOfInterest = "EVERYTHING" #"EVERYTHING"
catchExtraLabels = False

class Node(object):
	"""ADT for the TUGschematic for dealing with labels in a tree-like fashion"""
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
		self.children = []

	def __repr__(self):
		return self.value

	def addChild(self, x):
		if x not in self.children:
			self.children += [x]
		
class TUGschematic(object):
	def __init__(self, x):
		self.currentLevel = 0
		self.previousLevel = 0

		self.currentLabel = None

		self.variables = {} #holds the variables and if chosen, associated values
		self.labels = {} #holds labels and associated variables

		self.processLines(x)

	def addVariable(self, x):
		if (self.currentLabel in self.labels):
			if x not in self.labels[self.currentLabel]:
				self.labels[self.currentLabel] += [x]
		else:
			self.labels[self.currentLabel] = [x]

	def addValue(self, var, value):
		if (var in self.variables):
			if value not in self.variables[var]:
				self.variables[var] += [value]
		else:
			self.variables[var] = [value]

	def processLines(self, x):
		pickUpLabel = False
		print("Number of lines: " + str(len(x)) + "\n\n")

		for i in range(len(x)):
			line = x[i].strip()

			if (len(line) < 1):
				continue
			if (labelOfInterest == "EVERYTHING"):
				pickUpLabel = True
			elif (line == labelOfInterest):
				pickUpLabel = True

			if (pickUpLabel):
				#ignoring commented lines
				if (line[0] != "#" and line[0] != "/" and line[0] != "-"):
					openBracket = re.findall("{", line)
					closeBracket = re.findall("}", line)

					if (len(openBracket) > 0):
						self.currentLevel += 1
						if (line not in self.labels):
							self.labels[line] = []
							self.currentLabel = Node(line, self.currentLabel)
					elif (len(closeBracket) > 0):
						self.currentLevel -= 1
						self.currentLabel = self.currentLabel.parent
						if (self.currentLabel == None):
							self.previousLabel = None
						else:
							self.previousLabel = self
						if (self.currentLabel.value != labelOfInterest)
							pickUpLabel = False

					#Here we catch the variables and/or values
					if (self.currentLevel == self.previousLevel):
						matchVariable = re.findall(".* =", line)
						
						if (len(matchVariable) > 0):
							if (processToValues):
								matchValue = re.findall("=.*", line)
								self.addValue(matchVariable[0][:-2], matchValue[0][2:])
							else:
								self.addVariable(matchVariable[0][:-2])
					else:
						self.previousLevel = self.currentLevel
		
def readFiles():
	data = []
	p = pathlib.Path(myTUGpathToData)
	directories = [x for x in p.iterdir() if x.is_dir()]
	for i in directories:
		paths = list(i.glob('**/*.txt'))
		for path in paths:
			f = path.open()
			lines = f.read().split("\n")
			f.close()
			data += lines
	return data

def writeToFile(var, val):
	if (processToValues):
		#have to chunk the data because it will be too large
		print("being special\n\n")
		writeToFileSpecial(var, val)
	else:
		f = open(outputFileName, "w")
		for i in sorted(var):
			f.write(i + "\n{ ")
			for j in range(len(var[i])):
				x = var[i][j]

				if (j == len(var[i])-1):
					f.write(x)
				else:
					f.write(x + ", ")
			
			f.write(" }\n\n")
		f.close()

def writeToFileSpecial():
	chunkSize = 100
	count = 0
	stringData = ""

	while len(var) > 0:
		if (count == chunkSize):
			#write memory to file
			#f.write(stringData)
			count = 0
			stringData = ""
		else:
			#create value to write to file
			pass

	"""write(x + " : ")
				if (x in val):
					for k in range(len(val[x])):
						if (k == len(val[x])-1):
							write(val[x][k])
						else:
							write(val[x][k] + ",  ")"""

if __name__ == '__main__':
	x = readFiles()
	schematicX = TUGschematic(x)
	writeToFile(schematicX.variables, schematicX.values)
