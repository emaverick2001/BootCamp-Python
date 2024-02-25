#tuples
position_1 = (0, )*2
print(position_1)

position_2 = position_1 + (1, 1)
print(position_2)

position_2 += (1, 2)
print(position_2)

print(position_2.count(2))


# position_1 = (1, 0, 1)
# # Tuples are immutable, so the line below will cause an error
# position_1[1] = 2


employee_details = ("David Brent", 42, "Slough", "Manager")
name, age, *other = employee_details
print(name, age, other)


employee_details = ("David Brent", 42, "Slough", "Manager")
*personal_info, location, title = employee_details
print(personal_info, location, title)

# dicitonaries

top_quarterbacks = {'Patriots':'Brady','Saints':'Brees', 'Packers':'Rodgers'}
print(top_quarterbacks)

afc_coaches = dict(Patriots = 'Belichick', Saints = 'Payton')
print(afc_coaches)

# dictionary comprehensions
square = {x : x**2 for x in range(1,11)}
print(square)

#sets

set_of_remainders = { n%13 for n in range(100) if n%11==0}
print(set_of_remainders)