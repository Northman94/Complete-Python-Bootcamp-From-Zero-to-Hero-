
# Create 2 Files:

f = open('unZfile.txt', 'w+')
f.write('ONE FILE')
f.close()


f = open('unZfile2.txt', 'w+')
f.write('TWO FILE')
f.close()

# Better fold in try/except/finally

# = - = - = - = - = - = - = - = - = - =
# Create a Zip-File First:

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')

comp_file.write('unZfile.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('unZfile2.txt', compress_type = zipfile.ZIP_DEFLATED)

comp_file.close()

#Now we have 2 compressed files in a Zip.file


# = - = - = - = - = - = - = - = - = - =
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')

# zip_obj.extract()
zip_obj.extractall('extracted_content')

# print



# = - = - = - = - = - = - = - = - = - =
# We usually don't zip one file. We archaive the entire Folder.

import shutil

# We point a directory we want to turn into Zip-file.

dir_to_zip = '/Users/Zh/Documents/IT/Udemy/Python/Python Lessons Jupiter/extracted_content' # extracted_content

output_file_name = 'output_file'

shutil.make_archive(output_file_name, 'zip', dir_to_zip)


# Extracting content:

shutil.unpack_archive('output_file.zip', 'final_unzip','zip')

