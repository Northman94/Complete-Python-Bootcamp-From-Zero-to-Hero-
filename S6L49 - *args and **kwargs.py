
#  *args  &  **kwargs  ( are Functional Parameters )
#  *kwargs = key-word arguments

def myfunc(a, b, c=0):
    # returns 5% of the sum of a & b

    return sum((a, b, c)) * 0.05

myfunc(40,60)
# 5.0



# We can avoid the ammount limit of paremeters by:
#  *args = will be treated as a tuple of parameters

def myfunc2(*args):
    return sum(args) * 0.05

# With such approach, any ammount of arguments can be passed in. Turned into tuple.
myfunc2(7,10,15,8)
# 2.0


def myfunc3(*args):
    for item in args:
        print(item)

myfunc3(40,60,100,34)
# 40
# 60
# 100
# 34


# A Dictionary by *kwargs:
def myfunc4(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}.".format(kwargs["fruit"]))

        print("Dictionary:")
        print(kwargs)
    else:
        print("I did not find any fruit here.")


myfunc4(fruit = "Apple", veggie = "Lettuce")
# My fruit of choice is Apple.
# Dictionary:
# {'fruit': 'Apple', 'veggie': 'Lettuce'}



def myfunc5(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs["food"]))

myfunc5(10,20,30,fruit = "oranges",animal = "Dogs",food = "Lasagnas")
# I would like 10 Lasagnas

# A combination of both:

def myFunc6(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}.".format(args[2], kwargs["food"]))


myFunc6(10,20,30, animal = "dogs", metal = "gold", food = "Oranges")

# (10, 20, 30)
# {'animal': 'dogs', 'metal': 'gold', 'food': 'Oranges'}
# I would like 30 Oranges.


# Function taking an arbitrary number of arguments and returns the sum of those arguments:
def myfunc7(*args):
    return sum(args)

myfunc7(10,20)
# 30


# Function takes an arbitrary numb of args & returns a List containing only those args that are even:

numbList = []

def myfunc8(*args):
    for item in args:
        if item % 2 == 0:
            numbList.append(item)
    return numbList

myfunc8(1,2,3,4,5,6)
# [2, 4, 6]


# A Function that takes in a string & returns a string where
# every even letter is Uppercase & every odd letter is Lowercase.

def myFunc9(a):
    charLits1 = []
    charLits2 = []

    for char in a:
        charLits1.append(char)
    print(charLits1)

    print("\n NEXT \n")

    numb = 0

    for elmnt in charLits1:

        if numb % 2 == 0:  # even
            charLits2 += elmnt.upper()
        else:
            charLits2 += elmnt.lower()
        numb += 1
    print(charLits2)

    charLits3 = "".join(charLits2)

    print(charLits3)


myFunc9("adbcdefg")

# ['a', 'd', 'b', 'c', 'd', 'e', 'f', 'g']
#
#  NEXT
#
# ['A', 'd', 'B', 'c', 'D', 'e', 'F', 'g']
# AdBcDeFg


# OR A BETTER WAY

def myFunc10(word):
    out = []

    for i in range(len(word)):
        if i % 2 == 0:
            out.append(word[i].lower())
        else:
            out.append(word[i].upper())
    print(''.join(out))


myFunc10("asdfbnm")












