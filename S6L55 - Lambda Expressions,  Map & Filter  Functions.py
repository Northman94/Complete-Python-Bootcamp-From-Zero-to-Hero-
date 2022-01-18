
# map(function, *iterables) -> map object

# map => makes an iterator that apply the supplied function to each element
# of the iterable and can return a list of results for each element.
# Stops when the shortest iterable is exhausted.

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)
# 1
# 4
# 9
# 16
# 25


list(map(square,my_nums))
# [1, 4, 9, 16, 25]

# - - - - - - - - - - - - - - - -

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]

list(map(splicer, names))
# ['EVEN', 'E', 'S']

# - - - - - - - - - - - - - - - -

# filter ->  filters the original iterable
# and retents the items that returns True.

def check_even(n):
    return n % 2 == 0

my_numrs = [1,2,3,4,5,6]

list(filter(check_even, my_numrs))
# [2, 4, 6]

for q in filter(check_even, my_numrs):
    print(q)
# 2
# 4
# 6

# - - - - - - - - - - - - - - - -
# Lambda Expressions:

# Will turn this into Lambda:
def square2(num2):
    result = num2**2
    return result

square2(9)
# 81


# Simplify:
def square3(num3):
    return num3**2

square3(2)
# 4


# Because it is called Anonomous func & we will
# only use it once, no need to use def or name it.

square = lambda num4: num4**2

square(6)
# 36

# - - - - - - - - - - - - - - - -
# Lambda in map function:
numList = [1,2,3,4,5,6]

list(map(lambda num: num**3, numList))
# [1, 8, 27, 64, 125, 216]

# - - - - - - - - - - - - - - - -
# Lambda in filter function:
numList2 = [1,2,3,4,5,6]

list(filter(lambda n: n % 2 == 0, numList2))
# [2, 4, 6]

# - - - - - - - - - - - - - - - -
names2 = ["Eve","Jorge","Sam"]

list(map(lambda p: p[0], names2))
# ['E', 'J', 'S']

# - - - - - - - - - - - - - - - -

names3 = ["Eve","Jorge","Sam"]

list(map(lambda e: e[::-1], names3))
# ['evE', 'egroJ', 'maS']

# - - - - - - - - - - - - - - - -
names4 = ["Eve","Jorge","Sam"]

list(map(lambda z: z , names4[::-1]))
# ['Sam', 'Jorge', 'Eve']

