"""
@Description: 
This programme takes a OBJ file as input. 
It reads through each line, creating an OBJ class when it finds "o" or "g" at the start of a line. 
All lines read after that are treated as data belonging to that OBJ class until another object line is found. 
The OBJ classes are then ordered and written to file.

@help: 
You'll need to install python 3 if you don't already have it. 
1 - open your folder with "processOBJfile.py" < add example.obj file into the same folder.
2 - copy the address of this folder.
3 - press start < type "cmd" < press enter
4 - type "cd" < hit space < right click < paste < hit enter
5 - type "python processOBJfile.py < example.obj > anyNameYouLike.obj"
"""

import sys

class OBJobject():
	def __init__(self, name):
		self.name = name
		self.compare = self.getCompareValue(self.name)
		self.v = []
		self.vt = []
		self.vn = []
		self.f = []

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
		if x == "pivot":
			return 1
		elif x == "hand_atch":
			return 2
		elif x[-10:] == "_atch_rotx":
			return 3
		elif x[-10:] == "_atch_roty":
			return 4
		elif x[-5:] == "_coll":
			return 6
		else:
			return 5

	def len(self):
		return [len(self.v), len(self.vt), len(self.vn)]

	def reformatFaces(self, x):
		# x = [v, vt, vn]
		# x is the an array containing the modify by values.
		#Processing the array of arrays.
		c = 0
		for i in self.f:
			if not(isinstance(i, list)):
				#This is here because "s ..." is still in self.f
				c += 1
				continue
			y = "f "
			for j in i:
				for k in range(3):
					if (j[k] == None):
						y += "/"
					else:
						y += str(j[k] + x[k]) + "/"
				y = y[:-1]
				y += " "
			self.f[c] = y[:-1]
			c += 1

def processFile():
	# [v, vt, vn]
	#current count and totals
	c = [0, 0, 0]
	t = [0, 0, 0]

	objA = [] #an array containing .obj objects.

	for l in sys.stdin:
		x = l.split()
		if (len(x) < 1):
			continue
		if (x[0] == "o" or x[0] == "g"):
			objA += [OBJobject(x[1])]
			# New object to setup the totals.
			for i in range(3):
				t[i] = c[i]
		elif (x[0] == "v"):
			objA[-1].v += ["{} {} {}".format(x[1], x[2], x[3])]
			c[0] += 1
		elif (x[0] == "vt"):
			objA[-1].vt += ["{} {}".format(x[1], x[2])]
			c[1] += 1
		elif (x[0] == "vn"):
			objA[-1].vn += ["{} {} {}".format(x[1], x[2], x[3])]
			c[2] += 1
		elif (x[0] == "s"):
			objA[-1].f += [l]
		elif (x[0] == "f"):
			temp = []
			if "/" in x[1]:
				for i in x[1:]:
					y = i.split("/")
					for j in range(3):
						if (y[j] == ""):
							y[j] = None
						else:
							y[j] = int(y[j]) - t[j]
					temp += [y]
			else:
				print("please include the uv's and normals.")
			
			objA[-1].f += [temp]

	return objA

def writeToFile(x):
	y = [0, 0, 0]
	sys.stdout.write("# Blender OBJ File. Re-constructed for TUG.\n\n")
	for i in sorted(x):
		i.reformatFaces(y)
		sys.stdout.write(str(i))
		temp = i.len()
		for j in range(3):
			y[j] += temp[j]

writeToFile(processFile())