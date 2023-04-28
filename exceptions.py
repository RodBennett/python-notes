# EXCEPTIONS
# @syntax: try/except blocks

try: 
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally: 
    result = 1

print(result)

# Exception is a base class for non-exit exceptions. Non-exit exception allows your code to continue running when errors are found
try: 
    raise Exception("This is an error")
except Exception as error:
    print(error)

# Creating error handling classes

class DogNotFoundExcpetion(Exception):
    # pass is used in clsses with no methods or fucntions without code inside of them
    pass

try: 
    raise DogNotFoundExcpetion()
except DogNotFoundExcpetion:
    print("Dog not found")


