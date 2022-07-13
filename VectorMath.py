import math
import random

'''
matrix coords
(1,1)  , (1,2)
(2,1)  , (2,2)
(3,1)  , (3,2)
'''

lines = int(input("How many vectors: "))#how tall
#vectorDepth:   2 == 2d, 3 == 3d
#each line is a vector
vectorDepth = 2

def makeVector(vectorDepth, takeUserInput):
    takeUserInput = takeUserInput
    vectorList = []
    if takeUserInput:
        print("\n" + "New vector:")
    for index in range(vectorDepth): 
        if takeUserInput:
            userIn = input("number: ")
            vectorList.append(userIn)
        else:
            vectorList.append(random.randrange(9) + 1)#1 to 9
    return vectorList



matrix = []
for vector in range(lines):
    matrix.append(makeVector(vectorDepth, False))# (depth, userInput)
matrix2 = [[2,4],[3,6]]


def addMatrix(matrix, matrix2):
    matrix3 = []
    for i in range(len(matrix)):
        for i in range(vectorDepth):
            #noen
            print("gg")
            

print(matrix[1][0])