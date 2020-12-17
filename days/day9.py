from .day import Day
from collections import deque
import itertools

class Day9(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.preamble = deque()
		self.answerOnee = 0

	def processInput(self, inputList):
		return [int(x) for x in inputList]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		for i in range(25, len(self.inputList)):
			if not self.checkValid(i):
				self.answerOnee = self.inputList[i]
				return self.inputList[i]
		return None
	
	def checkValid(self, ind):
		validNum = set()
		for i, v in enumerate(self.inputList[ind - 25:ind]):
			for j in range(i + 1, ind):
				validNum.add(v + self.inputList[j])
		return self.inputList[ind] in validNum

	def answerTwo(self):
		for i, v in enumerate(self.inputList):
			for j in range(i + 2, len(self.inputList)):
				if sum(self.inputList[i: j]) == self.answerOnee:
					print("found")
					print(min(self.inputList[i: j]), max(self.inputList[i: j]))
					print(min(self.inputList[i: j]) + max(self.inputList[i: j]))
					return None
		return None
	