from .day import Day
import math

class Day12(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.direcCycle = "ESWN"

	def processInput(self, inputList):
		return [(x[0], int(x[1:])) for x in inputList]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		direc = "E"
		curLoc = (0, 0)
		for x in self.inputList:
			curLoc, direc = self.move(x, curLoc, direc)
		return abs(curLoc[0]) + abs(curLoc[1])

	def answerTwo(self):
		wp = (10, 1)
		curLoc = (0, 0)
		for x in self.inputList:
			if x[0] == "F":
				curLoc = self.moveShip(curLoc, wp, x)
			else:
				wp = self.moveWP(wp, x)
		return abs(curLoc[0]) + abs(curLoc[1])

	def move(self, inst, curLoc, direc):
		if inst[0] == "F":
			if direc == "E":
				return self.addCoord(curLoc, (inst[1], 0)), direc
			if direc == "W":
				return self.addCoord(curLoc, (-inst[1], 0)), direc
			if direc == "N":
				return self.addCoord(curLoc, (0, inst[1])), direc
			if direc == "S":
				return self.addCoord(curLoc, (0, -inst[1])), direc

		if inst[0] == "R":
			curInd = self.direcCycle.find(direc)
			curInd += int(inst[1]/90)
			return curLoc, self.direcCycle[curInd%len(self.direcCycle)]
		
		if inst[0] == "L":
			curInd = self.direcCycle.find(direc)
			curInd -= int(inst[1]/90)
			return curLoc, self.direcCycle[curInd%len(self.direcCycle)]

		if inst[0] == "L":
			if direc == "E":
				return curLoc, "N"
			if direc == "S":
				return curLoc, "E"
			if direc == "W":
				return curLoc, "S"
			if direc == "N":
				return curLoc, "W"	
				
		if inst[0] == "E":
			return self.addCoord(curLoc, (inst[1], 0)), direc
		if inst[0] == "W":
			return self.addCoord(curLoc, (-inst[1], 0)), direc
		if inst[0] == "N":
			return self.addCoord(curLoc, (0, inst[1])), direc
		if inst[0] == "S":
			return self.addCoord(curLoc, (0, -inst[1])), direc

	def moveShip(self, curLoc, wp, inst):
		scaledwp = tuple(x*inst[1] for x in wp)
		return self.addCoord(curLoc, scaledwp)

	def moveWP(self, wp, inst):
		if inst[0] == "E":
			return self.addCoord(wp, (inst[1], 0))
		if inst[0] == "W":
			return self.addCoord(wp, (-inst[1], 0))
		if inst[0] == "N":
			return self.addCoord(wp, (0, inst[1]))
		if inst[0] == "S":
			return self.addCoord(wp, (0, -inst[1]))

		if inst[0] == "R" or inst[0] == "L":
			return self.rotateCoord(wp, inst[1], inst[0])
		
	def addCoord(self, a, b):
		return tuple(aa + bb for aa, bb in zip(a, b))

	def rotateCoord(self, a, angle, direc):
		angle = angle * math.pi / 180
		if direc == "R":
			angle = -angle
		newX = int(round(a[0] * math.cos(angle) - a[1] * math.sin(angle), 0))
		newY = int(round(a[0] * math.sin(angle) + a[1] * math.cos(angle), 0))
		return (newX, newY)