# this is a commented line
# indentation matters in Python very much
# everything indented belongs to a block in Python


name = "Rod"
#  types: string(str), whole number(int), decimal(float), boolean(bool)
print(type(name) == str)
print(isinstance(name, str))

age = 2
print(isinstance(age, int))

age = 2.5
print(isinstance(age, float))

age = float(2)  # can manaully set type. 2 is int, but you can set it as float
print(isinstance(age, float))

# CASTING - data type conversions
number = "20"
age = int(number)
print(isinstance(age, int))




