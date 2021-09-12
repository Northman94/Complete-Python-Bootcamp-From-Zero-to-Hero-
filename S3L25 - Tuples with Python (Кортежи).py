
tup1 = (1,2,3)

myList1 = [1,2,3]

type(tup1)
# tuple

type(myList1)
# list

len(tup1)
# 3

tup1
# (1, 2, 3)


# Typles as Lists can contain different type of Objects.

tup2 = ("One", 2)

# Indexing & Slicing can be used too.

tup2[0]
# 'One'

tup2[-1]
# 2


# Methods:

tup3 = ("A", "B", "A")

tup3.count("A")
# 2

# Will show first appearance index if there is choice:

tup3.index("A")
# 0

tup3.index("B")
# 1


tup4 = ("Z", "Q", "S")

myList4 = [1, 2, 3]

myList4[0] = "NEW1"

myList4
# ['NEW1', 2, 3]

# Same with Typles will cause an Error: Tuple Objs doesn't support item assignment.

# The Benefit of a Typle is: passing in an Obj that shouldn't be changed. (Data integrity)
