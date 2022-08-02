import math
import random


#https://byjus.com/jee/matrix-operations/


def matrixMaker(numVectors,vectorDepth):#makes random matrixes
    matrix = []
    for i in range(numVectors):
        vector=[]
        for j in range(vectorDepth):
            vector.append(random.randint(0,9))
        matrix.append(vector)
    return matrix #final matrix

def vectorMaker(vectorDepth):
    vector=[]
    for j in range(vectorDepth):
            vector.append(random.randint(0,9))
    return vector

def betterVectorMaker():
    vector = str(input("enter a vector using parentheses(): "))
    vec = []
    #vector is a string here
    numcnt = 0
    for char in vector:
        if char == ",":
            numcnt+=1

    num = ""
    while numcnt > 0:
        if char.isnumeric():
            num += char
        if char == "," or char == ")":
            numcnt -=1
            vec.append(int(num))
            num = ""
    return vec

def betterMatrixMaker():
    matrix = []
    matrixDepth = int(input("how many vectors: "))
    for i in range(matrixDepth):
        matrix.append(betterVectorMaker())
    return matrix


def isEqualMatrixSize(matrixOne,matrixTwo):
    if len(matrixOne) != len(matrixTwo):
        return False
    for vectors in range(len(matrixOne)):
        if len(matrixOne[vectors]) != len(matrixTwo[vectors]):
            return False
    return True

def RowSwap(matrix, swapCnt):
    newMatrix = []
    for index,vector in enumerate(matrix, start = swapCnt):#!not done, need to move the vecotrs ny a certain index, so loop from the givne index and back to zero
        newMatrix.append(vector)
    #swap rows by gievn index
    print("swapping rows")
def colSwap(matrix, swapCnt):
    #swap cols by given index
    print("swaping cols")

def addMatrix(matrixOne, matrixTwo):
    matrixAdded = []
    #stop is the max vector leght to add
    isEqualMatrixSize(matrixOne,matrixTwo)    
    vecIndex = 0
    for vector in matrixOne:
        addedVec = []
        for index in range(len(vector)):
            addedVec.append(matrixOne[vecIndex][index] + matrixTwo[vecIndex][index])
        vecIndex+=1
        matrixAdded.append(addedVec)

    return matrixAdded


def lengthOfVector(vector):
    sumOfVec = 0
    for num in vector:
        sumOfVec += num * num
    return math.sqrt(sumOfVec)

def dotProduct(vectorOne, vectorTwo):#!only for 2 vectors
    #https://wikiless.org/wiki/Dot_product?lang=en
    dotProduct = []
    stop = min([len(vectorOne), len(vectorTwo)])
    for index in range(stop):
        dotProduct.append(vectorOne[index] * vectorTwo[index])
    return sum(dotProduct)

def displayMatrix(matrix):
    for vector in matrix:
        print(vector)
    print("\n")

def findMinLen(matrix):
    #finds smallest vector length
    #used for vector maths as a stoping point
    minLenList = []
    for vector in matrix:
        minLenList.append(len(vector))
    return min(minLenList)

def getMatrixLen(matrix):
    return(len(matrix))

matrixA = matrixMaker(1,3)
matrixB = matrixMaker(1,3)

print(matrixA)
print(matrixB)
print(addMatrix(matrixA,matrixB))
'''
matrixC = matrixMaker(3,2)

displayMatrix(matrixA)
print(dotProduct(matrixA[0],matrixA[1]))
print(lengthOfVector(matrixA[0]))

displayMatrix(matrixB)
print(dotProduct(matrixB[0],matrixB[1]))
displayMatrix(matrixC)


print(betterMatrixMaker())'''
#printing len(matrixA) is the amount of vectors
#printing len(matrixA[0]) is the lenght of vectors

#print(len(matrixA[1]))
#print(findMinLen(matrixA))
