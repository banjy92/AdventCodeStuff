import importlib

class DayFactory:
	def getDay(day, inputList):
		module = importlib.import_module("days")
		class_ = getattr(module, "Day" + str(day))
		return class_(inputList)