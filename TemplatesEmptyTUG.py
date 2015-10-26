import re
#Assume reading one old schematic and re-creating a new one from it.

#Use forward slashes in the paths. No back slashes.
TUGSchematicDataFile = "C:/Users/Rawr/Documents/GitHub/TUG/TestData.txt"
OutputFile = "C:/Users/Rawr/Documents/GitHub/TUG/TestOutput.txt"


#NOT USED YET----------------vvvvvvvvvvvvvv-----------------
#Use old labels, attributes, values. 
#If false and script cannot find label, attri or value then it will be discarded.
IncludeOld = True
#After processing, labels with similar attributes will be have there values merged and then cut.
MergeData = True
#How to specify new things?
NewThings = {}
#NOT USED YET----------------^^^^^^^^^^^^^------------------

class Node(object):
	def __init__(self, name, level, parent):
		self.name = name
		self.l = level
		self.parent = parent
		self.children = []
		self.attributes = {} #value key pairs printed initially if present

	def __str__(self):
		x = ""
		x += "{0}{1}\n{0}".format("\t"*self.l, self.name)
		x += "{\n"
		for i in sorted(self.attributes):
			x += '{0}{1} = {2}\n'.format("\t"*(self.l+1), i, self.attributes[i])
		for i in range(len(self.children)):
			x += str(self.children[i])
		x += "\t" * self.l + "}\n"
		return x

	def addChild(self, x):
		if x not in self.children:
			self.children += [x]

class SchematicProcessor(object):
	def __init__(self, data):
		self.cNode = Node("RootContainer", 0, None)
		self.process(data)

	def addAttribute(self, key, value):
		if (self.cNode != None):
			if (key in self.cNode.attributes):
				self.cNode.attributes[key] += [value]
			else:
				self.cNode.attributes[key] = value

	def process(self, x):
		print("Processing {} lines.\n".format(len(x)))
		c = 0
		for i in range(len(x)):
			line = x[i].strip()

			if (len(line) < 1):
				continue
			#ignoring commented lines
			if (line[0] != "#" and line[0] != "-" and line[0] != "/"):
				openBracket = re.findall("{", line)
				closeBracket = re.findall("}", line)

				if (len(openBracket) > 0):
					c += 1
					newNode = Node(x[i-1].strip(), c, self.cNode)
					self.cNode.addChild(newNode)
					self.cNode = newNode
				elif (len(closeBracket) > 0):
					c -= 1
					self.cNode = self.cNode.parent

				#Here we catch the variables and/or values
				matchAttri = re.findall(".* =", line)
				if (len(matchAttri) > 0):
					matchValue = re.findall("=.*", line)
					self.addAttribute(matchAttri[0][:-2], matchValue[0][2:])
		print("Processing finished.\n")

	def writeProcessedData(self, f):
		if (self.cNode.name != "RootContainer"):
			print("self.cNode was not at ROOT")
			return
		f.write(str(self.cNode))	

if __name__ == "__main__":
	f = open(TUGSchematicDataFile, "r")
	TUGdata = f.read().split("\n")
	f.close()
	
	ProcessorX = SchematicProcessor(TUGdata)

	f = open(OutputFile, "w")
	ProcessorX.writeProcessedData(f)
	f.close()