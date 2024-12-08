# Repeat all the examples

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

# Multi-dimensional Arrays

# 2 dimension Array
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape:', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Getting items from a numpy array
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row:', third_row)

first_column = two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Thirs column:', third_column)
print(two_dimension_array)
print('--------------------')

# Slicing Numpt array
first_two_row_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_row_and_columns)
print('--------------------')

# Reversing rows and the whole array
print(two_dimension_array[::-1, ::-1])
print('--------------------')

# Representing missing values
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)
print('--------------------')

# Numpy Zeroes
numpy_zeroes = np.zeros((3, 3), dtype = int, order = 'C')
print(numpy_zeroes)
print('--------------------')

numpy_ones = np.ones((3, 3), dtype = int, order = 'C')
print(numpy_ones)

twoes = numpy_ones * 2
print('--------------------')

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
print('--------------------')
reshaped = first_shape.reshape(3, 2)
print(reshaped)
print('--------------------')

flattened = reshaped.flatten()
print(flattened)
print('--------------------')

# Horizontal Stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('--------------------')

# Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
print('--------------------')

# Generating random numbers
# Random float
random_float = np.random.random()
print(random_float)
print('--------------------')

# List of random floats
random_floats = np.random.random(5)
print(random_floats)
print('--------------------')

# Generating a random integer between 0 and 10
random_int = np.random.randint(0, 10)
print(random_int)
print('--------------------')

# Generating a random integers between 2  and 11, and creating a one row array
random_int = np.random.randint(2, 10, size = 4)
print(random_int)
print('--------------------')

# Generating a random integers between 0 and 10
random_int = np.random.randint(2, 10, size = (3, 3))
print(random_int)
print('--------------------')

# Generationg random numbers
# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
print('----------------------------')

# Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
df = sns.load_dataset("penguins")
print(plt.hist(normal_array, color = 'grey', bins = 50))
print('----------------------------')

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype = float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)
print('----------------------------')

# Numpy numpy.arange()
# Creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)
print('----------------------------')

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
print('----------------------------')

# Creating sequence of numbers using linspace
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 20 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num = 10))
print('----------------------------')

# Not to include the last value in the interval
print(np.linspace(1.0, 5.0, num = 5, endpoint = False))
print('----------------------------')

# LogSpace
# Returns even spaced numbers on a log scales. LogSpace has the same paremeters as np.linspace.

# Syntax: numpy.logspace(start, stop, num, endpoint)
print(np.logspace(2, 4.0, num = 4))

# To check the size of an array
x = np.array([1, 2, 3], dtype = np.complex128)
print(x)
print(x.itemsize)
print('----------------------------')

# Indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)
print('First row:', np_list[0])
print('Second row:', np_list[1])

print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

# NumPy Statistical Functions with Example

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
print('----------------------------')

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))
print('----------------------------')

# How to create repeating sequences
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))
print('----------------------------')

# How to generate random numbers
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
print('----------------------------')

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
print('----------------------------')

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print('----------------------------')

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)
print('----------------------------')

rand2 = np.random.randn(2,2)
print(rand2)
print('----------------------------')

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)
print('----------------------------')

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

print(plt.hist(np_normal_dis, color="grey", bins=21))
print(plt.show())
print('----------------------------')

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)

# LINEAR ALGEBRA
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g) ) # 23
print('----------------------------')

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))
print('----------------------------')

## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)

print(np.linalg.det(i))
print('----------------------------')


Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

print(Z)
print('----------------------------')

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)
print('----------------------------')

np_arr = np.array(range(0, 11))
print(np_arr + 2)
print('----------------------------')

# We use linear equation for quantities which have linear relationship. Let's see the example below:
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

print(plt.plot(temp,pressure))
print(plt.xlabel('Temperature in oC'))
print(plt.ylabel('Pressure in atm'))
print(plt.title('Temperature vs Pressure'))
print(plt.xticks(np.arange(0, 6, step=0.5)))
print(plt.show())

# To draw the Gaussian normal distribution using numpy. As you can see below, the numpy can generate random numbers. To create random sample, we need the mean(mu), sigma(standard deviation), mumber of data points.

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.kdeplot(df[x])
print(ax.set(xlabel="x", ylabel='y'))
print(plt.show())