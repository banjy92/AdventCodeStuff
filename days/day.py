class Day:
	def __init__(self, inputList):
		self.inputList = inputList

	def getAnswer(self):
		return self.inputList
	
	def debug(self):
		propDict = self.__dict__
		for x in propDict:
			print("Field: ", x)
			print()
			print(propDict[x])
			print("-"*80)