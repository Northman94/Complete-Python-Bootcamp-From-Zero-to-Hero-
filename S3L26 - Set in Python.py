
# SETS are unordered collections of unique elements.

# Meaning that there can be only one representative of
# the same Obj. e.g. "A" or number 2 can’t be repeated.

mySet1 = set()

mySet1
# set()


mySet1.add(1)

mySet1
# {1}


mySet1.add(2)

mySet1
# {1, 2}


# Check if we can add the same Obj representative.

mySet1.add(2)

mySet1
# {1, 2}
# No we can't.


# The useful way of using:
myList2 = [1,1,1,1,4,4,4,4,2,2,2,3,3]

set(myList2)
# {1, 2, 3, 4}



myList3 = [1,3,2,2,2,3,1,1,3,2,3,2]

set(myList3)
# {1, 2, 3}
