# Repeat all the examplessdvsdv

# Importing numpy
import numpy as np
# Version of numpy
print('numpy:', np.__version__)
# Methods of numpy
# print(dir(np))

# Creating int numpy arrays
# Python list
python_list = [1, 2, 3, 4, 5]

# Checking data types
print('Type:', type(python_list))
print(python_list)

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(two_dimensional_list)

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating float numpy arrays
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

# Creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 1], dtype=bool)
print(numpy_bool_array)

# Creating multidimensional array using numpy
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array:', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_tuple: ', python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]])
print(three_by_four_array.shape)

# Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]])

print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)

# Mathematcial Operation using numpy

# Adition
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

# Substraction
print('original array:', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

# Multiplication
print('Original array:', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

# Division
print('Original array:', numpy_array_from_list)
ten_divided_original = numpy_array_from_list / 10
print(ten_divided_original)

# Modulus
print('Original array:', numpy_array_from_list)
ten_modulus_original = numpy_array_from_list % 10
print(ten_modulus_original)

# Floor Division
print('Original array:', numpy_array_from_list)
ten_floor_division_original = numpy_array_from_list // 10
print(ten_floor_division_original)

# Exponential
print('Original array:', numpy_array_from_list)
two_exponential_original = numpy_array_from_list ** 2
print(two_exponential_original)

# Checking data types

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2 ,3], dtype = 'bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Converting types
print('-------------------------')
# Int to Float
numpy_int_arr = np.array([1, 2, 3, 4], dtype = 'float')
print(numpy_int_arr)
print(numpy_int_arr.dtype)

# Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)
print(numpy_int_arr.dtype)

# Int ot boolean
numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(numpy_int_arr)
print(numpy_int_arr.dtype)

# Int to Str
numpy_float_list = numpy_float_arr.astype('int').astype('str')
print(numpy_float_list)
print(numpy_float_list.dtype)