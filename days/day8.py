from .day import Day

class Day8(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.curSet = set()
		self.setTwo = set()
		self.accOne = 0
		self.accTwo = 0

	def processInput(self, inputList):
		return [(x.split()[0], x.split()[1]) for x in inputList]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		x = 0
		self.curSet.add(x)
		while True:
			x = self.inst(self.inputList[x], x)
			if x == len(self.inputList):
				return self.accOne
			if x not in self.curSet:
				self.curSet.add(x)
			else:
				break
		return self.accOne

	def answerTwo(self):
		x = 0
		self.curSet.add(x)
		for x in self.curSet:
			print("start:", x)
			self.accTwo = 0
			setTwo = set()
			print(x, self.inputList[x])
			x = self.instTest(self.inputList[x], x, True)
			setTwo.add(x)
			while True:
				print(x, self.inputList[x])
				x = self.instTest(self.inputList[x], x, False)
				if x == len(self.inputList):
					return self.accTwo
				if x not in setTwo:
					setTwo.add(x)
				else:
					break
		return self.accTwo

	def inst(self, inst, i):
		if inst[0] == 'nop':
			return i + 1
		if inst[0] == 'jmp':			
			val = int(inst[1][1:])
			if inst[1][0] == '-':
				val = -val
			return i + val
		if inst[0] == 'acc':
			val = int(inst[1][1:])
			if inst[1][0] == '-':
				val = -val
			self.accOne += val
			return i + 1

	def instTest(self, inst, i, sw):
		if sw:
			if inst[0] == 'jmp':
				return i + 1
			if inst[0] == 'nop':		
				val = int(inst[1][1:])
				if inst[1][0] == '-':
					val = -val
				return i + val
		if inst[0] == 'nop':
			return i + 1
		if inst[0] == 'jmp':		
			val = int(inst[1][1:])
			if inst[1][0] == '-':
				val = -val
			return i + val
		if inst[0] == 'acc':
			val = int(inst[1][1:])
			if inst[1][0] == '-':
				val = -val
			self.accTwo += val
			return i + 1