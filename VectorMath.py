import math
import random


#https://byjus.com/jee/matrix-operations/
'''
could make oop by having a vector be an extension of a matrix
'''
class matrix():
    def __init__(self, numVectors, VectorDepth):
        self.Vectors = numVectors
        self.Depth = VectorDepth
        self.matrix = matrixMaker(numVectors,VectorDepth)

    def matrixMaker(numVectors,vectorDepth):#makes random matrixes
        matrix = []
        for i in range(numVectors):
            vector=[]
            for j in range(vectorDepth):
                vector.append(random.randint(0,9))
            matrix.append(vector)
        return matrix #final matrix
        
class vector():
    def __init__(self, VectorDepth):
        self.Depth = VectorDepth
        self.vector = vectorMaker(VectorDepth)
    
    def vectorMaker(vectorDepth):
        vector=[]
        for j in range(vectorDepth):
                vector.append(random.randint(0,9))
        return vector



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
def lengthOfVector(vector):
    sumOfVec = 0
    for num in vector:
        sumOfVec += num * num
    return math.sqrt(sumOfVec)

#! not done
def RowSwap(matrix, swapCnt):
    newMatrix = []
    start = swapCnt % len(matrix)
    for vector in range(start , len(matrix)):
        newMatrix.append(vector)
    for index in range(0, start):
        newMatrix.append(matrix[index])
    #swap rows by gievn index
    return newMatrix

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
def subtractMatrix(matrixOne, matrixTwo):
    matrixSubtracted = []
    #stop is the max vector leght to add
    isEqualMatrixSize(matrixOne,matrixTwo)    
    vecIndex = 0
    for vector in matrixOne:
        addedVec = []
        for index in range(len(vector)):
            addedVec.append(matrixOne[vecIndex][index] - matrixTwo[vecIndex][index])
        vecIndex+=1
        matrixSubtracted.append(addedVec)

    return matrixSubtracted
def matrixScale(matrix, scalar):
    scaledMatrix = []
    for vector in matrix:
        newVec = []
        for num in vector:
            newVec.append(num * scalar)
        scaledMatrix.append(newVec)
    return scaledMatrix

def dotProduct(vectorOne, vectorTwo):#!only for 2 vectors
    #https://wikiless.org/wiki/Dot_product?lang=en
    dotProduct = []
    stop = min([len(vectorOne), len(vectorTwo)])
    for index in range(stop):
        dotProduct.append(vectorOne[index] * vectorTwo[index])
    return sum(dotProduct)

def pythag(vectorOne,vectorTwo):
    return math.sqrt(math.pow(lengthOfVector(vectorOne),2) + math.pow(lengthOfVector(vectorTwo),2))

def findMinLen(matrix):
    #finds smallest vector length
    #used for vector maths as a stoping point
    minLenList = []
    for vector in matrix:
        minLenList.append(len(vector))
    return min(minLenList)

def getMatrixLen(matrix):
    return(len(matrix))

def displayMatrix(matrix):
    for vector in matrix:
        print(vector)
    print("\n")

matrixA = matrixMaker(1,3)
matrixB = matrixMaker(1,3)

print(matrixA)
print(matrixB)

print(addMatrix(matrixA,matrixB))

print(dotProduct(matrixA[0],matrixB[0]))

print(pythag([3],[4]))#tested on a perfect ratio hypotenuse, but works with any vectors

matrixX = matrixMaker(5,1)#5 vecrtos
displayMatrix(matrixX)

print(RowSwap(matrixX,2))
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
#printing len(matrixA[0]) is the length of a vector

#print(len(matrixA[1]))
#print(findMinLen(matrixA))
