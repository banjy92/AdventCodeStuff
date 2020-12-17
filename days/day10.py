from .day import Day

class Day10(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):
		return sorted([int(x) for x in inputList])

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		curList = sorted(self.inputList)
		testList = set()
		testSet = set()
		curVal = 0
		oneTotal = 0
		threeTotal = 0
		for x in curList:
			if x - curVal == 1:
				testSet.add(x)
				oneTotal += 1
			elif x - curVal == 3:
				testList.add(curVal)
				testList.add(x)
				threeTotal += 1
			curVal = x
		threeTotal += 1
		print(oneTotal)
		print(threeTotal)
		print(sorted(list(testList)))
		print(testSet.difference(testList))
		print(sorted(list(testSet.difference(testList))))
		print(len(testSet.difference(testList)))
		return oneTotal*threeTotal

	def answerTwo(self):
		curList = sorted(self.inputList)
		answer = self.knapsack(max(self.inputList), 0, {0})
		print(self.resultList)
		return answer

	def knapsack(self, goal, ind, curSet):
		wt = self.inputList[ind] - max(curSet)

		if wt > 3:
			return 0

		if goal == 0 or ind == len(self.inputList) - 1:
			if min(curSet) <= 3 and wt <= 3:
				return 1
			else:
				return 0

		if goal < 0:
			return 0

		if goal - (wt) < 0:
			return self.knapsack(goal, ind + 1, curSet)
		
		if wt <= 3:
			nxtInd = ind + 1
			noInclude = self.knapsack(goal, nxtInd, curSet)
			curSet.add(self.inputList[ind])
			include = self.knapsack(goal - (wt), nxtInd, curSet)
			return noInclude + include

		return 0