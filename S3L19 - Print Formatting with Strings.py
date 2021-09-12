
# Concatination (Склеивание)

myName = "Jose"
print("Hello, " + myName)
# Hello, Jose


# Interpolation (вкладывание в слоты):

"String here {} then also {}".format("str1", "str2")
print("Her name was {}".format("Jenny."))
# Her name was Jenny.


print("The {} {} {}.".format("fox", "brown", "quick"))
# The fox brown quick.


print("The {2} {1} {0}.".format("fox", "brown", "quick"))
# The quick brown fox.


print("The {0} {0} {0}.".format("fox", "brown", "quick"))
# The fox fox fox.


# Using Key-words:

print("The {f} {f} {f}.".format(f = "fox", b = "brown", q = "quick"))
# The fox fox fox.

print("The {q} {b} {f}.".format(f = "fox", b = "brown", q = "quick"))
# The quick brown fox.


# Float formatting: {value:beforeCommaWidth.presision f}

result = 100/777
print(result)
# 0.1287001287001287

print("Result: {}".format(result))
# Result: 0.1287001287001287

print("Result: {r}".format(r = result))
# Result: 0.1287001287001287

print("Result: {r:1.3f}".format(r = result))
# Result: 0.129


# F-string: (Python 3.6)

name = "Joe"
age = 10

print(f"{name} is {age} years old.")
# Joe is 10 years old.