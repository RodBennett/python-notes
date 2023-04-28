# LAMBDA FUNCTIONS
# @desc: only have one expression, must return a value, unnamed functions

lambda num: num * 2

lambda a, b : a * b

# lambdas can be called via variables, parameters w/o parentheses
multiply = lambda a, b : a * b

print(multiply(2, 4))