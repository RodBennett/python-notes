# DICTIONARIES ARE KEY/VALUE OBJECTS IN PYTHON - 
# @desc: KEY VALUE PAIRS, JSON
# @syntax: curly braces

dog = { "name": "Xavier", "age": 34, "color": "purple" }
print(dog["name"])

# can use get method to select keys
print(dog.get("name"))
print(dog.get("age"))

# can set set default values in dictionary using get method as well:
print(dog.get("color", "yellow"))

# pop method removes specified key:
dog.pop("name")
print(dog) # returns { "age": 34 }

# popitem method removes last key value pair
dog.popitem()
print(dog) # returns empty object (name already popped in previous pop method)
 
# use in method to check if key exists in object:
print("age" in dog) # returns True
print(dog)

# can check for list of keys: (lists are essentially arrays in JS)
print(list(dog.keys()))
print(dog.keys())

# can check for list of values:
print(list(dog.values()))
print(dog.values())

# can get all items of list in dictionary (keys and values)
print(list(dog.items()))

# can get legth of lists:
print(len(dog))

# add new value pair to list:
dog["favorite food"] = "meat" 
print(dog)
print(len(dog))

# delete item from a list via key:
del dog["age"]
print(dog)

# copy a dictionary
dogCopy = dog.copy()
print(dogCopy)
