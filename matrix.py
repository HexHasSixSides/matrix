# matrix.py
# created by Mario Reyes
# December 18 2019

from decimal import Decimal

def main():
    numColumns = int(input("Number of columns in the matrix: "))
    numRows = int(input("Number of rows in the matrix: "))
    
    matrix = makeMatrix(numColumns, numRows)
    matrixValues(matrix, numRows)

    printMatrix(matrix)

    reduceColumn(matrix,0)
    printMatrix(matrix)
    
    
    
#--------------------------------------------------------------
# makeMatrix                                                   
#                                                              
# function that initializes matrix with 0 values to            
# the dimensions provided by the user                          
# --------------------------------------------------------------
# inputs:
#
# columns    -    number of columns in desired matrix
# rows       -    number of rows in desired matrix
#---------------------------------------------------------------
# return values:
#
# matrix     -    the initialized matrix with zero values inside
#---------------------------------------------------------------
# notes:
# 
# N/A
#---------------------------------------------------------------
def makeMatrix(columns, rows):
    matrix = [[0 for column in range(columns)] for row in range(rows)]
    return matrix



#--------------------------------------------------------------
# stringToList
#
# function that takes in a string and converts it to a list where
# every element of the list is an element of the string separated 
# by a space converted to int
# --------------------------------------------------------------
# inputs:
#   
# string     -    string to convert to list of ints
#---------------------------------------------------------------
# return values:
#
# row        -    returns the row representation for the matrix
#---------------------------------------------------------------
# notes:
# 
# - used in method makeValues
#---------------------------------------------------------------
def stringToList(string):
    row = string.split()
    
    index = 0
    for item in row:
        row[index] = float(item)
        index += 1
        
    return row
    
    
    
#--------------------------------------------------------------
# makeValues
#
# function that asks user for values of each element in every 
# row of the matrix and changes the numbers in the lists
# accordingly
# --------------------------------------------------------------
# inputs:
#
# matrix     -    matrix whose values will be changed 
# rows       -    number of rows in matrix
#---------------------------------------------------------------
# return values:
#
# N/A
#---------------------------------------------------------------
# notes:
# 
# - this function also utilizes the stringToList method to turn 
#   the user inputted rows into a list of integers
#---------------------------------------------------------------
def matrixValues(matrix, rows):
    counter = 0
    while counter < rows:
        
        rowValues = input("Enter the values in row " + str(counter+1) + 
                              " separated by a space: ")
                            
        row = stringToList(rowValues)
        matrix[counter] = row
        counter += 1
 
 
 
#--------------------------------------------------------------
# scaleRow
#
# function that takes in a row of a matrix as well as a scalar
# and scales the entire row by that scalar value
# 
# --------------------------------------------------------------
# inputs:
#
# row        -    row of thematrix to be scaled
# scalar     -    scalar that will be mutliplied to the row
#---------------------------------------------------------------
# return values:
#
# row        -    returns the scaled row value
#---------------------------------------------------------------   
def scaleRow(row, scalar):
    
    index = 0
    for number in  row:
        row[index] = (number) * (scalar)
        
        index+=1
        
    return row



#--------------------------------------------------------------
# scaleMatrix
#
# function that takes in a matrix and a scalar and scales the
# entire matrix by that value
# 
# --------------------------------------------------------------
# inputs:
#
# matrix     -    matrix whose values will be scaled 
# scalar     -    scalar that will scale the entire matrix
#---------------------------------------------------------------
# return values:
#
# matrix     -    returns a new matrix with scaled values
#---------------------------------------------------------------
# notes:
# 
# - this function utilizes the scaleRow method to scale 
#   the row values in the original matrix
#---------------------------------------------------------------
def scaleMatrix(matrix, scalar):
    index = 0
    
    for row in matrix:
        matrix[index] = scaleRow(row, scalar)
        
        index += 1
            
    return matrix



#--------------------------------------------------------------
# matrixDimensions
#
# function that takes in a matrix, gets its row length and 
# column length to retrieve its dimensions, and returns a list
# with elements row length and column length (row x column)
# --------------------------------------------------------------
# inputs:
#
# matrix       -    matrix whose dimensions will be calculated
#---------------------------------------------------------------
# return values:
#
# dimensions  -    list that  contains the dimensions of matrix
#---------------------------------------------------------------
# notes:
#
# - utilizes both rowLength and columnLength functions to compute
#   matrix dimensions
#---------------------------------------------------------------
def matrixDimensions(matrix):
    rowLen = rowLength(matrix[0])
    columnLen = columnLength(matrix)

    dimensions = [rowLen, columnLen]
    
    return dimensions



#--------------------------------------------------------------
# rowLength
#
# function that takes in a row and returns the number of 
# elements found inside 
# --------------------------------------------------------------
# inputs:
#
# row        -    a row of a matrix 
#---------------------------------------------------------------
# return values:
#
# rowLength  -    integer number of elements in a row 
#---------------------------------------------------------------
def rowLength(row):
    rowLength = len(row)

    return rowLength



