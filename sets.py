 # SET DATA STRUCTURE - 
# @desc: mutable, not ordered
# @syntax: curly braces, no key/value pairs

set1 = { "Doug", "Syd", "Rod", "Luna" } 
set2 = { "Doug", "Luna", "Victoria" }

# find intersecting values in different sets:
intersect = set1 & set2
print(intersect)

# union of 2 sets - produces set only of unique values between sets, no overlaps
mod = set1 | set2
print(mod) # returns Doug, Syd, Luna (not Doug twice)

# compare sets (boolean): Does set1 have everything that set2 contains?
mod1 = set1 > set2
print(mod1)
mod2 = set1 < set2
print(mod2)

# subtract values of set1 from set2
mod = set1 - set2
print(mod)

# check lists:
print(list(set1))


