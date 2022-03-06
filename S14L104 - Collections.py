
# COLLECTIONS:

# 1) Counter Dictionary
# 2) Default Dictionary
# 3) Named Tuple


# Counter Dictionary of unique Obj-s:
# Counter is a Dictionary a sub-class.

from collections import Counter

my_list = [1,1,1,1,1,7,7,7,"a","a","a","a"]

Counter(my_list)
# Counter({1: 5, 7: 3, 'a': 4})



# = - = - = - = - = - = - = - = - =
# Same with strings:

letters = 'ababbablee'

Counter(letters)
# Counter({'a': 3, 'b': 4, 'l': 1, 'e': 2})

c = Counter(letters)
print(c)
# Counter({'b': 4, 'a': 3, 'e': 2, 'l': 1})

c.most_common()
# [('b', 4), ('a', 3), ('e', 2), ('l', 1)]

list(c)
# ['a', 'b', 'l', 'e']



# = - = - = - = - = - = - = - = - =
# Split by word:

sentence = "Hey hello You & I I & You"

Counter(sentence.lower().split())
# Counter({'hey': 1, 'hello': 1, 'you': 2, '&': 2, 'i': 2})



# = - = - = - = - = - = - = - = - =
# Common patterns when using the Counter( ) object:

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts



# = - = - = - = - = - = - = - = - =
# Default Dictionary:

# Default Dictionary returns some default value when reffering to a wrong Key.

from collections import defaultdict

d = {'a':10}

d
# {'a': 10}

d = defaultdict(lambda: 0)

d['correct'] = 100

d['correct']
# 100

d['WRONG KEY!']
# 0

d
# defaultdict(<function __main__.<lambda>()>, {'correct': 100, 'WRONG KEY!': 0})



# = - = - = - = - = - = - = - = - =
# Named Tuple:

my_tuple = (10,20,30)

my_tuple[0]
# 10

from collections import namedtuple

Dog = namedtuple("Dog",['name','age','breed'])

sammy = Dog(name='Thor',age=5,breed='Husky')

type(sammy)
# __main__.Dog

sammy
# Dog(name='Thor', age=5, breed='Husky')

print(sammy.name)
print(sammy.age)
print(sammy.breed)
# Thor
# 5
# Husky


sammy[0]
# Thor

