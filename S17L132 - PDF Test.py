
# PDFs and Spreadsheets Puzzle Exercise
# Let's test your skills, the files needed for this puzzle exercise
# You will need to work with two files for this exercise and solve the following tasks:
# Task One: Use Python to extract the Link to Google Drive from the .csv file.
# (Hint: Its along the diagonal from top left to bottom right).
# Task Two: Download the PDF from the Google Drive link
# (we already downloaded it for you just in case you can't download from Google Drive)
# and find the phone number that is in the document.
# Note: There are different ways of formatting a phone number!

# Task One: Grab the Google Drive Link from .csv File

import csv


file_stream = open('/Users/Zh/Documents/IT/Udemy/Python/Udemy Python All materials'+
                   '/15-PDFs-and-Spreadsheets/Exercise_Files/find_the_link.csv', encoding='utf-8')

# Note: we can devide with '+' in open()

# Reading CSV:
csv_data = csv.reader(file_stream)

# Reformat to Py-Obj:
data_lines = list(csv_data)

print(data_lines)
# [['h', '53', '24', '46', '4', '11', '3', '35', '17', '52', '9', ...


# We see that 'https' letters are shifted on 1, every [block]
len(data_lines) #Ammount of Rows [ ]
# 66


link = []
n = 0

for elmnt in data_lines:
    link.append(elmnt[n])

    n += 1

print(link)
print('\n')

final_link = "".join(link)
print(final_link)

# = - = - = - = - = - = - = - =
# Teacher:

link_str = ''

for row_num, data in enumerate(data_lines):
    link_str += data[row_num]

print('\n')
print(link_str)
# ['h', 't', 't', 'p', 's', ':' ...
#
# https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q

file_stream.close()
# better use (with open)

# = - = - = - = - = - = - = - = - = - = - = - =
# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.

# Save File to PC:

import requests


URL = 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'
response = requests.get(URL)

# This will save file where this code is Executed:

stream = open("PhonePDF.pdf", "wb")

stream.write(response.content)
stream.close()


# Get phone number from Google Drive PDF:
# 505 503 4455

import PyPDF2

w_directory = '/Users/Zh/Documents/IT/Udemy/Python/Udemy Python All materials/15-PDFs-and-Spreadsheets/PhonePDF.pdf'

# strm = open(w_directory, 'rb')


pdf_text = []

with open(w_directory, 'rb') as strm:
    pdf_reader = PyPDF2.PdfFileReader(strm)

    # Ammount of Pages:
    print(pdf_reader.numPages)
    print('\n')

    for elmt in range(pdf_reader.numPages):
        print(elmt)

        page = pdf_reader.getPage(elmt)

        pdf_text.append(page.extractText())

print(pdf_text)


# = - = - = - = - = - = - = - = - = - = - =

# Some error with file:
# So just copy Teaher code:

import re

pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ''

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text


for match in re.finditer(pattern, all_text):
    print(match)


all_text[41808:41808+20] #From to location on a Page








