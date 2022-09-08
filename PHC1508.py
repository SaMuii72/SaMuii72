ls = [21,35,12,45,78,65,95,12,32,12,45,65,75,85]
x = 0
for i in ls:
  x += i 
print(x/len(ls))

b = 0
for n in ls:
    for o in range(len(ls)-1):
        if (ls[o]  > ls[o+1]):
            ls[o], ls[o+1]  =  ls[o+1],ls[o]    
print(ls)
print("Med = " + str(ls[7]))

import numpy as np 
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[0,3])