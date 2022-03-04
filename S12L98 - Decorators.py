
def hello():
    return "Hello!"

hello()
# 'Hello!'

print(hello)
# <function __main__.hello()>

greet = hello

greet()
# 'Hello!'

# Is greet has a pointer(link) to hello or it has it's own copy ?
# We can check that by deleting "hello". If "greet" function leads to an error = it had a Link.

del hello

hello()
# NameError: name 'hello' is not defined

greet()
# 'Hello!'

# ...so it is a separate variable. Not a link.



# = - = - = - = - = - = - = - = - = - = - =
def hey():
    print("Hello hey2() function has been executed!")

    # func in a func:
    def greeting():
        return "\t This is a greeting() func inside hey()!"

    def wellcome():
        return "\t This is wellcome() inside hey()!"

    print(greeting())
    print(wellcome())
    print("End of hey() func!")


hey()

# Hello hey() function has been executed!
# 	 This is a greeting() func inside hey()!
# 	 This is wellcome() inside hey()!
# End of hey() func!


# If I try to get greeting( ) or wellcome( ) directly, I will get an Error.



# = - = - = - = - = - = - = - = - = - = - =
def yo(name="Britney"):
    print("Hello yo() function has been executed!")

    # func in a func:
    def greeting():
        return "\t This is a greeting() func inside yo()!"

    def wellcome():
        return "\t This is wellcome() inside yo()!"

    print("Returning a func()")

    if name == "Britney":
        print("1!")
        return greeting
    else:
        print("2!")
        return wellcome



my_func1 = yo("Tom") #No need for name in this case

# Hello yo() function has been executed!
# Returning a func()
# 2!

my_func1
# <function __main__.yo.<locals>.wellcome()>

print(my_func1())
#       This is wellcome() inside yo()!


# = - = - = - = - = - = - = - = - = - = - =
def cool():
    def super_cool():
        return "I'm very cool"

    return super_cool


some_func = cool()

some_func()
# "I'm very cool"




# = - = - = - = - = - = - = - = - = - = - =
# Passing another func as an argument:

def hello():
    return "Hi, Jose!"


def other(some_define_func):
    print("Other code runs here!")
    print(some_define_func())


other(hello)
# Other code runs here!
# Hi, Jose!



# = - = - = - = - = - = - = - = - = - = - =
# Decorators:

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original func.")

        original_func()

        print("Some extra code, after the original func.")

    return wrap_func



def func_needs_decorator():
    print("I want to be Decorated.")


decorated_func = new_decorator(func_needs_decorator)

decorated_func()
# Some extra code, before the original func.
# I want to be Decorated.
# Some extra code, after the original func.



# = - = - = - = - = - = - = - = - = - = - =
# The w@y:

@new_decorator              #Where to put
def func_needs_decorator(): #What to put
    print("I want to be Decorated.")


func_needs_decorator()
# Some extra code, before the original func.
# I want to be Decorated.
# Some extra code, after the original func.


# Decorators are often used in web-frameworks/Libraries: Django & Flask








