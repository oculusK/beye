import numpy as np
list = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(list)

num = arr[0:2, 1:,]

print(num)