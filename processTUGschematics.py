import re, pathlib

#Use forward slashes in the paths. No back slashes.
TUG_DataPath = "C:/Program Files (x86)/Steam/steamapps/common/TUG/Game/Core/Data"
OutputFileLocation = "C:/Program Files (x86)/Steam/steamapps/common/TUG/Mods/SchematicData.txt"

#Reduce the scope of the data collected to just the specified directory
readLocalSchematicsOnly = False

#Useful if you don't care about any associated values.
includeValues = True

#An empty string will be ignored. If specificed only that variable will be written within labels
onlyThisVariable = "category" # ie, "", "submesh" or "equipSound"

#Specify to only pickup data within a label of interest
labelOfInterest = "EVERYTHING" # ie, "EVERYTHING", "arguments" or "GameObjects"

class Node(object):
	"""ADT for the TUGschematic for dealing with labels in a tree-ish fashion"""
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
		self.previousLine = ""

		self.variables = {} #holds the variables and if chosen, associated values
		self.labels = {} #holds labels and associated variables

		self.processLines(x)

	def addVariable(self, x):
		if (self.currentLabel.value in self.labels):
			if x not in self.labels[self.currentLabel.value]:
				self.labels[self.currentLabel.value] += [x]
		else:
			self.labels[self.currentLabel.value] = [x]

	def addValue(self, var, value):
		if (var in self.variables):
			if value not in self.variables[var]:
				self.variables[var] += [value]
		else:
			self.variables[var] = [value]

	def processLines(self, x):
		print("processing...")
		print("Number of lines to process: " + str(len(x)))
		pickUpLabel = False
		labelOfInterestLevel = 0

		for i in range(len(x)):
			line = x[i].strip()

			if (len(line) < 1):
				continue
			if (labelOfInterest == "EVERYTHING"):
				pickUpLabel = True
			elif (line == labelOfInterest):
				labelOfInterestLevel = self.currentLevel
				pickUpLabel = True

			if (pickUpLabel):
				#ignoring commented lines
				if (line[0] != "#" and line[0] != "-" and line[0] != "/"):
					openBracket = re.findall("{", line)
					closeBracket = re.findall("}", line)

					if (len(openBracket) > 0):
						self.currentLevel += 1
						self.currentLabel = Node(self.previousLine, self.currentLabel)
						if (self.currentLabel.value not in self.labels):
							self.labels[self.currentLabel.value] = []

					elif (len(closeBracket) > 0):
						self.currentLevel -= 1
						if (self.currentLabel != None):
							if (self.currentLabel.parent != None):
								self.currentLabel = self.currentLabel.parent
							else:
								self.currentLabel = None
						if (self.currentLevel == labelOfInterestLevel):
							pickUpLabel = False
							

					#Here we catch the variables and/or values
					if (self.currentLevel == self.previousLevel):
						matchVariable = re.findall(".* =", line)
						self.previousLine = line
						
						if (len(matchVariable) > 0):
							if (includeValues):
								matchValue = re.findall("=.*", line)
								self.addValue(matchVariable[0][:-2], matchValue[0][2:])
								self.addVariable(matchVariable[0][:-2])
							else:
								self.addVariable(matchVariable[0][:-2])
					else:
						self.previousLevel = self.currentLevel
		print("processing finished.\n")
		
def readFiles():
	count = 0
	data = []
	p = pathlib.Path(TUG_DataPath)
	if (readLocalSchematicsOnly):
		paths = list(p.glob('*.txt'))
		for path in paths:
			f = path.open()
			lines = f.read().split("\n")
			f.close()
			data += lines
			count += 1
	else:
		paths = list(p.glob('**/*.txt'))
		for path in paths:
			f = path.open()
			lines = f.read().split("\n")
			f.close()
			data += lines
			count += 1
	print("Read through {} schematic files.".format(count))
	return data

def writeToFile(lab, var):
	#have to chunk the data because it will be too large
	f = open(OutputFileLocation, "w")
	print("writing...")
	print("Number of labels: " + str(len(lab)))
	print("Number of variables: " + str(len(lab)))

	for label in sorted(lab):
		if not(len(lab[label]) > 0):
			continue
		if (onlyThisVariable):
			if not(onlyThisVariable in lab[label]):
				continue
		f.write(label + "\n{\n")
		if (len(lab[label])>0):
			for i in range(len(lab[label])):
				x = lab[label][i]
				if (includeValues):
					if (x in var and len(var[x]) <= 1):
						if (onlyThisVariable):
							if (onlyThisVariable != x):
								continue
						f.write(x + " : ")
						if (len(var[x]) == 1):
							f.write(var[x].pop() + "\n")
						else:
							f.write("\n")
					elif (x in var):
						if (onlyThisVariable):
							if (onlyThisVariable != x):
								continue
						f.write(x + " : ")
						while (len(var[x])>0):
							if (len(var[x]) == 1):
								f.write(var[x].pop() + "\n")
							else:
								f.write(var[x].pop() +", ")
					else:
						if (onlyThisVariable):
							if (onlyThisVariable != x):
								continue
						f.write(x)
				else:
					if (onlyThisVariable):
							if (onlyThisVariable != x):
								continue
					if (i == len(lab[label])-1):
						f.write(x)
					else:
						f.write(x + ", ")
		f.write("}\n\n")
	print("writing finished.")
	f.close()

if __name__ == '__main__':
	rawData = readFiles()
	schematic = TUGschematic(rawData)
	writeToFile(schematic.labels, schematic.variables)
