from .day import Day

class Day15(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):		
		return [int(x) for x in inputList]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		memory = {}
		for i, v in enumerate(self.inputList[:-1]):
			memory[v] = i
		last = self.inputList[- 1]
		for x in range(len(self.inputList) - 1, 2019):
			if last in memory:
				d = x - memory[last]
				memory[last] = x
				last = d
			else:
				memory[last] = x
				last = 0

		return last

	def answerTwo(self):
		memory = {}
		for i, v in enumerate(self.inputList[:-1]):
			memory[v] = i
		last = self.inputList[- 1]
		for x in range(len(self.inputList) - 1, 29999999):
			if last in memory:
				d = x - memory[last]
				memory[last] = x
				last = d
			else:
				memory[last] = x
				last = 0
		return last
