
# Write a function that computes the
# volume of a sphere given its radius.

def vol(rad):
    return (4/3)*(3.14)*(rad**3)

vol(2)
# 33.49333333333333

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a function that checks whether a number is
# in a given range (inclusive of high and low)

def ran_check(num,low,high):
    return num in range(low, high + 1)

ran_check(5,2,7)
# True

# OR:

def ran_bool(num,low,high):
    return num > low and num < high

ran_bool(1,3,10)
# False

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.

def up_low(st1):
    upper = 0
    lower = 0

    for elmt in st1:
        if elmt.isupper():
            upper += 1
        elif elmt.islower():
            lower += 1
        else:
            pass

    print(f"№ of Upper case characters : {upper}")
    print(f"№ of Lower case Characters : {lower}")


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
# № of Upper case characters : 4
# № of Lower case Characters : 33

# - = - = - = - = - = - = - = - = - = - = - = - = -
# With DICTIONARY:

def up_low2(st2):
    d = {'UPPER': 0, 'LOWER': 0}

    for elmt in st2:
        if elmt.isupper():
            d['UPPER'] += 1
        elif elmt.islower():
            d['LOWER'] += 1
        else:
            pass

    print(f"№ of Upper case characters : {d['UPPER']}")
    print(f"№ of Lower case Characters : {d['LOWER']}")


up_low2('Hello Mr. Rogers, how are you this fine Tuesday?')

# - = - = - = - = - = - = - = - = - = - = - = - = -
# With Lambdas:

def up_low3(st3):
    upperCases = len(list(filter(lambda uppers: uppers.isupper(), st3)))
    lowerCases = len(list(filter(lambda uppers: uppers.islower(), st3)))

    print(f"№ of Upper case characters : {upperCases}")
    print(f"\n№ of Lower case Characters : {lowerCases}")


up_low3('Hello Mr. Rogers, how are you this fine Tuesday?')


# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    print(list(set(lst)))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
# [1, 2, 3, 4, 5]

# - = - = - = - = - = - = - = - = - = - = - = - = -
def unique_list2(ulst):
    unique = []

    for numb in ulst:
        if numb not in unique:
            unique.append(numb)
    return unique


unique_list2([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
# [1, 2, 3, 4, 5]

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(nlist):
    mult = 1

    for n in nlist:
        mult *= n

    return mult


multiply([1, 2, 3, -4])
# -24

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a Python function that checks whether
# a word or phrase is palindrome or not.

def palindrome(pal):
    old = pal.replace(" ", "")

    new = old[::-1]

    return new == old


palindrome('nurses run')
# True

# - = - = - = - = - = - = - = - = - = - = - = - = -
def palindrome(pal):
    pal = pal.replace(" ", "")

    return pal == pal[::-1]


palindrome('nurses run')
# True

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

import string

def is_pangram(str1, alphabet=string.ascii_lowercase):
    newList = []

    no_spaces = str1.replace(" ", "")

    for xz in no_spaces.lower():
        newList.append(xz)

    set_list = sorted(set(newList))

    merged_list = "".join(set_list)

    return merged_list == alphabet

# Paste a Str
# Remove Spaces
# Break string to a List + lower()
# Sort by Alphabet.

# Set()
# Shape List like Alphabet
# Compare with alphabet

is_pangram("The quick brown fox jumps over the lazy dog")
# True

# - = - = - = - = - = - = - = - = - = - = - = - = -
# Teacher:

import string


def is_pangram2(str2, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)

    str2 = str2.replace(" ", "")

    str2 = str2.lower()

    str2 = set(str2)

    return str2 == alphaset


is_pangram2("The quick brown fox jumps over the lazy dog")
# True
