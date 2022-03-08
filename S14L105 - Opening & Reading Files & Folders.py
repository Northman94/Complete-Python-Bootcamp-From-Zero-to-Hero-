
# A) How to open file in a Directory ?

#pwd  #jupiter & Mac/Linus command
# '/Users/.../Documents/.../Python Lessons Jupiter'

f = open('s14l15_1.txt','w+')

f.write('This is a Text str.')

f.close()



# = - = - = - = - = - = - = - = - = - =
import os

os.getcwd()
# '/Users/.../Documents/.../Python Lessons Jupiter'



# = - = - = - = - = - = - = - = - = - =
# Listing Files in a Directory:

os.listdir('/Users/.../Documents')
# ['IT', 'Kindle Books']


# = - = - = - = - = - = - = - = - = - =
# B) Move File around PC:

# May need permissions to do this:
import shutil

shutil.move('s14l15_1.txt','/Users/Zh/Desktop')
# '/Users/.../Desktop/s14l15_1.txt'


# = - = - = - = - = - = - = - = - = - =
# Ways to Delete Files:

# NOTE: The os module provides 3 methods for deleting files:

# os.unlink(path) ==> which deletes a file at the path your provide
# os.rmdir(path)  ==> which deletes a folder (folder must be empty) at the path your provide
#       So unlink all files & then delete an empty Folder.

# shutil.rmtree(path)  ==> this is the most dangerous, as
# it will remove all files and folders contained in the path.

# All of these methods can not be reversed! Which means if you make
# a mistake you won't be able to recover the file.
# Instead we will use the send2trash module.
# A safer alternative that sends deleted files to the trash
# bin instead of permanent removal.


# Install the send2trash module at command line:
#  pip install send2trash



# = - = - = - = - = - = - = - = - = - =
# Move File to a current working Directory:

shutil.move('/Users/Zh/Desktop/s14l15_1.txt', os.getcwd())
# '/Users/Zh/Documents/IT/Udemy/Python/Python Lessons Jupiter/s14l15_1.txt'

import send2trash

send2trash.send2trash('s14l15_1.txt')



# = - = - = - = - = - = - = - = - = - =
# Directory Tree Generator:

import os

# Tuple unpacking:

file_path = os.getcwd()

for folder, sub_folders, files in os.walk(file_path):

    print(f"Currently looking at {folder}.\n")
    print("The subfolders are: \n")

    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")

    print("\n The Files are:")
    for f in files:
        print(f"\t File: {f}")

# Will list current Folder, sub-folder list & inner files list.

