from .day import Day
from collections import namedtuple

PassPolicy = namedtuple('PassPolicy', 'minP maxP charP password')

class Day2(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):
		outList = []
		for line in inputList:
			e = line.split()
			minMaxPol = [int(i) for i in e[0].split("-")]
			newPol = PassPolicy(minMaxPol[0], minMaxPol[1], e[1][:-1], e[2])
			outList.append(newPol)
		return outList

	def getAnswer(self, questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		return sum(1 for i in self.inputList if i.minP <= i.password.count(i.charP) <= i.maxP)

	def answerTwo(self):
		return sum(1 for i in self.inputList if (i.password[i.minP - 1] == i.charP) ^ (i.password[i.maxP - 1] == i.charP))