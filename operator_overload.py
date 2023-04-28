# OPERATOR OVERLOAD

# @desc - compare 2 objects from the same class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # __gt__ means greater than
    def __gt__(self, other):
        return True if self.age > other.age else False

dog1 = Dog("Rod", 8)
dog2 = Dog("Beau", 6)

print(dog1 > dog2)