import webbrowser as wb

# Math:
wb.open('https://docs.python.org/3/library/math.html')

# = - = - = - = - = - = - = - = - = - = - = - = -


import math

# Math Library Documentation:
help(math)


# = - = - = - = - = - = - = - = - = - = - = - = -
value1 = 4.35
value2 = 4.67

math.floor(value1) # 4
math.ceil(value2)  # 5

print(round(value1)) # 4
print(round(value2)) # 5


# = - = - = - = - = - = - = - = - = - = - = - = -
to_even = 4.5
to_odd = 5.5

print(round(to_even)) # 4
print(round(to_odd))  # 6


# = - = - = - = - = - = - = - = - = - = - = - =
print(math.pi)
# 3.141592653589793


# = - = - = - = - = - = - = - = - = - = - = - =
from math import pi

print (pi)
# 3.141592653589793

print(math.e)
# 2.718281828459045

# Infinity:
print(math.inf)
# inf

# Not a Number:
print(math.nan)
# nan


# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# Google: Numpy - is a Library for Numerical processing.
# = - = - = - = - = - = - = - = - = - = - = - = - = - =


# Logarithm Base e
print(math.log(math.e))
# 1.0

print(math.log(100,10)) # 10 is a base
# 2.0

# Trigonometric func:
print(math.sin(10)) #Result in Radians
#  -0.5440211108893699

# To Degrees:
print(math.degrees(pi/2))
# 90.0

print(math.radians(180))
# 3.141592653589793


# = - = - = - = - = - = - = - = - = - = - = - = -
# Random Module:

# Random Module allows us to create random numbers. We can even set a seed
# to produce the same random set every time.

# The explanation of how a computer attempts to generate random numbers is beyond
# the scope of this course since it involves higher level mathematics.

# But if you are interested in this topic check out:
# https://en.wikipedia.org/wiki/Pseudorandom_number_generator
# https://en.wikipedia.org/wiki/Random_seed

# Understanding a seed:
# Setting a seed allows us to start from a seeded psuedo-random number generator,
# which means the same random numbers will show up in a series.
# Note, you need the seed to be in the same cell if your using jupyter to guarantee
# the same results each time.

# Getting a same set of random numbers can be important in situations where you will be
# trying different variations of functions and want to compare their performance
# on random values, but want to do it fairly (so you need the same set of random numbers each time).

import random

random.randint(0,5) # Returns random integer in range [a, b], including both end points.
# 5


# = - = - = - = - = - = - = - = - = - = - = - =
# SEED:

# If .seed()  was called before randomizer, same numbers will be printed, each time.

random.seed(42) #101

print(random.randint(0,100)) # 81
print(random.randint(0,100)) # 14
print(random.randint(0,100)) # 3
print(random.randint(0,100)) # 94
print(random.randint(0,100)) # 35
print(random.randint(0,100)) # 31
print(random.randint(0,100)) # 28
print(random.randint(0,100)) # 17
# 81
# 14
# 3
# 94
# 35
# 31
# 28
# 17



# = - = - = - = - = - = - = - = - = - = - = - =
my_list = list(range(0,20))

print(my_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


random.choice(my_list)
# 3



# = - = - = - = - = - = - = - = - = - = - = - =
# Select more that one random Obj from a List:
# = - = - = - = - = - = - = - = - = - = - = - =

# SAMPLE WITH REPLACEMENT (Can Repeat)
random.choices(population = my_list, k = 10)
# [6, 1, 1, 16, 12, 16, 14, 10, 19, 7]


# SAMPLE WITHOUT REPLACEMENT (Don't Repeat)
random.sample(population = my_list, k = 10)
# [17, 9, 11, 6, 2, 0, 10, 3, 4, 1]


my_list2 = list(range(0,20))

print(my_list2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


random.shuffle(my_list2)

print(my_list2)
# [3, 0, 8, 14, 19, 15, 11, 9, 13, 2, 1, 16, 12, 7, 17, 4, 18, 5, 10, 6]




# = - = - = - = - = - = - = - = - = - = - = - =
# Probability:
# = - = - = - = - = - = - = - = - = - = - = - =
random.uniform(a = 0, b = 100)
# 39.56319010606643

random.gauss(mu = 0, sigma = 1)
# 0.9522735598158206



# = - = - = - = - = - = - = - = - = - = - = - =
# If you are using those, read about: NUMBY
# = - = - = - = - = - = - = - = - = - = - = - =