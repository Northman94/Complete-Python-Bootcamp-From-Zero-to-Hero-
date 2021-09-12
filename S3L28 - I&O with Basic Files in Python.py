"""

# Creation of a Text file ONLY in Jupiter Notebook:

%%writefile myFile.txt

Hello, this is a text file.

Second text line.
Third text line.

# Return: Writing myFile.txt
# Empty lines are also considered.

myFile = open("myFile.txt")

# If I try to type any other File name, we will get Error No_2 FileNotFoundError
# To get your working directory:

pwd
# '/Users/User/Documents/...'

# .read() method returns a giand string with whole file:

myFile.read()
# '\nHello, this is a text file.\n\nSecond text line.\nThird text line.\n'

# Read it again and get nothing:

myFile.read()
# ''

# This happened because the cursour after reading was set to the end of a file.
# To reset coursour:

myFile.seek(0)
# 0

myFile.read()
# '\nHello, this is a text file.\n\nSecond text line.\nThird text line.\n'

# ∆∆∆ Can be stored in a variable if needed ∆∆∆


# To have more convenient view of file content:

myFile.seek(0)
# 0

myFile.readlines()
# ['\n',
#  'Hello, this is a text file.\n',
#  '\n',
#  'Second text line.\n',
#  'Third text line.\n']

# ∆∆∆ This allows to loop through this list. Or index over the lines.∆∆∆
"""

# ...
'''
# File Location:

# For WINDOWS double back-slashes "\\" is used,
# to not to be confused with an Esc-sequence (экранированием).

myFile = open ("С:\\Users\\Username\\Folder\\testFile.txt")

# For MacOS & Linux we use opposite direction forward-slashes:

myFile = open ("/Users/Username/Folder/testFile.txt")


# After you done working with File, file stream should be closed:

myFile.close()

# Another way. Stream here closes automatically:
with open("myFile.txt") as my_new_file:
    contents = my_new_file.read()

    contents
# '\nHello, this is a text file.\n\nSecond text line.\nThird text line.\n'


# Shift + Tab before "" will open List of functions that are already have been defined (Documentation):

with open("myFile.txt", mode = "r") as myFile:
    contents = myFile.read()

contents
# '\nHello, this is a text file.\n\nSecond text line.\nThird text line.\n'


# Permissions:
# mode = "r" is read only;
# mode = "w" is write only; owerwrite file or create New one;
# mode = "a" is for append; (will add on to File's end)
# mode = "r+" is r + w;
# mode = "w+" (owerwrites a File or creates a New one & reads it);


%%writefile myFile2.txt

ONE ON FIRST
TWO ON SECOND
THREE ON THIRD
# Writing myFile2.txt


with open("myFile2.txt", mode = "r") as f:
    print(f.read())
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD


# Adding a new Line:
with open("myFile2.txt", mode = "a") as f:
    f.write("FOUR ON FOURTH")

# Re-run previous code:
with open("myFile2.txt", mode = "r") as f:
    print(f.read())
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD
# FOUR ON FOURTH

# Due to mode "w" there is no Error for overwriting / creating New File:
with open ("12345.txt", mode = "w") as f1:
    f1.write("Another text file")


# Shorter variation:
x1 = open("myFile123.txt", "w")
x1.write("Some text.")
x1.close()

'''













