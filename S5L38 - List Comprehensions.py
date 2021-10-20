
# List Comprehensions are a  unique way  to quickly create a list with Python.

# If you create a List with a for loop + .append( ), a List Comprehension is a good alternative.


# Making a List of Every Character in a String:

myStr = "Hello"
myList = []

for letter in myStr:
    myList.append(letter)

myList
#['H', 'e', 'l', 'l', 'o']


#List Comprehension:

myLst2 = [ltr2 for ltr2 in myStr]

myLst2
# ['H', 'e', 'l', 'l', 'o']



myLst3 = [x for x in "Word"]

myLst3
# ['W', 'o', 'r', 'd']


myList4 = [num for num in range(0, 11)]

myList4
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



myList5 = [num**2 for num in range(0, 11)]

myList5
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



myList6 = [y for y in range(0, 11) if y%2 == 0]

myList6
# [0, 2, 4, 6, 8, 10]



celcius = [0,10,25.5,34.5]
fahrenheit = [( (9/5) * temp + 32) for temp in celcius]

fahrenheit
# [32.0, 50.0, 77.9, 94.1]



fahrenheit2 = []

for elmnt in celcius:
    fahrenheit2.append((9/5) * elmnt + 32)

fahrenheit2
# [32.0, 50.0, 77.9, 94.1]


# If statements is hard to read:


res = [n if n%2 == 0 else "ODD" for n in range(0,11)]

res
# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]


# Nested Loops in List Comprehension:

mL = []

for u in [2,4,6]:
    for z in [1,10,100]:
        mL.append(u*z)

mL
# [2, 20, 200, 4, 40, 400, 6, 60, 600]


mLt = [a*b for a in [2,4,6] for b in [1,10,100]]

mLt
# [2, 20, 200, 4, 40, 400, 6, 60, 600]