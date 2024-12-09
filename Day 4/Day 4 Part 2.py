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

def checkForMasX(line1, line2):
    x1 = line1[0][1]
    x2 = line1[1][1]
    y1 = line1[0][0]
    y2 = line1[1][0]
    x3 = line2[0][1]
    x4 = line2[1][1]
    y3 = line2[0][0]
    y4 = line2[1][0]

    centerPoint1 = (min(x1,x2)+1,min(y1,y2)+1)
    centerPoint2 = (min(x3,x4)+1,min(y3,y4)+1)
    if centerPoint1 != centerPoint2:
        return False

    return True

file = open(r"C:\Users\danie\PycharmProjects\adventOfCode\Day 4\Day 4 Input.txt", "r")

# Pull lines from file
formattedLines = []
for line in file:
    formattedLine = line.replace("\n","")
    formattedLines.append(formattedLine)

# Get positions of letters from lines
# each position in lists contain tuple of ( line number y, column number x)
mPositions = getPositionsOfLetter("M")
aPositions = getPositionsOfLetter("A")
sPositions = getPositionsOfLetter("S")

# get locations of diagonal mas. Horizontal and vertical directions are ignored
# masLocation contains tuple of (startPosition, stopPosition), also each position is ( line number y, column number x)
masLocations = []
nullPosition = (-1, -1)
diagonalDirections = [Directions.topLeft, Directions.topRight, Directions.botRight, Directions.botLeft]
for position in mPositions:
    for direction in diagonalDirections:
        aPosition = checkInDirectionForLetter(position, direction, aPositions)
        if aPosition != nullPosition:
            sPosition = checkInDirectionForLetter(aPosition, direction, sPositions)
            if sPosition != nullPosition:
                if position[0] < sPosition[0]:
                    tupleVariable = (position, sPosition)
                else:
                    tupleVariable = (sPosition, position)
                masLocations.append(tupleVariable)

masLocations.sort()
numberOfXmas = 0
for i, location1 in enumerate(masLocations):
    j = i - len(masLocations)
    for location2 in masLocations[:j]:
        if checkForMasX(location1, location2):
            numberOfXmas += 1

print(numberOfXmas)
file.close()