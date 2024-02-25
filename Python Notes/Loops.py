# =============================================================================
# i = 1
# sum_square = 0
# while (i<=3):
#     sum_square += (i*i)
#     i += 1
# print("sum of square is :", sum_square)
# =============================================================================

# =============================================================================
# while 1:
#     print("When will this end?")
# =============================================================================
    
# =============================================================================
# # Collatz conjecture
# x = float(input("Enter any positive number:"))
# steps = 0
# while(x != 1) :
#     if(x % 2 == 0):
#         x = x//2
#     else:
#         x = 3*x + 1
#     steps += 1
# print("Number of steps:",steps)
# 
# # list comprehensions
# 
# # List of the squares of all numbers from 1 to 10
# list_squares = [x*x for x in range(1,11)]
# print("List of squares : ", list_squares)
# 
# # List of the squares of all numbers from 1 to 10
# # that are divisible by 2
# list_squares = [x*x for x in range(1,11) if (x%2)==0]
# print("List of squares of even numbers only : ", list_squares)
# # List that has squares of all numbers from 1 to 10
# # and zeros if a number is odd
# list_squares = [x*x if (x%2)==0 else 0 for x in range(1,11) ]
# print("List of squares of even numbers : ", list_squares)
# =============================================================================

# find the sum of the square of the integers 1 to 1000
result = sum(x*x for x in range(1,1001))
print(result)