file = open(r"/Day 3/Day 3 Example Text.txt", "r")

characterString = file.read()
maxIndex = len(characterString)
mulSubstring = "mul("
doSubstring = "do()"
dontSubstring = "don't()"

lastIndexFound = -1
currentSum = 0
while True:
    # get next instance of substring
    currentIndex = characterString.find(mulSubstring, lastIndexFound+1)
    # if at end of file break out of loop
    if currentIndex == -1:
        break
    lastIndexFound = currentIndex

    # Determine if do or don't
    nearistDoIndex = -1
    nearistDontIndex = -1
    doIndex = characterString.find(doSubstring, nearistDoIndex+1)
    dontIndex = characterString.find(dontSubstring, nearistDontIndex+1)
    while doIndex < currentIndex or dontIndex < currentIndex and (nearistDoIndex != -1 and nearistDontIndex != -1):
        doIndex = characterString.find(doSubstring, nearistDoIndex+1)
        dontIndex = characterString.find(dontSubstring, nearistDontIndex+1)
        if doIndex < currentIndex:

            nearistDoIndex = doIndex
        if dontIndex < currentIndex:
            nearistDontIndex = dontIndex
        if doIndex == -1 and dontIndex == -1:
            break

    if nearistDontIndex > nearistDoIndex:
        continue

    if nearistDontIndex != -1 and nearistDoIndex == -1:
        continue

    # Get first number if valid
    firstNumber = ""
    firstNumberLength = 0
    while characterString[currentIndex+4+firstNumberLength].isdigit():
        firstNumber += characterString[currentIndex+4+firstNumberLength]
        firstNumberLength += 1

    # Ensure separating character is a comma and that first number isn't too long
    if characterString[currentIndex+4+firstNumberLength] != "," or firstNumberLength > 3:
        continue

    # Get second number if valid
    secondNumber = ""
    secondNumberLength = 0
    while characterString[currentIndex+4+firstNumberLength+1+secondNumberLength].isdigit():
        secondNumber += characterString[currentIndex+4+firstNumberLength+1+secondNumberLength]
        secondNumberLength += 1

    # Ensure final parentheses is in place and that second number isn't too long
    if characterString[currentIndex+4+firstNumberLength+1+secondNumberLength] != ")" or secondNumberLength > 3:
        continue

    currentSum += int(firstNumber) * int(secondNumber)

# Output sum, close file
print(currentSum)
file.close()
