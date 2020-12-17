from .day import Day
import itertools

class Day6(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.pidList = None

	def processInput(self, inputList):
		delim = ""		
		return [list(y) for x, y in itertools.groupby(inputList, lambda z: z == delim) if not x]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		return sum([len(set().union(*x)) for x in self.inputList])

	def answerTwo(self):
		return sum([len(set(x[0]).intersection(*x)) for x in self.inputList])