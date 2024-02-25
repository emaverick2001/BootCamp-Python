

def compute_func (x, y):
    # makes sure only digits are inputted
    assert (isinstance(x,int) or isinstance(x,float)), "Pass a number"
    return 3*(x+y)

print(compute_func('a','b'))
# print(compute_func('0','1'))

