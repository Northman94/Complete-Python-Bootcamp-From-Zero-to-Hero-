
# Advanced Numbers
# Problem 1: Convert 1024 to binary and hexadecimal representation

bin(1042)
# '0b10000010010'

hex(1042)
# '0x412'


# Problem 2: Round 5.23222 to two decimal places
a = round(5.23222,2)

print(a)
# 5.23



# Advanced Strings
# Problem 3: Check if every letter in the string s is lower case

s = 'hello how are you Mary, are you feeling okay?'

s.islower()
# False


# Problem 4: How many times does the letter 'w' show up in the string below?

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count('w')
# 12



# Advanced Sets
# Problem 5: Find the elements in set1 that are not in set2:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)
# {2}

set2.difference(set1)
# {7}


# Problem 6: Find all elements that are in either set:

set1.union(set2)
# {1, 2, 3, 5, 6, 7, 8}



# Advanced Dictionaries
# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
# using a dictionary comprehension.

{x:x**3 for x in range(5)}
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}



# Advanced Lists
# Problem 8: Reverse the list below:

list1 = [1,2,3,4]

list1[::-1]
# [4, 3, 2, 1]

# OR:

z = list1.copy()
z.reverse()

print(z)
# [4, 3, 2, 1]




# Problem 9: Sort the list below:

list2 = [3,4,2,5,1]
list2.sort()

print(list2)
# [1, 2, 3, 4, 5]

