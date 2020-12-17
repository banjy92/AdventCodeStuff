from .day import Day

class Day14(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):		
		return [[y if y[:3] != "mem" else y[4:-1] for y in x.split() if y != '='] for x in inputList]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		memory = {}
		mask = ""
		for x in self.inputList:
			if x[0] == "mask":
				mask = x[1]
			else:
				maskedval = self.maskVals(mask, x[1])
				memory[int(x[0])] = maskedval
		return sum(memory.values())

	def answerTwo(self):
		memory = {}
		mask = ""
		for x in self.inputList:
			if x[0] == "mask":
				mask = x[1]
			else:
				maskedAddresses = self.maskAdd(mask, x[0])
				for y in maskedAddresses:
					memory[y] = int(x[1])
		return sum(memory.values())

	def maskVals(self, mask, val):
		newVal = format(int(val), "0" + str(len(mask)) + "b")
		for i, v in enumerate(mask):
			if v != "X":
				newVal = newVal[:i] + v + newVal[i + 1:]
		return int(newVal, 2)

	def maskAdd(self, mask, val):
		newVal = format(int(val), "0" + str(len(mask)) + "b")
		for i, v in enumerate(mask):
			if v != "0":
				newVal = newVal[:i] + v + newVal[i + 1:]
		addList = []
		addList = self.floatPerm(newVal, newVal.find("X"), addList)
		return addList

	def floatPerm(self, val, i, addList):
		if "X" not in val or i == -1:
			addList.append(int(val, 2))
			return addList

		zval = val[:i] + "0" + val[i + 1:]
		ival = val[:i] + "1" + val[i + 1:]
		return self.floatPerm(zval, zval.find("X") , addList) + self.floatPerm(ival, ival.find("X") , addList)
		
