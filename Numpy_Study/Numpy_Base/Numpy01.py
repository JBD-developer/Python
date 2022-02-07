###############################
# TITLE : Numpy01
# CREATE DATE : 2022-02-07
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# Numpy ?

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
print(type(arr))

dataone = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dataTwo = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

for i in range(len(dataone)):
    for j in range(len(dataone[0])):
        dataone[i][j] *= 2
print(dataone)

for i in range(len(dataone)):
    for j in range(len(dataone[i])):
        dataone[i][j] += dataTwo[i][j]
print(dataone)



