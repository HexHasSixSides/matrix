# matrix.py
# created by Mario Reyes
# December 18 2019


def main():
    numColumns = int(input("Number of columns in the matrix: "))
    numRows = int(input("Number of rows in the matrix: "))
    
    matrix = makeMatrix(numColumns, numRows)
    matrixValues(matrix, numRows)
    
    scaleMatrix(matrix, 100)
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
        row[index] = number * scalar
        
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
    


def insertionSort(numList): 
    for index in range(1, len(numList)):
        
        keyValue = numList[index]
        previousValue = numList[index-1]
        
        while index >= 1 and previousValue > keyValue:
            numList[index] = numList[index-1]
            index -= 1
            previousValue = numList[index-1]
        
        numList[index] = keyValue
  


def largestItem(lenList):
    
    insertionSort(lenList)
    
    spaces = lenList[-1]
    return spaces
        
        
def numLen(num):
    return len(str(abs(num)))
  

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
    
    for row in matrix:
        print ('[%s]' % (' '.join('%09s' % i for i in row)))
        


        

        
        
            
        
        

    
main()
