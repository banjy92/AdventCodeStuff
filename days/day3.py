from .day import Day

class Day3(Day):
	def __init__(self, inputList):
		super().__init__(inputList)

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		return self.slope(3, 1, len(self.inputList[0]))

	def answerTwo(self):
		repLen = len(self.inputList[0])
		a = self.slope(1, 1, repLen)
		b = self.slope(3, 1, repLen)
		c = self.slope(5, 1, repLen)
		d = self.slope(7, 1, repLen)
		e = self.slope(1, 2, repLen)
		print(a, b, c, d, e)
		return a*b*c*d*e

	def slope(self, r, d, repLen):
		return sum(1 for i, x in enumerate(self.inputList[0::d]) if x[i*r%repLen] == "#")