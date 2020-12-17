from .day import Day

class Day1(Day):
	def __init__(self, inputList):
		pList = self.processInput(inputList)
		super().__init__(pList)

	def processInput(self, inputList):
		return sorted([int(i) for i in inputList])

	def getAnswer(self, questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		i, j = self.pointerRun(self.inputList, 2020)
		return i*j

	def answerTwo(self):
		for i in range(0, len(self.inputList)):
			sec, thi = self.pointerRun(self.inputList[i:], 2020 - self.inputList[i])
			if sec != None and thi != None:
				print(self.inputList[i], sec, thi)
				return self.inputList[i]*sec*thi
		return None

	def pointerRun(self, curList, targetSum):
		i = 0
		j = len(curList) - 1
		while i < j:
			curSum = curList[i] + curList[j]
			if curSum == targetSum:
				return curList[i], curList[j]
			elif curSum > targetSum:
				j -= 1
			else:
				i += 1
		return None, None