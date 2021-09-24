# Iterable =  obj can be iterated over. Go through every element in the Obj.
# Through every letter in a String, every Obj is a List, every Key in a Dictionary…

# Syntax of a "for" Loop:

my_iterable = [1,2,3]

for every_elmnt in my_iterable:
    print(every_elmnt);

print("\n");


myList = [1,2,3,4,5]

for numb in myList:
    print(numb)

print("\n");


myList1 = [1,2,3]

for i in myList:
    print("hello")

print("\n");


myList2 = [1,2,3,4,5]

for numb2 in myList2:
    # Check for even numbs
    if numb2 % 2 == 0:
        print(numb2)
    else:
        print(f"Odd Number: {numb2}")


# Difference of TAB usage:

list_sum = 0

for j in myList2:
    list_sum = list_sum + j
    print(list_sum)

print("\n");


listSum = 0

for j in myList2:
    listSum = listSum + j

print(listSum)

print("\n");


myString = "Hello World"

for letter in myString:
    print(letter)

print("\n");


for letter in "Hello World":
    print(letter)

print("\n");


for _ in "Hello":
    print("Great")

print("\n");



# We can use "_" instead of a variable name, if we don't use it:

tup = (1,2,3)

for k in tup:
    print(k)

print("\n");


listOfTuples = [(1,2), (3,4), (5,6), (7,8)]
len(listOfTuples)

print("\n");


for jk in listOfTuples:
    print(jk)

print("\n");


# Tuple Unpacking:
#  "( )" can be not used

for (a,b) in listOfTuples:
    print(a)
    print(b)

print("\n");


for (a,b) in listOfTuples:
    print(a)

print("\n");


dctnry = {"k1":1, "k2":2, "k3":3}

for x in dctnry:
    print(x)

print("\n");


dctnry = {"k1":1, "k2":2, "k3":3}
for x in dctnry.items():
    print(x)

print("\n");


dctnry1 = {"k1":1, "k2":2, "k3":3}
for x in dctnry1.values():
    print(x)

print("\n");


dctnry2 = {"k1":1, "k2":2, "k3":3}
for key,value in dctnry1.items():
    print(value)

print("\n");
