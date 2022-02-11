###############################
# TITLE : Numpy02
# CREATE DATE : 2022-02-08
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################

# Numpy datatype

import numpy as np
print(np.__version__)

data = [1.1, 2, 3]
a = np.array(data)
print(a)
print(a.dtype)

a = np.array(data, dtype=np.float32)
print(a)
print(a.dtype)

a = np.array(data, dtype=np.int32)
print(a)
print(a.dtype)

a = np.array(data, dtype="i4")
print(a)
print(a.dtype)
print("=====================")

data = [1.1, 2, 3]
a = np.float64(data)
print(a.dtype)
a = np.int32(data)
print(a.dtype)
print("=====================")

data = [2.1, 3, 4]
a= np.float64(data)
print(a.dtype)
a= a.astype(np.int64)
print(a.dtype)
print("=====================")

data = [1.0, 2.0, 3.0]
a = np.float64(data)
print(a.dtype)
print(a)
a = a.astype(np.string_)
print(a.dtype)
print(a)
a = np.uint16(0)
print(a.dtype)
print(a)
a = np.uint16(-1)
print(a)

# Numpy
# Scalar : What exists only as a single data value
# Vector : The arrangement of numbers(1D array)
# Matrix : 2D arrangement of numbers (rows : columns)

# Scalar
print("=====================")
print("Scalar=====================")
a = np.array(1)
print(a)
print(a.shape, a.ndim)
print("Vector=====================")
a = np.array([1, 2, 3])
print(a)
print(a.shape, a.ndim)

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(a)
print(a.shape, a.ndim)

a = np.array([[1]])
print(a)
print(a.shape, a.ndim)

arr_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_matrix )
print(arr_matrix .shape, arr_matrix.ndim)

arr_tensor = np.array([[[1, 2], [1, 2], [1, 2]], [[1, 2], [1,2], [1, 2]]])
print(arr_tensor)
print(arr_tensor.shape, arr_tensor.ndim)
