
# Un-Zip instruction file:

import zipfile

unz = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
unz.extractall('instructions')


# OR


import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','instructions')

extr_path = '/Users/.../instructions.txt'

with open(extr_path) as f:
    content = f.read()
    print(content)

# Good work on unzipping the file!
# You should now see 5 folders, each with a lot of random .txt files.
# Within one of these text files is a telephone number formated ###-###-####
# Use the Python os module and regular expressions to iterate through each file,
# open it, and search for a telephone number.

# = - = - = - = - = - = - = - = - = - = - = - = - =


'''
Find a Telephone number in text files in dir.
'''

import os
import re

pattern = r'\d{3}-\d{3}-\d{4}'

for path, folders, files in os.walk(os.getcwd()):
    print(f'Path: {path}\n')
    print(f'Folders: {folders}\n')
    print(f'Files: {files}')
    print("= - = - = - = - = - = - = - = - =\n")

    for file in files:

        if file.endswith(".txt"):

            open_file = open(f'{path}/{file}', 'r')
            text = open_file.read()

            phone_number = re.findall(pattern, text)

            if phone_number != []:
                print(f"The phone number is: {phone_number}")

            open_file.close()

# The phone number is: ['719-266-2837']

