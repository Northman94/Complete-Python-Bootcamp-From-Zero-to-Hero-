
list1 = [1,2,3]

# .append( )
# Adds an element to the end of a list:

list1.append(4)
print(list1)
# [1, 2, 3, 4]

# .count( )
# Takes in an element and returns the number of times it occurs in a List:

list1.count(10)
# 0

list1.count(4)
# 1


# .append( )
# Ads a whole object at the end:

x = [1, 2, 3]
x.append([4, 5])
print(x)
# [1, 2, 3, [4, 5]]


# .extend( )
# extend: extends list by appending elements from the iterable:

x = [1, 2, 3]
x.extend([4, 5])
print(x)
# [1, 2, 3, 4, 5]

# Note how extend() appends each element from the passed-in list.
# That is the key difference.



# index()
# will return the index of whatever element is placed as an argument.
# Note: If the the element is not in the list an Error is raised.

list1.index(2)
# 1

# list1.index(12)
# Will cause an Error




# insert()
# takes in two arguments: insert(index,object)
# This method places the object at the index supplied:

list2 = [1,2,3,4]

# Place a letter at the index 2
list2.insert(2,'inserted')

print(list2)
# [1, 2, 'inserted', 3, 4]


# pop()
# allows us to "pop" off the last element of a List.
# However, by passing an index position you can remove and return a specific element.

ele = list2.pop(1)  # pop the second element

print(list2)
# [1, 'inserted', 3, 4]

print(ele) #returns popped iteam
# 2


# remove()
# method removes the first occurrence of a value:

l1 = [1, 'inserted', 2,3]
l1.remove('inserted')

print(l1)
# [1,2,3]


l2 = [1,2,3,4,3]
l2.remove(3)

print(l2)
# [1, 2, 4, 3]



# .reverse( )
# It affects your list permanently.

l2.reverse()
print(l2)
# [3, 4, 2, 1]


# .sort( )
# Will sort your list in place:

list3 = [1,3,2,4]
list3.sort()

print(list3)
# [1,2,3,4]

# The sort() method takes an optional argument for reverse sorting.
# Note this is different than simply reversing the order of items.

list3.sort(reverse=True)

print(list3)
# [1, 2, 3, 4]


# = - = - = - = - = - = - = - = - = - = - =

# Be Careful With Assignment!
# A common programming mistake is to assume you can assign a modified list to a new variable.
# While this typically works with immutable objects like strings and tuples:


# Strings:

x = 'hello world'
y = x.upper()

print(y)
# HELLO WORLD

# Will NOT work the same way with Lists:

x2 = [1,2,3]
y2 = x2.append(4)

print(y2)
# None


# What happened? In this case, since List methods like append()
# affect the list in-place, the operation returns a None value.
# This is what was passed to y2. In order to retain x2 you would have
# to assign a copy of x2 to y2, and then modify y2:

# The Right Way:

x3 = [1,2,3]
y3 = x3.copy()
y3.append(4)

print(x3)
# [1, 2, 3]

print(y3)
# [1, 2, 3, 4]



