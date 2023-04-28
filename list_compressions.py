# LIST COMPRESSIONS
# @desc - create lists in a very concise way, can be used instead of maps amd loops

numbers = [ 1, 2, 3, 4, 5 ]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# COMPRESSION IS SAME AS LOOP:
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)



