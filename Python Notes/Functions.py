# Lambda 
odd_or_even = lambda x : print("Even") if x%2==0 else print("Odd")
print(odd_or_even(5))

# functions as objects
def get_func_raised_to_n (n):
    print("inside first func")
    def specified_n(x):
        print("inside second func")
        return x**n
    return specified_n

raised_to_two = get_func_raised_to_n(2)
print(type(raised_to_two))
print(raised_to_two(9))

#OR

def get_func_raised_to_n (n):
    return lambda x: x**n
raised_to_two = get_func_raised_to_n(2)
print(type(raised_to_two))
print(raised_to_two(9))