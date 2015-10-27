import re

#Use forward slashes in the paths. No back slashes.
TUGSchematicDataFile = "C:/.../TestData.txt"
OutputFile = "C:/.../TestOutput.txt"

class Node(object):
	def __init__(self, n, d, p):
		self.name = n
		self.depth = d #depth of the node from root
		self.parent = p
		self.children = []
		self.attributes = {} #value key pairs printed initially if present

	def __eq__(self, other):
		if not(isinstance(other, Node)):
			return False
		else:
			if (other.name == self.name):
				return True
			return False

	def __str__(self):
		x = ""
		x += "{0}{1}\n{0}".format("\t"*self.depth, self.name)
		x += "{\n"
		for i in sorted(self.attributes):
			x += '{0}{1} = {2}\n'.format("\t"*(self.depth+1), i, self.attributes[i])
		for i in range(len(self.children)):
			x += str(self.children[i])
		x += "\t" * self.depth + "}\n"
		return x

	def addChild(self, x):
		if x not in self.children:
			self.children += [x]

class SchematicProcessor(object):
	def __init__(self, data):
		self.rootNode = Node("RootContainer", 0, None)
		self.currentNode = self.rootNode
		self.process(data)

	def addAttribute(self, key, value):
		if (self.currentNode != None):
			self.currentNode.attributes[key] = value

	def process(self, x):
		print("Processing {} lines.".format(len(x)))
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
					newNode = Node(x[i-1].strip(), c, self.currentNode)
					self.currentNode.addChild(newNode)
					self.currentNode = newNode
				elif (len(closeBracket) > 0):
					c -= 1
					self.currentNode = self.currentNode.parent

				#Here we catch the variables and/or values
				matchAttri = re.findall(".* =", line)
				if (len(matchAttri) > 0):
					matchValue = re.findall("=.*", line)
					self.addAttribute(matchAttri[0][:-2], matchValue[0][2:])
		print("Processing finished.\n")

	def findNode(self, node, root=None):
		"""Can specify the root but will default to RootContainer"""
		if (root == None):
			root = self.rootNode
		if not(isinstance(node, Node) and isinstance(root, Node)):
			print("Either the thing you were looking for or where you tried to find it, was not an instance of a node.")
			return None
		else:
			return self.dfs(root, node)

	def dfs(self, node, wantedNode):
		if (node != wantedNode):
			if (len(node.children) > 0):
				temp = None
				for i in range(len(node.children)):
					x = self.dfs(node.children[i], wantedNode)
					if (isinstance(x, Node)):
						temp = x
				return temp
			else:
				return None
		else:
			print("Found match:", node.name)
			return node

	def writeProcessedData(self, f):
		f.write(str(self.rootNode))

if __name__ == "__main__":
	f = open(TUGSchematicDataFile, "r")
	TUGdata = f.read().split("\n")
	f.close()
	
	x = SchematicProcessor(TUGdata)

	x.currentNode = x.rootNode
	newNode = Node("Equipable", 0, None)
	selectedNode = x.findNode(newNode)

	if (selectedNode != None):
		#This is where you've got to figure out which things to keep.
		#newNode.attributes = selectedNode.attributes
		newNode.parent = selectedNode.parent
		newNode.attributes = selectedNode.attributes
		newNode.depth = selectedNode.depth
		for i in newNode.attributes:
			newNode.attributes[i] = 0

		i = selectedNode.parent.children.index(selectedNode)
		selectedNode.parent.children[i] = newNode

	f = open(OutputFile, "w")
	x.writeProcessedData(f)
	f.close()