"""
@Author: Aaron (Rawr)

@Description: 
This programme takes a OBJ file as input. 
It reads through each line, creating an OBJ class when it finds "o - mesh_names" lines. 
All lines read after that are treated as data belonging to that OBJ class. 
The OBJ classes are then ordered and written to file so that any objects named "pivot" 
are at the top and objects who's names end with _coll are at the bottom.

@help: 
You'll need to install python 3.X.X if you don't already have it. 
https://www.python.org/downloads/
Your OBJ file also needs to use the "o" identifier i.e. "o object_name"
check out my tutorial here if you need extra help:
http://forum.nerdkingdom.com/discussion/2293/using-blender-youll-need-this
1 - open your folder with "processOBJfile.py" < add your.obj file into the same folder.
2 - copy the address of this folder.
3 - press start < type "cmd" < press enter
4 - type "cd" < hit space < right click < paste < hit enter
5 - type "python processOBJfile.py < your.obj > anyNameYouLike.obj"
6 - Enjoy.
"""

import sys

class OBJ():
	def __init__(self, name):
		self.name = name
		self.v = []
		self.vt = []
		self.vn = []
		self.f = []
		self.compare = self.getCompareValue(self.name)

	def __repr__(self):
		x = "o {}\n\n".format(self.name)
		for i in self.v:
			x += "v {}\n".format(i)
		x += "# {} vertices\n\n".format(len(self.v))
		for i in self.vt:
			x += "vt {}\n".format(i)
		x += "# {} vertex textures\n\n".format(len(self.vt))
		for i in self.vn:
			x += "vn {}\n".format(i)
		x += "# {} vertex normals\n\n".format(len(self.vn))
		for i in self.f:
			x += "{}\n".format(i)
		x += "# {} polygons\n\n".format(len(self.f)-1)
		return x

	def __eq__(self, other):
		return self.name == other.name

	def __ne__(self, other):
		return self.name != other.name

	def __lt__(self, other):
		return self.compare < other.compare

	def __le__(self, other):
		return self.compare <= other.compare

	def __gt__(self, other):
		return self.compare > other.compare

	def __ge__(self, other):
		return self.compare >= other.compare

	def getCompareValue(self, x):
		#pivot is less than _coll
		if x[:5] == "pivot":
			return 1
		elif x[-5:] == "_coll":
			return 3
		else:
			return 2

	def len(self):
		return [len(self.v), len(self.vt), len(self.vn)]
	
	def addV(self, x):
		self.v += [x]

	def addVN(self, x):
		self.vn += [x]

	def addVT(self, x):
		self.vt += [x]

	def addF(self, x, y):
		if y in self.f:
			#temp = self.f.index(y)
			self.f += [x]
		else:
			self.f += [y]
			self.f += [x]

	def formatF(self, x):
		#1 - s 1
		#2 - [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
		#3 - [[2, 2, 2], [5, 5, 5], [6, 6, 6], [3, 3, 3]]
		#4 - [[5, 7, 5], [7, 8, 7], [8, 9, 8], [6, 10, 6]]
		# i = ^^^
		for i in range(len(self.f)):
			try:
				#[1 - [18, 21, 18], 2 - [17, 20, 17], 3 - [10, 12, 10], 4 - [12, 14, 12]]
				# j = ^^^
				temp = "f "
				for j in range(len(self.f[i])):
					#[12, 14, 12]
					# k = ^^^
					temp2 = ""
					for k in range(len(self.f[i][j])):
						self.f[i][j][k] = self.f[i][j][k] + x[k]
						temp2 += str(self.f[i][j][k]) + "/"
					self.f[i][j] = temp2[:-1]
				for j in self.f[i]:
					temp += j + " "
				self.f[i] = temp[:-1]
			except:
				pass


def processFileByLine():
	vC, vtC, vnC = 0, 0, 0
	vT, vtT, vnT = 0, 0, 0
	objCount, faceS = 0, ""
	objA = [] #the array containing OBJ objects

	for l in sys.stdin:
		x = l[0]
		try:
			a = l[1]
		except:
			a = " "
		if x == "o":
			objA += [OBJ(l.split()[1])]
			objCount += 1
			vT, vtT, vnT = vC, vtC, vnC
		elif (x == "v") and (a == " "):
			temp = "{} {} {}".format(l.split()[1][:-2], l.split()[2][:-2], l.split()[3][:-2])
			objA[objCount-1].addV(temp)
			vC += 1
		elif (x == "v") and (a == "t"):
			temp = "{} {}".format(l.split()[1][:-2], l.split()[2][:-2])
			objA[objCount-1].addVT(temp)
			vtC += 1
		elif (x == "v") and (a == "n"):
			temp = "{} {} {}".format(l.split()[1][:-2], l.split()[2][:-2], l.split()[3][:-2])
			objA[objCount-1].addVN(temp)
			vnC += 1
		elif x == "s":
			faceS = l[:-1]
		elif x == "f":
			temp = processFace(l[2:], [vT, vtT, vnT])
			objA[objCount-1].addF(temp, faceS)

	return objA

def processFace(x, a):
	data = x.split()
	out = []
	for i in data:
		y = i.split("/")
		for j in range(len(y)):
			y[j] = int(y[j]) - a[j]
		out += [y]
	return out

def writeToFile(x):
	y = [0, 0, 0]
	sys.stdout.write("# Blender OBJ File. Restructured for TUG.\n\n")
	for i in sorted(x):
		i.formatF(y)
		sys.stdout.write(str(i))
		temp = i.len()
		for j in range(3):
			y[j] += temp[j]

writeToFile(processFileByLine())