# =============================================================================
# age = int(input("Enter your age: "))
# 
# if age >= 18:
#     print('Yay ! You are eligible to vote')
#     print('You are also eligible for jury duty')
# print('You can\'t vote yet')
# =============================================================================

# Conditional Expressions
x = int(input("Enter your age: "))
print("Positive" if x > 0 else "Negative" if x < 0 else "Zero")

# in operator

list_of_my_cars = ["Civic", "Accent", "Camry", "Corolla"]
if "Civic" in list_of_my_cars:
    print("I own a Civic")
    
# is operator

# checks to see if two vars refer to the same object stored in memory

shopping_list = ["yogurt", "banana", "bread", "eggs"]
shopping_cart = shopping_list

if shopping_cart is shopping_list:
   print("All items in the list are now in the cart")
   
# example
   
age = int(input("Enter your age: "))
driving_experience = int(input("How many years have \
you held a driver's license: "))

if age > 25 and driving_experience > 5:
    print("You are an experienced driver")
    print("We can offer you our premium insurance plan")
elif age < 25 or driving_experience < 5:
    print("We can offer you our young driver plan")
else:
    print("We do not have an insurance plan to offer you")
    
# nesting example

print(9//9)

ones_string = ["zero","one","two","three","four", \
"five","six","seven","eight","nine"]
tens_string = ["ten","twenty","thirty","forty","fifty" \
,"sixty","seventy","eighty","ninety"]

number = int(input("Enter a number : "))

if number>=0 and number<100:
    if (number<10):
        print("You entered "+ones_string[number])
    else:
        print("You entered "+tens_string[number//10 - 1] + \
              " " + ones_string[number%10])
else:
    print("Enter a number between 0 to 99")