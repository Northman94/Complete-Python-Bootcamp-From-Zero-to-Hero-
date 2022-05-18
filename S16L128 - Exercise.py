
# Image Exercise
# In the folder "Working with Images" there are two images we will be working with:
# word_matrix.png
# mask.png
# The word_matrix is a .png image that contains a spreadsheet
# of words with a hidden message in it.
# Your task is to use the mask.png image to reveal the hidden message
# inside the word_matrix.png. Keep in mind, you may need to make changes
# to the mask.png in order for this to work.

from PIL import Image

background = Image.open('matrix.png')
mask = Image.open('mask.png')

h,w = background.size
resized_mask = mask.resize((h,w))

resized_mask.putalpha(200)


background.paste(resized_mask, (0,0), resized_mask)
background.show()