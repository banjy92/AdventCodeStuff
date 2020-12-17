from .day import Day

class Day16(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))
		self.valid = []

	def processInput(self, inputList):
		ti = inputList.index("your ticket:")
		self.yt = [int(x) for x in inputList[ti + 1].split(",")]
		nti = inputList.index("nearby tickets:")
		self.nt = [[int(y) for y in x.split(",")] for x in inputList[nti + 1:]]
		bi = inputList.index("")
		self.c = {x.split(":")[0] : [tuple(int(y) for y in x.split()[-3].split("-")), tuple(int(y) for y in x.split()[-1].split("-"))] for x in inputList[:bi]}
		return inputList

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		er = 0
		for i, x in enumerate(self.nt):
			valt = True
			for y in x:
				invalid = 0
				for z in self.c.values():
					if z[0][0] > y or (z[0][1] < y and z[1][0] > y) or z[1][1] < y:
						invalid += 1
				if invalid == len(self.c.values()):
					er += y
					valt = False
			if valt:
				self.valid.append(i)
		return er

	def answerTwo(self):
		valdic = {x : list(self.c.keys()) for x in range(0, len(self.yt))}
		for x in self.valid:
			for i, y in enumerate(self.nt[x]):
				for k in self.c:
					if self.c[k][0][0] > y or (self.c[k][0][1] < y and self.c[k][1][0] > y) or self.c[k][1][1] < y:
						valdic[i].remove(k)
		finalDict = {}
		while True:
			curVal = None
			for x in valdic:
				if len(valdic[x]) == 1 and x not in finalDict:
					curVal = x
					break

			if curVal is not None:
				finalDict[curVal] = valdic[curVal][0]
			else:
				minVal = 100
				for i, z in enumerate([len(valdic[x]) for x in valdic]):
					if z < minVal and z != 1:
						minVal = z
						curVal = i
				for y in finalDict:
					if finalDict[y] in valdic[curVal]:
						valdic[curVal].remove(finalDict[y])
			
			if len(finalDict) == 20:
				break
		answer = 1
		for x in finalDict:
			if finalDict[x][:9] == "departure":
				answer *= self.yt[x]
				print(x, finalDict[x], "******")
			else:
				print(x, finalDict[x])
		return answer
