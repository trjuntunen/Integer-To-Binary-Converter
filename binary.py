def main():
	number = askUserForNumber()
	numberIs1or2(number)
	binaryPositions = []
	getBinary1s(number, number, binaryPositions)
	squaresUpToNumber = getArrayOfSquaresUpTo(number)
	reversedBinaryList = list(reversed(buildBinary(binaryPositions, squaresUpToNumber)))
	print()
	reversedBinaryList = formatBinaryIntoList(reversedBinaryList)
	binaryList = reverseList(reversedBinaryList)
	printResults(binaryList)


def printResults(binaryList):
	for char in binaryList:
		print(char,end="")
	print()
	print()

def formatBinaryIntoList(reversedBinaryList):
	newList = []
	for num in range(len(reversedBinaryList)):
		if num % 8 == 0:
			newList.append(" ");
		newList.append(reversedBinaryList[num])
	return newList

def numberIs1or2(number):
	if number == 1:
		print("01")
		exit(0)
	elif number == 2:
		print("010")
		exit(0)

def buildBinary(binaryPositions, squaresUpToNumber):
	result = []
	for num in range(len(squaresUpToNumber)):
		if squaresUpToNumber[num] in binaryPositions:
			result.append(1)
		else:
			result.append(0)
	result.append(0)
	return list(reversed(result))

def getBinary1s(number, amountLeft, binaryPositions):
	if amountLeft <= 0:
		return
	highestSquare = getHighestSquareUpTo(amountLeft)
	binaryPositions.append(highestSquare)
	amountLeft = amountLeft - highestSquare
	getBinary1s(number, amountLeft, binaryPositions)

def getHighestSquareUpTo(limit):
	count = 1
	for i in range(1, limit):
		if (count * 2) > limit:
			break
		count = count * 2
	return count

def getArrayOfSquaresUpTo(limit):
	squares = []
	count = 1
	for i in range(1, limit):
		if count > limit:
			break
		squares.append(count)
		count = count * 2
	return squares

def reverseList(binaryPositions):
	newList = []
	for num in reversed(binaryPositions):
		newList.append(num)
	return newList

def askUserForNumber():
	return int(input("Enter a number: "))

main() 