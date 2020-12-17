from .day import Day

class Day7(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.oneHash = {}
		self.twoHash = {}

	def processInput(self, inputList):
		outputList = {}
		for x in inputList:
			newList = x.replace("contain", ",").split(",")
			key = " ".join(newList[0].split()[:2])
			outputList[key] = {}
			for y in newList[1:]:
				curVals = y.split()
				if curVals[0] == 'no':
					pass
				else:
					num = int(curVals[0])
					col = " ".join(curVals[1: 3])
					outputList[key][col] = num
		return outputList

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		matchBag = "shiny gold"
		return sum([self.findBag(x, matchBag) for x in self.inputList if x != matchBag])

	def answerTwo(self):
		matchBag = "shiny gold"
		return self.sumBag(matchBag) - 1

	def findBag(self, curBag, matchBag):
		# return hash val if exists
		if curBag in self.oneHash:
			return self.oneHash[curBag]

		# else hash according to condition and return value
		if matchBag in self.inputList[curBag]:
			self.oneHash[curBag] = True
		elif not bool(self.inputList[curBag]):
			self.oneHash[curBag] = False
		else:
			self.oneHash[curBag] = any(self.findBag(x, matchBag) for x in self.inputList[curBag])
		return self.oneHash[curBag]

	def sumBag(self, curBag):
		if curBag in self.twoHash:
			return self.twoHash[curBag]

		if not bool(self.inputList[curBag]):
			self.twoHash[curBag] = 1
		else:
			self.twoHash[curBag] = sum([self.inputList[curBag][x]*self.sumBag(x) for x in self.inputList[curBag]]) + 1
		return self.twoHash[curBag]