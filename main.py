# import numpy as np
#
# arr = np.array((1, 2, 3, 4, 5, 6))
# print(arr)
# print(type(arr))

# creating a 0-D array

import numpy as np
arr = np.array(42)
print(arr)

# creating a 1-D array

import numpy as np
arr = np.array((1, 2, 3, 4, 5, 6))
print(arr)

# creating a 2-D array

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# creating 3-D array

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Checking the number of Dimensions (ndim)

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4])
c = np.array([[1, 2, 3], [1, 2, 3]])
d = np.array([[[1, 2], [1, 2]], [[1, 2], [1, 2]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# creating higher dimemsions

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print(arr.shape)
print("the number of dim:", arr.ndim)

# Array indexing

import numpy as np
arr = np.array((1, 2, 3, 4, 5, 6))
print(arr[2] + arr[4])

# Accessing 2-D arrays

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr[0, 2])

# Slicing an Array

import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# start:stop:step
print(arr[1:5])
print(arr[0:8:2])
print(arr[:5])
print(arr[::2])

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(arr1[1:3, :])
print(arr1[:, 1:3])
print(arr1[2:3:3])
