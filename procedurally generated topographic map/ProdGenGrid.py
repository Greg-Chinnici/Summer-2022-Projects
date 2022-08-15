import math
#prodgne topo map in python

#has to be odd

sideLen = 13
gridSize = sideLen * sideLen;

def makeGrid(sideLen):
    '''
    grid = [
        1,2,3,4,3,2,1,
        2,3,4,5,4,3,2,
        3,4,5,6,5,4,3,
        4,5,6,7,6,5,4,
        3,4,5,6,5,4,3,
        2,3,4,5,4,3,2,
        1,2,3,4,3,2,1
        ]#how do i make the array like this in a one liner using a for loop
    '''
    grid = []
    for row in range(sideLen):
        row = []
        for index in range(sideLen):
            row.append(0)
        grid.append(row)

    return grid

grid = makeGrid(sideLen)

lightLevelDict = [
    " ",
    ".",
    "'",
    ":",
    "!",
    ";",
    "-",
    "~",
    "=",
    "+",
    "*",
    "#",
    "%",
    "@",
]

NorthSlope = 1
SouthSlope = 1
WestSlope = 1
EastSlope = 1

def generateHighPoint():
    index = int(input("what index do you want the highpoint out of " + str(gridSize) + ": "))
    index -= 1
    grid[index//sideLen][index%sideLen] = (len(lightLevelDict)-1)#idk if this works

def getHighPoint(grid):
    topnum = 0
    for row in grid:
        for num in row:
            if int(num) > topnum:
                topnum = int(num)
    
    for rowNum, row in enumerate(grid):
        for numIndex, num in enumerate(row):
            if num == topnum:
                return [rowNum , numIndex]

def setMainRow(grid):
    highCoords = getHighPoint(grid)
    mainRow = grid[highCoords[0]]

    for index in range(len(mainRow)):
        if index > highCoords[1]:
            mainRow[index] = grid[highCoords[0]][highCoords[1]] - EastSlope * (index - highCoords[1])
        if index < highCoords[1]:
            mainRow[index] = grid[highCoords[0]][highCoords[1]] - WestSlope * (highCoords[1] - index)
def setSubRow(grid):#! this is broken
    highCoords = getHighPoint(grid)
    for rowNum, row in enumerate(grid):
        if row == grid[highCoords[0]]:#! not working
            continue
        topnumIndex = 0
        for index, num in enumerate(row):
            if num != 0:
                topnumIndex = index
        for index in range(len(row)):
            if index > row[topnumIndex]:
                row[index] = grid[rowNum][topnumIndex] - abs(EastSlope * (index - topnumIndex))
            if index < row[topnumIndex]:
                row[index] = grid[rowNum][topnumIndex] - abs(WestSlope * (topnumIndex - index))

def setMainCol(grid):
    highCoords = getHighPoint(grid)
    for rowIndex in range(sideLen):
        slope = 0
        if rowIndex == highCoords[1]:
            pass
        if rowIndex > highCoords[0]:
            slope = SouthSlope
        if rowIndex < highCoords[0]:
            slope = NorthSlope
        grid[rowIndex][highCoords[1]] = grid[highCoords[0]][highCoords[1]] - (abs(highCoords[0] - rowIndex) * slope) #! )#value of the highest - distance from it times slope

def zeroOut(grid):
    for rowIndex, row in enumerate(grid):
        for index, num in enumerate(row):
            if num <= 0:
                grid[rowIndex][index] = 0
            grid[rowIndex][index] = int(grid[rowIndex][index])#* rounds after all the numbers are set

def display():
    for index, row in enumerate(grid):
        print(f"{index + 1}: {row}")
    print("")
def displayChars():
    for row in grid:
        for num in row:
            print(lightLevelDict[num] , end = " ")
        print("")
    print("")

#! doesnt work perfectly but its kinda close, random 0s make it look weird

#* main
generateHighPoint()
#? highPoint works
print("SetMainRow")
setMainRow(grid)
display()

#? setMainRow works
print("SetMainCol")
setMainCol(grid)
display()

print("SetSubRow")
setSubRow(grid)#! something  wrong in here
display()

print("ZeroOut")
zeroOut(grid)
display()
#? main col works

displayChars()

