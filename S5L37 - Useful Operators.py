
myList = [1,2,3]

# We can iterate through it:

# for num in range()


# Pressing Shift + Tab in Jupiter, will open window with parameters

# Init signature: range(self, /, *args, **kwargs)
# Docstring:
# range(stop) -> range object
# range(start, stop[, step]) -> range object


# Or:

for num in range(5):
    print(num)
# 0
# 1
# 2
# 3
# 4


for num in range (0,10,2):
    print(num)
# 0
# 2
# 4
# 6
# 8

for num in range (0,11,2):
    print(num)
# 0
# 2
# 4
# 6
# 8
# 10


# Generators:

range(0,11,2)
# range(0,11,2)

# We can cast it to a List:

list(range(0,11,2))
# [0, 2, 4, 6, 8, 10]

# Generators are special type of function that will generate info instead of saving it to the memory

# ENUMERATE:

intex_count = 0

for letter in "abcde":
    print("At index {} the letter is {}".format(intex_count, letter))
    intex_count += 1

# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

ind_count = 0
word = "abcde"

for ltr in word:
    print(word[ind_count])
    ind_count += 1

# a
# b
# c
# d
# e

word = "abcde"

for i in enumerate(word):
    print(i)

# Will get tuple:
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')

# Tuple unpacking:

wrd = "abc"

for index, letter in enumerate(wrd):
    print(index)
    print(letter)
    print("\n")
# 0
# a

# 1
# b

# 2
# c

# Zip-function: (opposite of an enumerate)

list1 = [1,2,3]
list2 = ["a","b","c"]

zip(list1,list2)

# <zip at 0x7fef41e845c0>
# This means that we have a ZIP generator waiting for us at this memory location.

# But we can get a list of Tuples by iteration:

for  q in zip(list1,list2):
    print(q)
# (1, 'a')
# (2, 'b')
# (3, 'c')


list3 = [1,2,3,4,5]
list4 = ["a","b","c"]

for t in zip(list3,list4):
    print(t)
# (1, 'a')
# (2, 'b')
# (3, 'c')

# Notice that we get the same result, due to Tuple pairs nature ^^^


list(zip(list3,list4))
# [(1, 'a'), (2, 'b'), (3, 'c')]


listA = [1,2,3,4,5]
listB = ["a","b","c"]
listC = [100,200,300]

for a,b,c in zip(listA,listB,listC):
    print(b)
# a
# b
# c


# "IN" Key-Word:

2 in [1,2,3]
# True

"x" in ["x", "y", "z"]
# True

"o" in "a world"
# True

"myKey" in {"myKey":234}
# True

r = {"mKey":123}
"mKey" in r.keys()
# True

d = {"mKey":123}
123 in d.values()
# True


# min / max:

nList = [10,30,20,40]

min(nList)
# 10

max(nList)
# 40



# Random:

from random import shuffle

bList = [1,2,3,4,5,6,7,8,9]

shuffle(bList)

bList
# [2, 5, 9, 6, 8, 7, 4, 1, 3]


# Shuffle does not return anything, so it can't be assigned to a Variable.

type(shuffle)
# method

randList = shuffle(bList)
type(randList)
# NoneType


# Grab a random int:

from random import randint
randint(0, 100)
# 69


myNum = randint(0, 100)

myNum
# 99


# Getting User Input:

result = input("Enter your Age:")

result
# e.g.  30

# Input always accepts everything & convert it to a string.

type(result)
# str

float(result)
# 30.0

int(result)
# 30

# Can implicitly convert:

result2e = int(input("Enter your Number: "))

type(result2e)
# int

