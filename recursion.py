# RECURSIONS

# @desc - functions in python can call themselves

# Factorial
# 3! 3*2*1 = 6 
# 4! 4*3*2*1 = 24

def factorial(n):
    # first line is base case, required
    if n == 1: return 1
    # second line is recursion case
    return n * (factorial(n - 1))

print(factorial(4))