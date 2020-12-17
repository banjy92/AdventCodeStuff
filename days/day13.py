from .day import Day
import math

class Day13(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):
		self.e = int(inputList[0])
		return [x if x =='x' else int(x) for x in inputList[1].split(',')]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		minVal = self.e
		minX = self.e
		for x in [x for x in self.inputList if type(x) is int]:
			print(x)
			print(x - self.e%x)
			if minVal > (x - self.e%x):
				minVal = (x - self.e%x)
				minX = x
		print(minVal, minX)
		return minVal*minX

	def answerTwo(self):
		allmod = math.prod(x for x in self.inputList if type(x) is int)
		print(allmod)
		nums = [((v - i) % v, v) for i, v in enumerate(self.inputList) if type(v) is int]
		print(nums)
		sums = 0
		for x in nums:
			z = int(allmod/x[1])
			iz = z%x[1]
			iiz = iz ** (x[1] - 2)
			iiiz = iiz%x[1]
			mult = (iiiz*z)%allmod
			print(mult%x[1])
			print(x[0])
			print(x[0]*mult)
			sums += x[0]*mult
		print(sums%allmod)
		print(allmod, sums)
		print(allmod + (sums%allmod))
		return None
