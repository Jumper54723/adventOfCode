file = open(r"C:\Users\danie\PycharmProjects\adventOfCode\Day 3\Day 3 Puzzle Input.txt", "r")

characterString = file.read()
maxIndex = len(characterString)
mulSubstring = "mul("

lastIndexFound = -1
currentSum = 0
while True:
    # get next instance of substring
    currentIndex = characterString.find(mulSubstring, lastIndexFound+1)
    # if at end of file break out of loop
    if currentIndex == -1:
        break
    lastIndexFound = currentIndex

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
