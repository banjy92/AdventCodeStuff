from .day import Day
import re
import itertools

class Day4(Day):
	def __init__(self, inputList):
		super().__init__(self.processInput(inputList))

	def processInput(self, inputList):
		delim = ""
		print([[z.split() for z in list(y)] for x, y in itertools.groupby(inputList, lambda z: z == delim) if not x])
		return [{za[0] : za[1] for za in (z.split(":") for z in " ".join(y).split())} for x, y in itertools.groupby(inputList, lambda z: z == delim) if not x]

	def getAnswer(self , questionNum):
		return self.answerOne() if questionNum == 1 else self.answerTwo()

	def answerOne(self):
		return sum([1 for x in self.inputList if self.allKeysExist(x)])

	def answerTwo(self):
		return sum([1 for x in self.inputList if self.isValidInput(x)])

	def allKeysExist(self, pairList):
		return all(k in pairList for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))

	def isValidInput(self, pairList):
		return self.allKeysExist(pairList) \
		and re.search('^(19[2-9]\d|200[0-2])$', pairList['byr']) \
		and re.search('^(201\d|2020)$', pairList['iyr']) \
		and re.search('^(202\d|2030)$', pairList['eyr']) \
		and re.search('^(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)$', pairList['hgt']) \
		and re.search('^#[0-9a-f]{6}$', pairList['hcl']) \
		and re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', pairList['ecl']) \
		and re.search('^[0-9]{9}$', pairList['pid'])