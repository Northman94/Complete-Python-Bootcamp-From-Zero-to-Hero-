
# Encapsulation:

import webbrowser as wb
wb.open('https://www.pythontutorial.net/python-oop/python-private-attributes/#:~:text=Introduction%20to%20encapsulation%20in%20Python&text=Encapsulation%20is%20the%20packing%20of,is%20an%20example%20of%20encapsulation.')


# Inheritance:

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I'm an Animal")

    def eat(self):
        print("Chewing")


my_animal = Animal()
# Animal Created
my_animal.eat()
# Chewing


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)  # Just to trigger base-method
        print("Dog created")

    def who_am_i(self):
        print("I'm a Dog")

    def eat(self):
        print("Eating Dog food")

    def bark(self):
        print("Woof!")

my_dog = Dog()
# Animal Created
# Dog created

my_dog.eat()
# Eating Dog food

my_dog.who_am_i()
# I'm a Dog

my_dog.bark()
# Woof!




# Polymorphism:

# In Python Polimorphism reffers to the way, in which different Obj Classes,
# can share the same methods name, and then this methods can be called from
# the same place. Even though a variety of different Obj-s can be passed-in.


class Doggie():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"



class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"


niko = Doggie("Niko")
felix = Cat("Felix")


print(niko.speak())
# Niko says Woof!
print(felix.speak())
# Felix says Meow!


for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())
# <class '__main__.Doggie'>
# Niko says Woof!

# <class '__main__.Cat'>
# Felix says Meow!




# Getting Obj specific results:
def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
# Felix says Meow!

# Abstract class - never expect an instance of it to be created.
# Designed to only serve as a base class.

class Mammals():
    # Not creating Instance, because it's a base Class
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must Implement this Abstract method.")


class Horse(Mammals):

    def speak(self):
        return self.name + " says Pfff!"


class Bird(Mammals):

    def speak(self):
        return self.name + " says Twitt!"


fido = Horse("Fido")
oro = Bird("Oro")

print(fido.speak())
# Fido says Pfff!
print(oro.speak())
# Oro says Twitt!


# We can have a base class for opening Files. And inherited one for opening PDF,
# Excel-s,MP3 etc. We want them to share the same (open) method name.














