#Creating a sparse matrix with random numbers 
import timeit
import scipy.sparse as sparse
import scipy.stats as stats
import numpy as np
from scipy.sparse import csr_matrix 

start_time = timeit.default_timer()
# create sparse random matrix with specific random numbers
rvs = stats.norm(loc=3, scale=1).rvs
.
S = sparse.random(5, 5, density=0.25, data_rvs=rvs)

sparseMatrix=S.toarray()
print('sparse matrix including zeros')
print(sparseMatrix)

   
size = 0
  
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            size += 1
  

rows, cols = (3, size) 
compactMatrix = [[0 for i in range(cols)] for j in range(rows)] 
  
k = 0
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            compactMatrix[0][k] = i 
            compactMatrix[1][k] = j 
            compactMatrix[2][k] = sparseMatrix[i][j] 
            k += 1
print("Array with non zero numbers from sparseMatrix")
for i in compactMatrix: 
    print(i)

stop_time = timeit.default_timer()
print('Time:', stop_time - start_time)