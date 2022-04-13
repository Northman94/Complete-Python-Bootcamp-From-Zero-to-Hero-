
# Images on a Website tipically have their own URL link. (ending in .jpg or .png)

# Beautiful Soup can scan a Webpage, locate the <img> tags and grab these URLs.

# Then we can Download the URLs as Images & write them to PC.

# !!! Always check copyright permission before Downloading & Using image from a Website.
# Wikipedia is open sourсe.


# Wikipedia:Ten things you may not know about images on Wikipedia:

# https://en.wikipedia.org/wiki/Wikipedia:Ten_things_you_may_not_know_about_images_on_Wikipedia


import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text,"lxml")

soup.select('img')[0] #no need to put <> because it's a HTML tag.

# <img alt="This is a good article. Click here for more information."
# data-file-height="185" data-file-width="180" decoding="async" height="20"
# src="//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol
# _support_vote.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/94/
# Symbol_support_vote.svg/29px-Symbol_support_vote.svg.png 1.5x,
# //upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/
# 39px-Symbol_support_vote.svg.png 2x" width="19"/>


# <img alt=
# "alt" means, if the image can't be found, show an alternative.
#  src=  is what we are looking for (source). Every Image on Wiki has it unique URL.


soup.select('.thumbimage')
# Use dot(.) because it's a Class.

# [<img alt="" class="thumbimage" data-file-height="600" data-file-width="800"
# decoding="async" height="165" src="//upload.wikimedia.org/wikipedia/commons/thumb/
# 6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png"
# srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/
# 330px-Kasparov_Magath_1985_Hamburg-2.png 1.5x, //upload.wikimedia.org/wikipedia/
# commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/440px-Kasparov_Magath_1985_Hamburg-2.png
# 2x" width="220"/>,

#  <img alt="" class="thumbimage" data-file-height="2756" data-file-width="2067"
#  decoding="async" height="293" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/83/
#  One_of_Deep_Blue%27s_processors_%282586060990%29.jpg/
#  220px-One_of_Deep_Blue%27s_processors_%282586060990%29.jpg"
#  srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/83/
#  One_of_Deep_Blue%27s_processors_%282586060990%29.jpg/
#  330px-One_of_Deep_Blue%27s_processors_%282586060990%29.jpg 1.5x,
#  //upload.wikimedia.org/wikipedia/commons/thumb/8/83/
#  One_of_Deep_Blue%27s_processors_%282586060990%29.jpg/
#  440px-One_of_Deep_Blue%27s_processors_%282586060990%29.jpg 2x" width="220"/>]


comp_img = soup.select('.thumbimage')[0]

print(comp_img)

# <img alt="" class="thumbimage" data-file-height="600" data-file-width="800"
# decoding="async" height="165" src="//upload.wikimedia.org/wikipedia/commons/thumb/
# 6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png" srcset="
# //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/
# 330px-Kasparov_Magath_1985_Hamburg-2.png 1.5x, //upload.wikimedia.org/wikipedia/commons/
# thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/
# 440px-Kasparov_Magath_1985_Hamburg-2.png 2x" width="220"/>


type(comp_img)

# is not a String
# will treat as a Dictionary
# it's a tag-Obj

# bs4.element.Tag


comp_img['class']
# ['thumbimage']


comp_img['src']
# '//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/
# Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png'



# In Jupiter use Markup mode to see image:

# <img
# src= "//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/
# Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png">


# Add:  https://

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/'
'6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')



# binary file:
image_link.content

# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\...



# Save image on PC:

# image format should match URL format (e.g. .jpg)
# wb = write binary

f = open('my_PC_image.jpg', 'wb')

f.write(image_link.content)
# 85054

f.close()


# Image Downloaded
# If you want to save in another place: 'my_PC_image.jpg' instead of this use fule File path.


