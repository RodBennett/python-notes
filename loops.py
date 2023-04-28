# WHILE LOOPS AND FOR LOOPS

condition = True
while condition == True:
    print("The condition is true")

    # set to false after fir iteration to avoid infinite loop
    condition = False

# WHILE LOOP
count = 0
while count < 10:
    count = count + 1
    print("The condition is true")

print("End loop")

# FOR LOOP
items = [ 1, 2, 3, 4 ]
for item in items:  # this line reads as "for each item in item" ...
    print(item)

# ENUMERATE returns INDEX
items = [ 1, 2, 3, 4 ]
for item in enumerate(items):  # returns (0, 1) (1, 2), etc.
    print(item)

names = ["Rod", "Nancy", "Andria"]
for index, name in enumerate(names):
    print(index, name) # returns 0, 1, etc w/o parenthesis

# RANGE in for loops
for item in range(10):
    print("RANGE", item) # returns 0-9 values

# BREAK AND CONTINUE in Loops
for item in items:
    if item == 2:
        continue # when loop hits 2 it stops at continue line and doesn't execute next line...this is why 2 is not printed, then continues after 2
    print("CONTINUE", item) # returns 1, 3, 4

for item in items:
    if item == 3:
        break # code stops executing 
    print("BREAK", item) # returns 1, 2 ... breaks at 3