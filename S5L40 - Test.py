

# Use for, .split(), and if to create a Statement
# that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

iList = st.split()
print(iList)

# ['Print', 'only', 'the', 'words', 'that',
# 'start', 'with', 's', 'in', 'this', 'sentence']

# - - - - - - - - - - - - - - - - - - - - - - - -
iList2 = []

for word in iList:
    if word[0] == 's':
       print(word)

# start
# s
# sentence


# Better Solution:
st0 = 'Print only the words that start with s in this sentence'

for w1 in st0.split():
    if w1[0].lower() == 's':
        print(w1)

# - - - - - - - - - - - - - - - - - - - - - - - - -

# Use range( ) to print all the even numbers from 0 to 10.

iList3 = [numb for numb in range(0,11) if numb % 2 == 0]

print(iList3)
# [0, 2, 4, 6, 8, 10]

#Or another Solution:

for n1 in range (0,11,2):
    print(n1)

# - - - - - - - - - - - - - - - - - - - - - - - - -
# Use a List Comprehension to create a list of all numbers
# between 1 and 50 that are evenly divisible by 3

iList4 = [evenNumb for evenNumb in range(1,51) if evenNumb % 3 == 0]

print(iList4)

# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
# - - - - - - - - - - - - - - - - - - - - - - - - -

# Go through the string below and if the length
# of a word is even print "even!"

strng = 'Print every word in this sentence that has an even number of letters'

iList5 = strng.split()

print(f"{iList5} \n")

for word in iList5:         # Better to use>>>  for word in strng.split():
    if len(word) % 2 == 0:
        print(word + " - is even")
"""
['Print', 'every', 'word', 'in', 'this', 'sentence', 'that', 'has', 'an', 'even', 'number', 'of', 'letters'] 

word - is even
in - is even
this - is even
sentence - is even
that - is even
an - is even
even - is even
number - is even
of - is even
"""


# Write a program that prints the integers from 1 to 100. But
# for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

iList6 = list(range(1, 101))

for evr_elmnt in iList6:      # Better>>>  for evr_elmnt in range(1,101):
    if evr_elmnt % 3 == 0 and evr_elmnt % 5 == 0:
        print("FizzBuzz")
    elif evr_elmnt % 3 == 0:
        print("Fizz")
    elif evr_elmnt % 5 == 0:
        print("Buzz")
    else:
        print(evr_elmnt)

# - - - - - - - - - - - - - - - - - - - - - -

# Use List Comprehension to create a list of the
# first letters of every word in the string below:

str8 = 'Create a list of the first letters of every word in this string'

iList7 = str8.split()
print(f"{iList7} \n")

#- - - - - - - - - - - - - - - - - - - - -
iList8 = []

for u in iList7:
    iList8.append(u[0])

print(f"{iList8} \n")

#- - - - - - - - - - - - - - - - - - - - -
# The way of List Comprohension:
iList9 = [emt[0] for emt in str8.split()]

print(f"{iList9} \n")


















