import numpy as np
x = np.zeros(5, dtype=np.int32)
print("Zeros:", x)

x = np.ones(5, dtype=np.float64)
print("Ones:", x)

x = np.array([1,2,4,5], dtype=np.float32)
print("From list:", x)

# create an array with 6 evenly-spaced values spread over [0,1]
x = np.linspace(0,1,6)
print("6 pts between 0, 1:", x)

# Similar to the range function
x = np.arange(5)
print("Arange:", x)


# attributes

# Create a two by two matrix
a = np.zeros((2,2))

print(a)

print("No. of dimensions of a ", a.ndim)
print("Shape of array a ",a.shape)
print("No. of elements of a ",a.size)

# reshaping data

x = np.linspace(1,6,6,dtype=np.int32)
print(x)

b = x.reshape(2,3)
print("Array after reshaping ")
print(b)

# Array operations

# Similar to the range function
x = np.arange(1,10)

divisible_by_3 = x[x%3==0]
divisible_by_3_2 = x[(x%3==0) & (x%2==0)]

print(x%3==0)
print(divisible_by_3)
print(divisible_by_3_2)

# Expressions

x = np.ones(5)
y = np.ones(5)
print(x+y)
print(x+5)

# Functions
x = np.ones(10)

print(np.sin(x))

# calculating an expression 2 wways

# first way

x = np.random.random(10000)
y = np.random.random(10000)

f_sum = 0
for a,b in zip(x,y):
    f_sum += np.cos(a+b) + a**2

print(f_sum)

# second way

f_sum2 = np.sum(np.cos(x+y) + x**2)
print(f_sum2)