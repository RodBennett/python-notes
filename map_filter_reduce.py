# MAP

nums = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, nums)

# maps can take lambda functions as args:
result = map(lambda a : a * 2, nums)
print(list(result))

# FILTER
def isEven(n):
    return n % 2 == 0

result = filter(isEven, nums)

# OR...
result = filter(lambda n : n % 2 == 0, nums)

print(list(result))

# REDUCE
expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]

from functools import reduce

sum = 0
for expense in expenses:
    sum += expense[1] # expense[1] refers to value in each tuple

# OR
sum = reduce(lambda a, b : a[1] + b[1], expenses) # read as initial value plus current value, iterable (ie. expenses)
print(sum)



