
#Links on Regecs:

# https://regexlearn.com/learn

# https://jex.im/regulex/#!flags=&re=%5E(a%7Cb)*%3F%24



# Overview of Regular Expressions

# Regular Expressions (sometimes called regex for short) allows a user
# to search for strings using almost any sort of rule they can come up.
# For example, finding all capital letters in a string, or finding
# a phone number in a document.

# Regular expressions are notorious for their seemingly strange syntax.
# This strange syntax is a byproduct of their flexibility.
# Regular expressions have to be able to filter out any string pattern
# you can imagine, which is why they have a complex string pattern format.


# We can search for sub-strings in a larger string and get a bool result:

"dog" in "my dog is great"
# True


# We search for e-mails by certain pattern:
"text" + "@" + "text" + ".com"

# The  "re"  Library allows us to create specialized pattern strings
# & then Search for matches within text.

# The primary skill set for Regex is understanding
# the special syntax for these pattern strings.


# = - = - = - = - = - = - = - = - = - =
# Phone Number:
# (555)-555-5555
r"(\d\d\d)-\d\d\d-\d\d\d\d"

#or

r"(\d{3})-\d{3}-\d{4}"  #{} => quantifiers


# = - = - = - = - = - = - = - = - = - =
import re

text = "The agent's phone Numb is 408-555-1234. Call soon!"
pattern = "phone"

print(re.search(pattern, text))

pattern2 = "NOT IN TEXT"

print(re.search(pattern2, text))
# None


# = - = - = - = - = - = - = - = - = - =
pattern3 = "phone"

match = re.search(pattern3, text)

match.start()
# 12

match.span()
# (12, 17)

match.end()
# 17

# In case we have a multiple matches inside a string, we will receive first one, but...
text2 = "My phone - once, my phone - twice."

match2 = re.findall('phone', text2)

print(match2)
# ['phone', 'phone']

len(match2)
# 2


# = - = - = - = - = - = - = - = - = - =
for obj in re.finditer('phone', text2):
    print(obj.span())
# (3, 8)
# (20, 25)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
#  Character   |    Description     |    Example Pattern    |    Example Match  |
#----------------------------------------------------------------------------------
#     \d             A Digit               file_\d\d             file_42

#     \w            Alphanumeric           \w-\w\w\w              A-b_1
#
#     \s             White Space            a\sb\sc               a b c
#
#     \D             A non digit             \D\D\D                ABC
#
#     \W          Non-alphanumeric         \W\W\W\W\W              *-+=)
#
#     \S            Non-whitespace          \S\S\S\S               Yoyo
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =


txt1 = "My phone number is 408-555-1234"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',txt1)

# Better use Quantifiers:  r'\d{3}-\d{3}-\d{4}'

print(phone)
# <re.Match object; span=(19, 31), match='408-555-1234'>

print(phone.group())
# 408-555-1234


# = - = - = - = - = - = - = - = - = - =
# Notice the repetition of \d. That is a bit of an annoyance, especially if we are
# looking for very long strings of numbers. Let's explore the possible quantifiers.

## Quantifiers:

# Now that we know the special character designations, we can use
#  them along with quantifiers to define how many we expect.



# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
#  Character        Description         Example Pattern Code        Exammple Match
#----------------------------------------------------------------------------------
#     +       Occurs one or more times      Version \w-\w+          Version A-b1_1

#    {3}       Occurs exactly 3 times           \D{3}                    abc

#   {2,4}       Occurs 2 to 4 times             \d{2,4}                  123

#    {3,}         Occurs 3 or more                \w{3,}              anycharacters

#     \*       Occurs zero or more times          A\*B\*C*                AAACC

#      ?             Once or none                plurals?                plural
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =


# Group compile:

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #Three separate Phone Groups.

res = re.search(phone_pattern,txt1)

print(res.group())
# 408-555-1234

print(res.group(2))
# 555


# Aditional Rejex synthax:
# Or operator " | " (pipe operator " | ")

import re

re.search(r"cat|dog", "The dog is here")
# <re.Match object; span=(4, 7), match='dog'>

re.findall(r"at", "The cat in the hat sat there.") #len()
# ['at', 'at', 'at']

re.findall(r".at", "The cat in the hat sat there.") # "." is for any character
# ['cat', 'hat', 'sat']


# = - = - = - = - = - = - = - = - = - =
# If a string starts with smth:
re.findall(r"^\d", "1 is a Numb")  # " ^ " means "string Starts with"
# ['1']

re.findall(r"^\d", "The 1 is a Numb")
# []   # No match


re.findall(r"\d$", "The number is 2") # " $ " means "string Ends with"
# ['2']


# = - = - = - = - = - = - = - = - = - =
# Exclude:
phase = "There are 3 numbers 34 in this 8 text"

# Exclude Digits:
pattern = r'[^\d]'

re.findall(pattern,phase)
# ['T',
#  'h',
#  'e',
#  'r',
#  'e',
#  ' ',
#  'a',
#  'r',
#  'e',
#  ' ',
#  ' ',
#  'n',
#  'u',
#  'm',
#  'b',
#  'e',
#  'r',
#  's',
#  ' ',
#  ' ',
#  'i',
#  'n',
#  ' ',
#  't',
#  'h',
#  'i',
#  's',
#  ' ',
#  ' ',
#  't',
#  'e',
#  'x',
#  't']


# = - = - = - = - = - = - = - = - = - =
#  " + " sign is for grouping. Will split at removed Object place.

pattern2 = r'[^\d]+'

re.findall(pattern2,phase)
# ['There are ', ' numbers ', ' in this ', ' text']


# Remove punctuation:
punctuat = "This is a string! But it has punctuation. How can we remove it?"

re.findall(r'[^!.?]+', punctuat)
# ['This is a string', ' But it has punctuation', ' How can we remove it']

no_spaces = re.findall(r'[^!.? ]+', punctuat) #Added exclude space

' '.join(no_spaces)
# 'This is a string But it has punctuation How can we remove it'


# = - = - = - = - = - = - = - = - = - =
# Include:

sntce = "Only find hypen-words in this sentece. But you do not know how long-ish they are."

ptrn = "[\w]+"

re.findall(ptrn, sntce)
# ['Only',
#  'find',
#  'hypen',
#  'words',
#  'in',
#  'this',
#  'sentece',
#  'But',
#  'you',
#  'do',
#  'not',
#  'know',
#  'how',
#  'long',
#  'ish',
#  'they',
#  'are']


# = - = - = - = - = - = - = - = - = - =
ptrn2 = "[\w]+-[\w]+"

re.findall(ptrn2, sntce)
# ['hypen-words', 'long-ish']


# = - = - = - = - = - = - = - = - = - =
# Will get same result here:
# but difficult to read

ptrn3 = "\w+-\w+"

re.findall(ptrn3, sntce)
# ['hypen-words', 'long-ish']



# = - = - = - = - = - = - = - = - = - =
t1 = "Hello, would you like some catfish?"
t2 = "Hello, would you like to take a catnap?"
t3 = "Hello, have you seen this caterpillair?"

re.search(r'cat(fish|nap|erpillair)', t1)
# <re.Match object; span=(27, 34), match='catfish'>

re.search(r'cat(fish|nap|erpillair)', t2)
# <re.Match object; span=(32, 38), match='catnap'>

re.search(r'cat(fish|nap|erpillair)', t3)
# <re.Match object; span=(26, 38), match='caterpillair'>
