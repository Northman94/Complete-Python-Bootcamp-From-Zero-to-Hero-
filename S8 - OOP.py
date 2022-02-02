
# S8L69 - OOP - Attributes & Class Keywords

class Dog():
    # constructor:
    def __init__(self,_breed,_name,_spots):
    # By Convention all 3 should be same: breed
        self.breed = _breed
        self.name = _name
        self.spots = _spots

# instance of Sample()
my_dog = Dog(_breed = "Huskie",_name = "Joy",_spots = True)


type(my_dog)
# __main__.Dog


# Attributes - called on Obj-s:

my_dog.breed
# 'Huskie'

my_dog.name
# 'Joy'

my_dog.spots
# True


# S8L70 - OOP - Class Obj Attributes & Methods

# Sometimes we need an attribute that will be applied
# to all Class instances = CLASS OBJ ATTRIBUTE
# No need to use "self" - word with it.
# CLASS OBJ ATTRIBUTE is used out of Constructor.

class Dog():
    # Class Obj Attribute:
    # same for all Class Instances
    species = "mammal"

    # constructor:
    def __init__(self, _breed, _name, ):
        # By Convention all 3 should be the same: breed
        self.breed = _breed
        self.name = _name

    # method
    def bark(self, age):
        print("Woof! - said {}. Age:{}".format(self.name, age))
        # self is not used with {age} - it's provided by certain instance method.


# instance of Sample()
my_dog1 = Dog("Lab","Hope")
my_dog2 = Dog("Pug","Ginger")

my_dog.species
# 'mammal'

my_dog1.bark(3)
# Woof! - said Hope. Age:3

my_dog2.bark(1)
# Woof! - said Ginger. Age:1



# - = - = - = - = - = - = - = - = - = - = - =

class Circle():
    # Class Obj Attribute:
    pi = 3.14

    # We can define default parameter R=1
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi  # or Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


# create an instance
my_circle = Circle(30)

print(my_circle.radius)
print(my_circle.pi)
# 30
# 3.14

my_circle.get_circumference()
# 188.4
