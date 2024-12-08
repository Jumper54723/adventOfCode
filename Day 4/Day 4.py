from enum import Enum

class Directions(Enum):
    left = 0
    topLeft = 1
    top = 2
    topRight = 3
    right = 4
    botRight = 5
    bot = 6
    botLeft = 7

def getPositionsOfLetter(letter):
    letterPositions = []
    for i, line in enumerate(formattedLines):
        index = -1
        linePositions = []
        while True:
            index = line.find(letter, index + 1)
            if index == -1:
                break
            tupleVariable = (i,index)
            letterPositions.append(tupleVariable)
    return letterPositions

def checkInDirectionForLetter(startPosition, directionToCheck, testLetterPositions):
    line = startPosition[0]
    column = startPosition[1]
    nullPosition2 = (-1, -1)
    positionToTest = nullPosition
    match directionToCheck:
        case Directions.left:
            positionToTest = (line, column - 1)
        case Directions.topLeft:
            positionToTest = (line - 1, column - 1)
        case Directions.top:
            positionToTest = (line - 1, column)
        case Directions.topRight:
            positionToTest = (line - 1, column + 1)
        case Directions.right:
            positionToTest = (line, column + 1)
        case Directions.botRight:
            positionToTest = (line + 1, column + 1)
        case Directions.bot:
            positionToTest = (line + 1, column)
        case Directions.botLeft:
            positionToTest = (line + 1, column - 1)

    if positionToTest in testLetterPositions:
        return positionToTest
    else:
        return nullPosition2


file = open(r"C:\Users\danie\PycharmProjects\adventOfCode\Day 4\Day 4 Input.txt", "r")

# Pull lines from file
formattedLines = []
for line in file:
    formattedLine = line.replace("\n","")
    formattedLines.append(formattedLine)

# Get positions of letters from lines
xPositions = getPositionsOfLetter("X")
mPositions = getPositionsOfLetter("M")
aPositions = getPositionsOfLetter("A")
sPositions = getPositionsOfLetter("S")

# check for possible instances of XMAS
possibleXmasLocations = []
nullPosition = (-1, -1)
for position in xPositions:
    for direction in Directions:
        mPosition = checkInDirectionForLetter(position, direction, mPositions)
        if mPosition != nullPosition:
            tupleVariable = (mPosition, direction)
            possibleXmasLocations.append(tupleVariable)

# Get number of Xmas instances
xmasCount = 0
for possibleXmas in possibleXmasLocations:
    aPosition = checkInDirectionForLetter(possibleXmas[0],possibleXmas[1],aPositions)
    if aPosition != nullPosition:
        sPosition = checkInDirectionForLetter(aPosition, possibleXmas[1], sPositions)
        if sPosition != nullPosition:
            xmasCount += 1


print(xmasCount)
file.close()