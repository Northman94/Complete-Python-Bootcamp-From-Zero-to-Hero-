
# While loops will continue to execute a block of code while some condition remains True.

# Syntax:
'''
 while some_boolean_condition:
     #do something


 while some_boolean_condition:
     #do something
 else:
     #do smth else
'''

x = 0

while x < 5:
    print(f"Current value of X is {x}")
    x = x + 1
    #or
    x += 1
else:
    print("X is greater than 5")


print("\n");
'''
Keywords:

break: Breaks out of the current closest enclosing loop;

continue: Goes to the top of the closest enclosing loop;

pass: Does nothing at all. A Placeholder to avoid Loop errors.

'''

z = [1,2,3]

for item in z:
    #comment
    pass


print("\n");

myString = "Sammy"

for letter in myString:
    if letter == "m":
        continue
    print(letter)


print("\n");

myString = "Sammy"

for letter in myString:
    if letter == "m":
        break
    print(letter)


print("\n");

x1 = 0

while x1 < 5:
    if x1 == 2:
        break
    print(x1)
    x1 += 1





















