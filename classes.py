# CLASSES
# @desc --- classes instantiate objects / objects are intances of classes / class is the type of an object

class Dog:
    def bark(self):
        print("woof")

roger = Dog()

print("TYPE", type(roger))

class Canine:
    # define properties of class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Hello canine")

    # create methods of class
    def bark(self):
        print("Woof!")

rodney = Canine("Rod", 6)
print(rodney.name, rodney.age)
rodney.bark()

# INHERITANCE
class Colors:
    def bright(self):
        print("Bright color")

class Red(Colors):
    def __init__(self, brightness, dullness):
        self.brightness = brightness
        self.dullness = dullness

    def beautiful(self):
        print("Red")

color = Red("nice", "pretty")
print(color.dullness)
color.bright()
        
