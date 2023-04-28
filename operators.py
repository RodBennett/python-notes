# OPERATORS

1 + 1 # add
2 - 1 # subtract
2 * 2 # multiply
4 / 2 # division
4 % 3 # modulus
4 ** 2 # exponent
5 // 2 # floor division, returns rounded down whole int if remainder


age = 8
age += 8
print(age)

# CAN USE += OPERATOR FOR STRINGS IN PYTHON:
name = "Rod"
name += " is a swell guy."
print(name)

# COMPARISON OPERATORS: == != > < >= <=

# BOOLEAN OPERATOR: or (if first argument is falsy, go to 2nd argument...if 1st arg is true, print 1st argument)

print(0 or 1) # 0 is falsy
print(False or "hey") # returns first true value, "hey"
print("hi" or "hey") # returns first true value "hi"
print([] or False) # returns false (empty arrays are falsy)
print(False or []) # returns [] because "False" is falsy and or operator always goes to second value

#  BOOLEAN OPERATOR: and (if both are truthy, pring 2nd value only)

print (0 and 1)
print(False and "hey")
print("hi" and "hey")
print([] and False)
print(False and [])

# IDENTITY OPERATOR: is
# MEMBERSHIP OPERATOR: in - tests if somehting is in a list

#  TERNARY OPERATOR
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult2(age):
    return True if age > 18 else False
    
print(is_adult2(16))

# MULTI LINE STRING
print("""My

name

is 

Rod
""")
      
# STRING METHODS
print("rod".upper()) # toUpperCase() in JS
print("ROD".lower()) # toLowerCase() in JS
print("rod person".title()) # capitalizes frist letter of each word like toUpperCase()[0]
print("rod".islower()) # Boolean for if all are lower
print("rod".isupper()) # Boolean for if all are upper

name = "Rod"
print(len(name)) # len is length of string
print("o" in name) # checks to see if substring exists in original string

#  ESCAPE OPERATOR
name = "R\nod Bennett"

# get specific charcter on string by index
name = "Wendy"
print(name[0])
print(name[-1])

# SLICE OPERATOR
print(name[1:3]) # returns "en"

# can also use empty values to signify beginning or end of string in slice operator
print(name[:3]) # returns Wen
print(name[1:]) # returns endy
print(len(name) - 1)

# ALL BOOLEAN

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked]) # True only is ALL conditions are true
print(ready_to_serve)

# COMPLEX NUMBERS - one part real, one part imaginary
num1 = 2+3j
num2 = complex(2,3)

print(num2.real, num2.imag)

# ABSOLUTE VALUE
print(abs(-5.5))
# ROUNDUP/ROUND DOWN
print(round(5.49))
print(round(5.434, 1)) # rounding to specified decmimal point or toFixed()) in JS

# ENUMS TO CREATE CONSTANT VARIABLES IN PYTHON (no const, var, let in python)
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))
print(State["ACTIVE"])
print(list(State))
print(len(State))

# INPUT OPERATOR
age = input("What is your age? ")
print("Your age is " + age)
