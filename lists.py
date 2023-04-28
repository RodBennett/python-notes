# arrays are called lists in Python
# @syntax: square brackets

# CHECK IF VALUE IS IN LIST: in
dogs = ["Roger", "Sid", 1, True, "John", "Quincy"]

# can reassign specific values in list via index
dogs[2] = "Rod"
print("Roger" in dogs)
print("Rod" in dogs)
print(dogs[1])
print(dogs)

# EXTRACT PART OF A LIST
print(dogs[2:5])

# APPEND NEW VALUE TO LIST
dogs.append("Jimmy") # append only takes one argument
print(len(dogs))
dogs.extend(["Judah", 4, True, "Bennett"]) # extend can take multiple arguments
dogs += ["Drake", True] # += operator does same thing as extend
dogs.remove("Quincy")
dogs.pop() # removes last item from list

# INSERT NEW ITEM INTO LIST AT SPECIFIED POSITION
dogs.insert(1, "Justin") # only takes one argument
dogs[3:3] = ["Kevin", "Jenny", "Jonny"] # inserts multiple items into list via slice method

# SORTNG LISTS

people = ["Ringo", "paul", "John"]

# can use slice [:] method to preserve original list  
peoplecopy = people[:]
people.sort()
# sort by lower or uppercse letters
people.sort(key=str.lower)

# this method preserves original list as well
print(sorted(people, key=str.lower))
print(people)
print(peoplecopy)