
# Immutability of a Strings = (Can't change):
# You can't use indexing[ ] to change individual elements of a string.
# Only by concatenation or by reassigning a new one.

name = "Sam"
last_letters = name[1:]
# Result: 'am'


newName = "P" + last_letters
# Result: 'Pam'


x = "Hello,"
x += " it is beautiful outside."
# Result: 'Hello, it is beautiful outside.'


char = "Z"
char *= 10
# Result: 'ZZZZZZZZZZ'


# Don't confuse (DataTypes) numbers & strings with numbers in them:
"2" + "3"
# Result: '23'


# Obj-s in Python have build in methods, which are functions inside an Obj.
x = "Hello Darling"
x.upper()
# Temporary result: 'HELLO DARLING'

# But original x variable will still will be: 'Hello Darling'
# To affect the original String, a reassignment is needed:

x = x.upper()
# Result: 'HELLO DARLING'

x.lower()
# Temporary result: 'hello darling'


# (Split) creates a List of Strings.
# Split devides string by a space or selected letter or a sign in brackets ( )

x.split()
# Result: ['Hello', 'Darling']


z = "Hi, this is a string"
z.split("i")
# Result: ['H', ', th', 's ', 's a str', 'ng']