from .day import Day

class Day5(Day):
	def __init__(self, inputList):
		super().__init__(inputList)
		self.pidList = self.setPidList()

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		pidList = self.getPidList()
		return max(pidList)

	def answerTwo(self):
		return set(range(min(self.getPidList()), max(self.getPidList()))).difference(self.getPidList()).pop()

	def getPidList(self):
		if self.pidList == None:
			self.setPidList()
		return self.pidList
	
	def setPidList(self):
		self.pidList = [self.binFind(127, 0, x[:7], "B", "F") * 8 + self.binFind(7, 0, x[-3:], "R", "L") for x in self.inputList]

	def binFind(self, upper, lower, searchString, uSign, lSign):
		for x in searchString:
			if x == lSign:
				upper = (upper + lower)//2
			else:
				lower = (upper + lower)//2 + 1
		return upper

	def debug(self):
		for i in zip(self.inputList, self.pidList):
			print(i[0], i[1])