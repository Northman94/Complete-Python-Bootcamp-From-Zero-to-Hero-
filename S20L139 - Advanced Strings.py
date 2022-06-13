
# Advanced Strings

s = 'hello world'


# Changing case

# We can use methods to capitalize the first word of a string,
# or change the case of the entire string.

# Capitalize first word in string
s.capitalize()
# 'Hello world'

s.upper()
# 'HELLO WORLD'

s.lower()
# 'hello world'

# Remember, strings are immutable.
# None of the above methods change the string in place,
# they only return modified copies of the original string.

print(s)
# 'hello world'

# To change a string requires reassignment:

s = s.upper()
print(s)
# 'HELLO WORLD'

s = s.lower()
print(s)
# 'hello world'


# Location and Counting
s.count('o') # returns the number of occurrences, without overlap
# 2


s.find('o') # returns the index of the first occurence
# 4


# Formatting
# The center() method allows you to place your string 'centered'
# between a provided string with a certain length. Personally,

s.center(20,'=')
'====hello world====='


# The expandtabs() method will expand tab notations \t into spaces:

print('helo\thi')
#   helo	hi


'hello\thi'.expandtabs()
#  'hello   hi'


# is check methods:
# These various methods below check if the string is some case.

s = 'hello321'
# isalnum() will return True if all characters in s are alphanumeric

s.isalnum()
# True


# isalpha() will return True if all characters in s are alphabetic

s.isalpha()
# False


#  islower() will return True if all cased characters in s are lowercase
#  and there is at least one cased character in s, False otherwise.
s.islower()
# True


# isspace() will return True if all characters in s are whitespaces.
' '.isspace()
# True


# istitle() will return True if s is a title cased string and there is
# at least one character in s, i.e. uppercase characters may only follow
# uncased characters and lowercase characters only cased ones.
# It returns False otherwise.
'Hello'.istitle()
# True


# isupper() will return True if all cased characters in s are uppercase
# and there is at least one cased character in s, False otherwise.

s.isupper()
# False


# Another method is endswith() which is essentially the same as a boolean check on s[-1]
s.endswith('o')
# True



# Built-in Reg. Expressions
# Strings have some built-in methods that can resemble regular expression operations.
# We can use split() to split the string at a certain element and return a list of the results. We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.


s.split('e')
# ['h', 'llo']


'h8e8l8l8o'.split('8')
# ['h', 'e', 'l', 'l', 'o']


'hello'.partition('l') # first part // first separator // end
# ('he', 'l', 'lo')


