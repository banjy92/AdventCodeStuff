import fileread
import days
from dayFactory import DayFactory

curDay = int(input("Enter day: "))
filename = input("Enter input file: ")
if filename == "":
	filename = "input" + str(curDay) + ".txt"
rawList = fileread.readFile("inputs/" + filename)

day = DayFactory.getDay(curDay, rawList)

if isinstance(day, days.Day):
	print("Answer 1: ")
	print(day.getAnswer(1))
	print("Answer 2:")
	print(day.getAnswer(2))
else:
	print("Answer is not an instance...")
	print(day)

# br = input()
# day.debug()