import numpy as np

# Returns true if array is safe or false if not
def testIfReportIsSafe(numbers):

    # get list of differences between numbers
    numberList1 = numbers[1:]
    numberList2 = numbers[:len(numbers)-1]
    differenceList = np.subtract(numberList1,numberList2)

    # check for too large a change or a zero
    if abs(np.max(differenceList)) > 3 or abs(np.min(differenceList)) > 3 or 0 in differenceList:
        return False

    # check for change in direction
    if np.min(differenceList) < 0:
        if np.max(differenceList > 0):
            return False

    return True
########################################################################################################################


file = open(r"/Day 2 Puzzle Input.txt", "r")

numberOfSafeReports = 0
for line in file:
    # split into numbers and format a little
    formattedLine = line.replace("\n","")
    numbers = [int(ele) for ele in formattedLine.split(" ")]

    reportIsSafe = False
    for index, number in enumerate(numbers):
        tempArray = np.delete(numbers, index)
        reportIsSafe = testIfReportIsSafe(tempArray)
        if reportIsSafe:
            break

    # If no issues add one to count and continue through loop
    if reportIsSafe:
        numberOfSafeReports += 1

print(numberOfSafeReports)
file.close()