#--------------------------------------------------------------
# columnLength
#
# function that takes in a matrix and returns the number of 
# elements in every column of the matrix 
# --------------------------------------------------------------
# inputs:
#
# matrix      -   the matrix whose column length will be counted
#---------------------------------------------------------------
# return values:
#
# columnLength  -  integer number of number of elements in
#                  column of matrix 
#---------------------------------------------------------------
def columnLength(matrix):
    columnLength = len(matrix[0])

    return columnLength



#--------------------------------------------------------------
# rowSubtract
#
# function that takes two different rows of a matrix and 
# performs subtraction of the first provided row with the second
# provided row and saves the new values in the second provided
# row
# --------------------------------------------------------------
# inputs:
#
# row1        -    row that will be subtracted from row2
# row2        -    row that will get changed by row1
#---------------------------------------------------------------
# return values:
#
# N/A
#---------------------------------------------------------------
# notes:
#
# - utilizes the rowLength function to calculate the length of 
#   the rows of the matrix for the while loop
#---------------------------------------------------------------
def rowSubtract(row1, row2):
    rowLen = rowLength(row1)
    counter = 0

    while counter != rowLen:
        newRowEntry = Decimal(str(row2[counter])) - Decimal(str(row1[counter]))
        row2[counter] = newRowEntry
        counter += 1

    


#--------------------------------------------------------------
# insertionSort
# 
# function that performs the well-known insertion sort algrthm
# on a row of a matrix
# --------------------------------------------------------------
# inputs:
#
# row         -    row of matrix that will be sorted in
#                 ascending order
#---------------------------------------------------------------
# return values:
#
# N/A
#---------------------------------------------------------------
def insertionSort(row): 
    for index in range(1, len(row)):
        
        keyValue = row[index]
        previousValue = row[index-1]
        
        while index >= 1 and previousValue > keyValue:
            row[index] = row[index-1]
            index -= 1
            previousValue = row[index-1]
        
        row[index] = keyValue
  


#--------------------------------------------------------------
# largestItem
# 
# function that takes in a row and finds the largest value
# present in that row
# --------------------------------------------------------------
# inputs:
#
# row         -    row of matrix whose largest element will be
#                  found in
#---------------------------------------------------------------
# return values:
#
# largestItem  -   integer of the largest number in the row
#---------------------------------------------------------------
# notes:
#
# - utilizes the insertionSort function to sort a copy of the 
#   row and grab its last element once it is sorted to grab
#   the largest number
#---------------------------------------------------------------
def largestItem(row):
    # added the '[:]' to copy the list and not change
    # the actual row in the matrix
    p_row = row[:] 
    insertionSort(p_row)
    largestItem = p_row[-1]

    return largestItem



#--------------------------------------------------------------
# numLen
# 
# function that takes in a number and returns the number of 
# spaces it takes up 
# --------------------------------------------------------------
# inputs:
#
# number       -   number whose spaces will be counted
#---------------------------------------------------------------
# return values:
#
# N/A  -   integer of the number of spaces the number takes up
#---------------------------------------------------------------
def numLen(num):
    return len(str(abs(num)))
  


def reduceColumn(matrix, column):
    numRows = rowLength(matrix[0])
    numColumns = columnLength(matrix)

    pivotRow = matrix[column]
    pivotPosition = pivotRow[column]

    # makes a list of the elements in the column of the matrix
    columnList = []
    for row in matrix:
        columnList.append(row[column])


    # makes a list of scalars needed to get zero under the pivot
    # position once subtracted 
    scalarNumbers = []
    for number in columnList[1:]:

        scalar = number/pivotPosition
        scalarNumbers.append(scalar)

    counter = 1
    for scalar in scalarNumbers:

        undoScalar = 1/(scalar)
        newRow = scaleRow(pivotRow, scalar)
        matrix[column] = newRow

        rowSubtract(matrix[column], matrix[column+counter])

        rowBefore = scaleRow(pivotRow, undoScalar)
        matrix[column] = rowBefore

        counter += 1



    print(columnList)
    print(scalarNumbers) 

        

def ref(matrix):
    numRows = rowLength(matrix[0])
    numColumns = columnLength(matrix)

    
#--------------------------------------------------------------
# printMatrix
#
# function that prints an entire matrix to the screen
# 
# --------------------------------------------------------------
# inputs:
#
# matrix     -    matrix to be printed to screen
#---------------------------------------------------------------
# return values:
#
# N/A
#--------------------------------------------------------------- 
def printMatrix(matrix):

    dimensions = matrixDimensions(matrix)
    row = str(dimensions[0])
    column = str(dimensions[1])

    print(" ")
    print("--------------------------------------------")
    print("#####################")
    print("#  |"+row+" x "+column+"  MATRIX|  #")
    print("#####################")

    for row in matrix:
        print ('[%s]' % (' '.join('%09s' % i for i in row)))
    
    print("--------------------------------------------")

        


        

        
        
main()
