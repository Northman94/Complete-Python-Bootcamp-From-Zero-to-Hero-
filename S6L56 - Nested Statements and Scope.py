
x = 25

def printer():
    x = 50
    return x

print(printer())
# 50

# - - - - - - - - - - - - - - - - - -
# LOCAL

lambda num: num**2
# num is local to a num lambda function.

# - - - - - - - - - - - - - - - - - -
# Enclosing

# GLOBAL
name = 'George'

def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'Betty'
        print('Hello, ' + name)
    hello()

# So name at the top is Global & name in a function - Enclosing
greet()
# Hello, Betty

# - - - - - - - - - - - - - - - - - -
# The only level above GLOBAL is a BUILD IN FUNCTION level.
help(len)
# Help on built-in function len in module builtins:
#
# len(obj, /)
#     Return the number of items in a container.

# - - - - - - - - - - - - - - - - - -
q = 10

def reasignment(q):
    print(f'Global Q is {q}')

    q = 30
    print(f'Q changed Locally = {q}')


reasignment(q)
print(f'But globally it is still {q}')

# Global Q is 10
# Q changed Locally = 30
# But globally it is still 10


# - - - - - - - - - - - - - - - - - -
# To eventually change GLOBAL variable too:
z = 10

def reasignment():
    global z

    print(f'Global Z is {z}')

    z = 'A STRING'  # Global change
    print(f'And now Global Z is {z}')

reasignment()

# Global Z is 10
# And now Global Z is A STRING

