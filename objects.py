# OBJECTS - 
# @descr - everything in Python is an object (all data structures and types), properties and methods
# @syntax - .(dot) syntax

age = 8
print(age.bit_length()) # number of bits necessary to represent nmber in binary notation


items = [ 1, 2 ]
items.append(3)
print(items)
items.pop()
print(items)

# id gives memory address where data is stored
print(id(items))