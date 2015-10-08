import sys, re, pathlib

class TUGschematic(object):
	"""docstring for TUGschematics"""
	def __init__(self, x):
		self.currentLevel = -1
		self.previousLevel = -1
		self.data = {}
		self.labels = []
		self.previousline = ""

		#set the following to your own desire
		self.UseInterestFilter = False
		self.interest = "GameObjects"
		self.interested = False

		self.processLines(x)		

	def addAttri(self, x):
		dkey = "{}".format(self.labels[-1])
		if (dkey in self.data):
			if x not in self.data[dkey]:
				self.data[dkey] += [x]
		else:
			self.data[dkey] = [x]

	def processLines(self, x):
		#Notice that 
		for i in range(len(x)):
			line = x[i].strip()
			if (len(line) < 1):
				continue
			if (self.UseInterestFilter):
				if (line == self.interest):
					self.interested = True
				if (self.interested):
					if (line[0] != "#" and line[0] != "/" and line[0] != "-"):
						matchOpen = re.findall("{", line)
						matchClose = re.findall("}", line)

						if (len(matchOpen) > 0):
							self.currentLevel += 1
							self.labels += [self.previousline]
						elif (len(matchClose) > 0):
							self.currentLevel -= 1
							self.labels.pop()
							if (self.currentLevel == 0):
								self.interested = False

						if (self.currentLevel == self.previousLevel):
							self.previousline = line
							matchAttri = re.findall(".* =", line)
							if (len(matchAttri) > 0):
								self.addAttri(matchAttri[0][:-2])
						else:
							self.previousLevel = self.currentLevel
			else:
				if (line[0] != "#" and line[0] != "/" and line[0] != "-"):
					matchOpen = re.findall("{", line)
					matchClose = re.findall("}", line)

					if (len(matchOpen) > 0):
						self.currentLevel += 1
						self.labels += [self.previousline]
					elif (len(matchClose) > 0):
						self.currentLevel -= 1
						self.labels.pop()
						if (self.currentLevel == 0):
							self.interested = False

					if (self.currentLevel == self.previousLevel):
						self.previousline = line
						matchAttri = re.findall(".* =", line)
						if (len(matchAttri) > 0):
							self.addAttri(matchAttri[0][:-2])
					else:
						self.previousLevel = self.currentLevel
		
def readFiles():
	data = []
	p = pathlib.Path("C:/Program Files (x86)/Steam/steamapps/common/TUG/Game/Core/Data")
	directories = [x for x in p.iterdir() if x.is_dir()]
	for i in directories:
		paths = list(i.glob('**/*.txt'))
		for path in paths:
			f = path.open()
			lines = f.read().split("\n")
			f.close()
			data += lines
	return data

def writeToFile(x, opt=False):
	if (opt):
		#attempt at pretty printing
		s1, s2, s3 = "", "", ""

		for i in range(len(x)):
			if not(s1):
				s1 = x[i]
				if (i == len(x)):
					sys.stdout.write(s1 + "\n")
					s1, s2, s3 = "", "", ""
			elif not(s2):
				s2 = x[i]
				if (i == len(x)):
					sys.stdout.write("{}\t\t{}\n".format(s1, s2))
					s1, s2, s3 = "", "", ""
			elif not(s3):
				s3 = x[i]
				sys.stdout.write("{}\t\t{}\t\t{}\n".format(s1, s2, s3))
				s1, s2, s3 = "", "", ""
	else:
		for i in sorted(x):
			sys.stdout.write(i + ": ")
			for j in range(len(x[i])):
				if (j == len(x[i]) - 1):
					sys.stdout.write(x[i][j] + ".")
				else:
					sys.stdout.write(x[i][j] + ", ")
			sys.stdout.write("\n")
	
x = readFiles()
schematicX = TUGschematic(x)
writeToFile(schematicX.data)


