# TUPLES DATA STRUCTURE - 
# @ descr: immutable groups of objects
# @ syntax: parentheses

names = ("Rod", "Syd", "Helen")

names[0]
names.index("Rod")

print(names[0]) # returns value of specified index
print(names.index("Rod")) # returns index number of value

print("Syd" in names) # returns boolean

print(sorted(names))

# can concat tuples into new tuple, but cannot modify original tuple:
newTuple = names + ("John", "Paul", "Steve")
print(newTuple)

