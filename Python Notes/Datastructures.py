import copy
# =============================================================================
# x = 4234
# y = x
# print("Address of x :",id(x))
# print("Address of y :",id(y))
# x = x + 1
# #y = "Hi"
# print("Address of x post increment:",id(x))
# print("Address of y post edit :",id(y))
# =============================================================================
# =============================================================================
# my_list = [8,9,1,3,7,2,5]
# print(my_list[:4])
# print(my_list[1:4])
# print(my_list[:])
# print(my_list[0:6:2]) #prints 8,1,7
# print(my_list[0:7:2]) #prints 8,1,7,5
# =============================================================================

# Initialize a list
my_list = [8,9,1,3,7,2,5]
# Use * to append together three copies of a one-element list
# containing 0, and store this in a new variable
three_zeroes = [0]*3
# Now, change every other element of my_list to zero
my_list[1::2] = three_zeroes
print(my_list)

list_1 = [1,5]
list_1 = list_1*4
list_2 = [5,3]
list_3 = list_1 + list_2
print(sum(list_2))
print(min(list_2))
print(max(list_2))

# reversing a list w/out using reverse method
print(my_list[::1])
print(my_list[::-1])

# copying a list
list_one = [2, 4, 6]
list_two = list_one
print("List 1 address : ", id(list_one))
print("List 2 address : ", id(list_two))
list_one.append(5)
print("List 1 : ", list_one)
print("List 2 : ", list_two)
print("List 1 address : ", id(list_one))
print("List 2 address : ", id(list_two))

# shallow vs deepcopy
# shallow
list_i = [2, 4, 6]
list_j = [1, 6, 9]
list_one = [list_i, list_j]
list_two = list_one[:]
print("Lists copied")
print(list_one)
print(list_two)
list_i.append(2)
print("One of the member lists is modified")
print(list_one)
print(list_two)

# deep 
list_two = copy.deepcopy(list_one)
print("Lists copied")
print(list_one)
print(list_two)
list_i.append(3)
print("One of the member lists is modified")
print(list_one)
print(list_two)