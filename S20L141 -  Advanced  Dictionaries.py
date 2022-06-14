
# Dictionary Comprehensions
# Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension for quick creation. It is not as commonly used as List Comprehensions, but the syntax is:

{x:x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


{k:v**2 for k,v in zip(['a','b'], range(2))}
# {'a': 0, 'b': 1}


# One of the reasons it is not as common is the difficulty
# in structuring key names that are not based off the values.


# Iteration over keys, values, and items
# Dictionaries can be iterated over using the keys(), values() and items() methods:

d = {'k1':1,'k2':2}

for k in d.keys():
    print(k)
# k1
# k2


for r in d.values():
    print(r)
# 1
# 2


for item in d.items():
    print(item)
# ('k1', 1)
# ('k2', 2)



# Viewing keys, values and items
# By themselves the keys( ), values( ) and items( ) methods
# return a dictionary view object. This is not a separate list of items.
# Instead, the view is always tied to the original dictionary.

key_view = d.keys()
print(key_view)
# dict_keys(['k1', 'k2'])


d['k3'] = 3
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

print(key_view)
# dict_keys(['k1', 'k2', 'k3'])































