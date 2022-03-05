
# Generator functions allow us to write a function that can send back
# a value and then later resume to pick up where it left off.

# Allowing us to generate a sequence of values over time.
# The main difference in syntax will be the use of a "yield" statement.

# Generator functions will automatically suspend and resume their
# execution and state around the last point of value generation.

# The advantage is that instead of having to compute an entire series of values
# up front, the generator computes one value, waits until the next value is called for.


# Transforming generator to a List:
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list(range(4)):
    print(i)
# 0
# 1
# 2
# 3

for z in range(0,4):
    print(z)
# 0
# 1
# 2
# 3

# = - = - = - = - = - = - = - = - = - =
def create_cubes(n):
    result = []

    for x in range(n):
        result.append(x ** 3)

    return result


create_cubes(10)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# = - = - = - = - = - = - = - = - = - =
for n in create_cubes(5):
    print(n)
# 0
# 1
# 8
# 27
# 64


# = - = - = - = - = - = - = - = - = - =
# YIELD:
# Generators are more memory-efficient. No List in memory.

def create_cubes2(n):
    for x in range(n):
        yield x ** 3


create_cubes2(5)
# <generator object create_cubes2 at memory cell №123>

for n in create_cubes2(5): #Generator
    print(n)
# 0
# 1
# 8
# 27
# 64

list(create_cubes2(5))
# [0, 1, 8, 27, 64]


# = - = - = - = - = - = - = - = - = - =
# Fibonacci sequence:

def fibonacci_sequence(p):
    a = 0
    b = 1

    for y in range(p):
        yield a

        a, b = b, a + b


for u in fibonacci_sequence(10):
    print(u)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


# = - = - = - = - = - = - = - = - = - =
def next_gen():
    for t in range(3):
        yield t

gen = next_gen()

gen
# <generator object next_gen at 0x7f858a18b510>

print(next(gen))
# 0
print(next(gen))
# 1
print(next(gen))
# 2


# = - = - = - = - = - = - = - = - = - =
# Iter:

gr = "hello"

for w in gr:
    print(w)
# h
# e
# l
# l
# o

gr_iter = iter(gr) #turning into iterator

# now we can use next()

print(next(gr_iter))
# h
print(next(gr_iter))
# e


# = - = - = - = - = - = - = - = - = - =
# GENERATOR  COPREHENSION:
my_list = [1,2,3,4,5]

generator_coprehension = (item for item in my_list if item > 3)

for item in generator_coprehension:
    print(item)
# 4
# 5


# import webbrowser as wbo

# wbo.open(https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html)

