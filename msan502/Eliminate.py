
#import necessary libraries
import numpy as np

#define function that calculates the solution to Ax=b given A and b
   
def eliminate(nrow, ncol, matrix, bVec ):

   
    matrix = matrix.astype(float)
    rows = range(1,nrow)
    columns = range(0,ncol-1)
    
    #xans = np.linalg.solve(matrix,bVec) 
    
    pivot = matrix[0,0]
    
    #swap rows if first pivot is zero
    if pivot == 0:
        temp = matrix[[0,]] 
        matrix[0,] = matrix[1,]
        matrix[1,] = temp
        bVec[0] , bVec[1] = bVec[1] , bVec[0]
        
    
    #loop through columns then rows to create a triangular matrix by selecting the appropriate pivot, 
    #calculating the multiplier, and subtracting the multiple of one row to the next rows in the same column
    for j in columns:
        
        for i in rows:
            
            if i == j == (nrow-1): 
                break
        
            #pivots are assumed to be the diagonal of the matrix
            pivot = matrix[j,j]
            
            #swap rows if pivot is zero. Reassign pivot with new row swap
            if pivot == 0:
                temp_m = matrix[[i,]] 
                matrix[i,] = matrix[i+1,]
                matrix[i+1,] = temp_m
                
                bVec[i] , bVec[i+1] = bVec[i+1] , bVec[i]
                
                pivot = matrix[j,j]
            
            if i<j:
                continue
            
            elif i == j:
                lemma = matrix[i+1,j] / pivot
                matrix[i+1,] = matrix[i+1,] - matrix[j,]*lemma
                bVec[i+1] = bVec[i+1] - bVec[i]*lemma
            
            else: 
                lemma = matrix[i,j] / pivot
                matrix[i,] = matrix[i,] - matrix[j,]*lemma
                bVec[i] = bVec[i] - bVec[j]*lemma
            
        #Return error if Permanent Failure
        if not np.any(matrix[nrow-1,]) == True and bVec[nrow-1] !=0:
            print "Permanent Failure with no failure: 0 = number"
            return
        
        #Return error if Infinite Number of Solutions   
        if not np.any(matrix[nrow-1,]) == True and bVec[nrow-1] ==0:
            print "Failure with Infinite Number of Solutions: 0=0" 
            return


    #Perform back substitution to get solution vector
    x = []
    var3=0
    x.append( bVec[-1]/matrix[-1,-1])
    
    for i in range(nrow-2,-1,-1):
        if i== nrow-2:
            var = var = (bVec[i] - matrix[i,i+1]*x[0]) / matrix[i,i]
            x.insert(0,var)

        else:
            for m,j in zip(range(0,len(x)),range (i+1,ncol,1)):
                
                var2 = matrix[i,j]*x[m]
                var3 = var3 + var2
            
            var = (bVec[i] - var3) / matrix[i,i]
            x.insert(0,var)
            var3=0
    
    return  matrix , x  
    
