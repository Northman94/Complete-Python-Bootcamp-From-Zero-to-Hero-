
my_list = [1, 2, 3]

my_list = ["String", 100, 20.5]

len(my_list)
# 3

list1 = ["One", "Two", "Three"]
list1[0]
# 'One'


list1[1:]
# ['Two', 'Three']


# Concatination:

list1
# ['One', 'Two', 'Three']

list2 = ["Four", "Five"]


list1 + list2
# ['One', 'Two', 'Three', 'Four', 'Five']
# Line above is not saving any result. Need to assign a variable for that.


# Strings are immutable. But Lists are changeable.
list4 = ["One", "Two", "Three"]
list4[0] = "ONE ALL CAPS"
list4
# ['ONE ALL CAPS', 'Two', 'Three']


# Adding New element to a List:
list4.append("Four")
list4
# ['ONE ALL CAPS', 'Two', 'Three', 'Four']


# Deletes & returns the last Obj. Can be stored in a variable:
list4.pop()
# 'Four'

list4
# ['ONE ALL CAPS', 'Two', 'Three']


# Or add an index:
list4.pop(0)
# 'ONE ALL CAPS'

list4
# ['Two', 'Three']

list4.pop(-1)
# 'Three'


# List Sorting:
list5 = ["A", "E", "Z", "B", "C"]
list6 = [4, 8, 2, 0, -3]
# Returns nothing. So nothing to store in a variable.

list5.sort()
list6.sort()
list5
# ['A', 'B', 'C', 'E', 'Z']
list6
# [-3, 0, 2, 4, 8]


# Newbies mistakes:

sortedList = list5.sort()
sortedList
# Because sorting returns nothing, so there is nothing to assign in a variable.

type(sortedList)
# NoneType

# None is a return value of a function/methods that doesn't really return anything.
# But if you want to assing a sorted List to a variable:

list6.sort()
sortedList = list6

sortedList
# [-3, 0, 2, 4, 8]


# Reverse:
sortedList.reverse()
sortedList
# [8, 4, 2, 0, -3]


