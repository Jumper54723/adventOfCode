file = open(r"/Day 1 Puzzle Input.txt", "r")


list1 = list()
list2 = list()
for line in file:
    formattedLine = line.replace("\n","")
    formattedLines = formattedLine.split("   ")
    list1.append(formattedLines[0].strip())
    list2.append(formattedLines[1].strip())

list1.sort()
list2.sort()

totalSum = 0
currentIndex = 0
for num in list1:
    num1 = list1[currentIndex]
    num2 = list2[currentIndex]
    currentDifference = int(num1) - int(num2)
    totalSum += abs(currentDifference)
    currentIndex += 1

print(totalSum)
file.close()
