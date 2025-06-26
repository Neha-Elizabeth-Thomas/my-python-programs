import pandas as pd 
import numpy as np 
data = np.array(['a1','b1','c1','d1','e1']) 
S= pd.Series(data, index = [1001, 1002, 1003, 1004, 1005]) 
print(S[[1002, 1003, 1004]])


arr1 = np.arange(6).reshape((3, 2))
print(arr1)
print(a)
arr2 = np.arange(6).reshape((3, 2))

# The operation that produces [[0,1],[4,5],[8,9]]
arr3 = arr1 + arr2[0].reshape((1,2))
print(arr3)