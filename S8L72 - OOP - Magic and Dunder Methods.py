
import webbrowser as wb
wb.open('https://habr.com/ru/post/186608/')


# Examples of ordinary Methods usage:
my_list = [1,2,3]

len(my_list)
# 3

class Sample():
    pass

my_sample = Sample()

print(my_sample)
# <__main__.Sample object at "memory address">

print(id(my_sample))
# "memory address"

print(my_list)
# [1,2,3]

# - = - = - = - = - = - = - = - = -

# How do I use buid-in Python functions like
# len() or print(), with my own user-defined Obj-s ?

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python OOP','Jose',200)

print(b) # What is a string representation of "b"
# <__main__.Book object at "memory address">

str(b)
# '<__main__.Book object at "memory address">'



# - = - = - = - = - = - = - = - = -
class Book2():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}."
        # f-string literal formatting

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Obj has beed Deleted")



b2 = Book2('High Tech','Martha',100)

print(b2)
str(b2)
# High Tech by Martha.
# 'High Tech by Martha.'

len(b2)
# 100

# - = - = - = - = - = - = - = - = -
# Delete b2 from PC memory.
# If we call it - an Error will occur
# b2 is not Defined.

del b2
# Obj has been Deleted
