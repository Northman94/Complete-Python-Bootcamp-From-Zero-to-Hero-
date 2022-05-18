
#  CSV   - stands for ''comma separated Variables''.
#
# Can be separated with something else: Tab, Horizontal Bar, semicolon etc.
#
# It’s a common output for spreadsheet Programs.
#
# Example:
# Name,   Hours,    Rate
# David,    20,      15
# Clare,    40,      20
#
#
# When Excel & GoogleSpreadsheets  are exported to .CSV files, only info is transferred.
# NO formulas, images, macros etc. within a .CSV file.
# Only RAW Data.
#
#
# Other Libraries to Explore:
#
# Pandas:
#  full Data analysis (works with most tabular Data types);
# runs Visualizations & analysis.
#
#
# Openpyxl:
# Designed for Excel files;
# retains a lot of Excel-specific functionality;
# supports Excel formulas;
# python-excel.org  tracks other Excel-based Python Libraries.
#
#
# Google Sheets Python API:
# direct Python interface   for working with Google Spreadsheets;
# allows to make direct changes to the Spreadsheets hosted Online;
# more complex syntax, but available in many Programming Languages.

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - =


# A WRONG WAY:
import csv

# Open file
data = open('example.csv') # name or path


# call a csv.reader on it to convert to CSV data
csv_data = csv.reader(data) #delimiter can be used


# reformat it into a Py-Obj [List of Lists]
data_lines = list(csv_data)
print(data_lines)


# Should be a UnicodeDecodeError
# This means that a file may have different Encodings. = Unable to read special characters.
# e.g. @ or Spanish letters
# have a Google search for correct relevant Encoding type



# = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# A Right Way (with encoding):

# Open file
data = open('example.csv',encoding='utf-8') # name or path


# call a csv.reader on it to convert to CSV data
csv_data = csv.reader(data)


# reformat it into a Py-Obj [List of Lists]
data_lines = list(csv_data)
print(data_lines)


len(data_lines) # ammount of rows from [ to ]
#1001


print(data_lines[0])
# ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']


print(data_lines[1])
# ['1',
#  'Joseph',
#  'Zaniolini',
#  'jzaniolini0@simplemachines.org',
#  'Male',
#  '163.168.68.132',
#  'Pedro Leopoldo']


for line in data_lines[:5]:
    print(line)

# ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
# ['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo']
# ['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri']
# ['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver']
# ['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']



print(data_lines[2][3])
# 'fdrillingcourt1@umich.edu'



all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails)



# = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# Merging Name + Surname:

data_lines[10]
# ['10',
#  'Hyatt',
#  'Gasquoine',
#  'hgasquoine9@google.ru',
#  'Male',
#  '221.155.106.39',
#  'Złoty Stok']


full_names = []

for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

full_names



# = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# Writing to a .CSV file:

file_to_output = open('to_save_file.csv', mode = 'w', newline = '') #Will override existing one.

csv_writer = csv.writer(file_to_output, delimiter = ';') #Or TAB: delimiter = '\t'

csv_writer.writerow(['a','b','c'])
#7

csv_writer.writerow([['1','2','3'],['4','5','6']])
# 33

file_to_output.close()



# = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# Adding new rows:

f = open('to_save_file.csv', mode = 'a', newline = '') # a = append
csv_writer = csv.writer(f)

csv_writer.writerow(['1','2','3'])
# 7    #Output shows ammount of writter Characters


f.close()

