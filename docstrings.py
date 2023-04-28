# DOCSTRING
# @desc: documentation for code to help remember what your code does, like comments
# @syntax: triple quotes """ """

"""Incement module counts numbers"""

def increment(n):
    """Increment a number"""
    return n + 1

num = increment(3)
print(num)

# docstring can be caled with global hellp function
print(help(num))

class Dog:
    """Class represents a dog"""
    def __init__(self, name, age):
        """ Initialize a new dog """
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("Woof!")

print(help(Dog))