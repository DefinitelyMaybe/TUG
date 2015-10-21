#Assume reading one old schematic and re-creating a new one from it.

#Use forward slashes in the paths. No back slashes.
SchematicDataPath = "C:/Program Files (x86)/Steam/steamapps/common/TUG/Game/Core/Data"
OutputFile = "C:/Program Files (x86)/Steam/steamapps/common/TUG/Mods/SchematicData.txt"

#Use all old labels, attributes, values.
IncludeOld = True

#How to specify new things?
NewThings = {}

class TreeNodeTUG(object):
    def __init__(self, name, parent=None):
        self.name = name
		self.parent = parent
		self.children = []
        self.attributes = {} #value key pairs printed initially if present
	
	def __repr__(self):
		return self.name

	def addChild(self, x):
		if x not in self.children:
			self.children += [x]

class SchematicParserTUG(object):
	def __init__(self, oldData):
		self.currentNode = None
		self.process(oldData)

	def addAttribute(self, key, value):
		if (self.currentNode != None):
			self.currentNode.attributes[key] = [value]

	def processor(self, x):
		for i in range(len(x)):
			line = x[i].strip()

			if (len(line) < 1):
				continue
			#ignoring commented lines
			if (line[0] != "#" and line[0] != "-" and line[0] != "/"):
				openBracket = re.findall("{", line)
				closeBracket = re.findall("}", line)

				if (len(openBracket) > 0):
					self.currentLabel = TreeNodeTUG(self.previousLine, self.currentLabel)
					if (self.currentLabel.value not in self.labels):
						self.labels[self.currentLabel.value] = []

				elif (len(closeBracket) > 0):
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
		
"""
f = open(TUG_DataPath, "r")
data = f.read().split("\n")
f.close()
return data
"""

"""
f = open(OutputFileLocation, "w")
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
f.close()"""
	
if __name__ == "__main__":
    pass
