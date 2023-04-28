# FUNCTIONS - use def keyword to signify functions.  Indentation creates blocks of code for functions

def hello(name):
    print(f"Hello {name}")
    # OR print("hello " + name)

hello("Rod")

# creating optional parameters with default value if no other argument is passed
def hi(name="my friend"):
    print("Hi " + name)

hi()

def nameAge(name, age):
    print("Hello " + name + " you are " + str(age) + " years old")

nameAge("Rod", 47)

# returning multiple comma separated values from function
def greetings(name):
    print("Hello " + name + "!")
    return name, "Rod", 47

print(greetings("Sydney"))

# GLOBAL SCOPE - variables declared outside of function
age = 8
def test():
    print(age)

test()

# FUNCTION SCOPE - variables declared inside of functions, not readable outseide of function
def age():
    age = 10
    print(age)

print(age) # not accessible in function scope
age()

# NESTED FUNCTIONS
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("I am happy")



def count():
    count = 0

    def increment():
        nonlocal count # nonlocal calls variable from outside function scope
        count = count + 1
        print(count)

        increment()
count()








