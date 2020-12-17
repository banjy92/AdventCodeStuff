from .day import Day

class Day11(Day):
	def __init__(self, inputList):
		super().__init__(inputList)
		self.prevList = []
		self.answerTwoList = self.inputList.copy()

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		if False:
			answer = self.cycle()
		return None

	def answerTwo(self):
		answer = self.cycletwo()
		return answer

	def cycle(self):
		cycle = 0
		while(self.prevList != self.inputList):
			self.prevList = self.inputList.copy()
			for j in range(0, len(self.inputList)):
				for i in range(0, len(self.inputList[j])):
					self.checkadjacent((i, j))
				
			cycle = sum([x.count("#") for x in self.inputList])
		return cycle

	def cycletwo(self):
		cycle = 0
		while(self.prevList != self.answerTwoList):
			self.prevList = self.answerTwoList.copy()
			for j in range(0, len(self.answerTwoList)):
				for i in range(0, len(self.answerTwoList[j])):
					self.newcheckadjacent((i, j))
				
			cycle += 1
			print(sum([x.count("#") for x in self.answerTwoList]))
		return cycle

	def checkadjacent(self, current):
		nlist = [(current[0] - 1,  current[1] - 1), (current[0], current[1] - 1), (current[0] + 1, current[1] - 1), (current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0] - 1, current[1] + 1), (current[0], current[1] + 1), (current[0] + 1, current[1] + 1)]
		ecount = 0
		ocount = 0
		for x in nlist:
			if x[0] >= 0 and x[0] < len(self.prevList[0]) and x[1] >= 0 and x[1] < len(self.prevList):
				if self.prevList[x[1]][x[0]] == "L":
					ecount += 1
				if self.prevList[x[1]][x[0]] == "#":
					ocount += 1

		if self.prevList[current[1]][current[0]] == "L":
			if ocount == 0:
				self.inputList[current[1]] = self.inputList[current[1]][:current[0]] + "#" + self.inputList[current[1]][current[0] + 1:]
		elif self.prevList[current[1]][current[0]] == "#":
			if ocount >= 4:
				self.inputList[current[1]] = self.inputList[current[1]][:current[0]] + "L" + self.inputList[current[1]][current[0] + 1:]

	def newcheckadjacent(self, current):
		nlist = [(current[0] - 1,  current[1] - 1), (current[0], current[1] - 1), (current[0] + 1, current[1] - 1), (current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0] - 1, current[1] + 1), (current[0], current[1] + 1), (current[0] + 1, current[1] + 1)]

		nlist = self.getneighbors(nlist, current)
		ecount = 0
		ocount = 0
		for x in nlist:
			if x[0] >= 0 and x[0] < len(self.prevList[0]) and x[1] >= 0 and x[1] < len(self.prevList):
				if self.prevList[x[1]][x[0]] == "L":
					ecount += 1
				if self.prevList[x[1]][x[0]] == "#":
					ocount += 1

		if self.prevList[current[1]][current[0]] == "L":
			if ocount == 0:
				self.answerTwoList[current[1]] = self.answerTwoList[current[1]][:current[0]] + "#" + self.answerTwoList[current[1]][current[0] + 1:]
		elif self.prevList[current[1]][current[0]] == "#":
			if ocount >= 5:
				self.answerTwoList[current[1]] = self.answerTwoList[current[1]][:current[0]] + "L" + self.answerTwoList[current[1]][current[0] + 1:]

	def getneighbors(self, currentn, current):
		newn = []
		for x in currentn:
			xdiff = x[0] - current[0]
			ydiff = x[1] - current[1]
			curX = x[0]
			curY = x[1]
			while curX >= 0 and curX < len(self.prevList[0]) and curY >= 0 and curY < len(self.prevList) and self.prevList[curY][curX] == ".":
				curX += xdiff
				curY += ydiff
			newn.append((curX, curY))
		return newn
