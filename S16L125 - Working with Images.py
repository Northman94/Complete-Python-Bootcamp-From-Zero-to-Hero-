
# pip install pillow
import pillow
from PIL import Image

mac = Image.open('example.jpg')

type(mac)
# PIL.JpegImagePlugin.JpegImageFile


# In Jupiter Notebook:
# mac

# In PyCharm:
mac.show()
# This will open image on your PC

# To Crop, we need to know the size first
print(mac.size)   # Coordinates
# (1993, 1257)

print(mac.filename)
# 'example.jpg'

print(mac.format_description)
# 'JPEG (ISO 10918)'

# = - = - = - = - = - = - = - = - = - =

# Cropping Images = Grabbing a sub-section¶

mac.crop( (850,850, 1200,1200) )  #Tuple

pencils = Image.open('pencils.jpg')
pencils.show()

print(pencils.size)
# (1950, 1300)


# Start Coordinates
x = 0
y = 0
# Crop Size
w = 1950 / 3  # 30% of the width
h = 1300 / 10
pencils.crop( (x,y, w,h) )


print(mac.size)
# (1993, 1257)

half = 1993 / 2
x = half - 200
w = half + 200

y = 800
h = 1200
mac.crop( (x,y, w,h) )

# = - = - = - = - = - = - - =

# Ctrl + C & Ctrl + V on on another:

computer = mac.crop((x,y, w,h))

mac.paste(im = computer, box = (0,0)) #(0,0) if for to-left corner

mac.show()



# = - = - = - = - = - = - - =
# Resize:

print(mac.size)
# (1993, 1257)

mac.resize((3000,500)) #Tuple

mac.rotate(90) #counterclock-wise



# = - = - = - = - = - = - - =
# Color Transparancy:
# RGBA = Red, Green, Blue, Alpha
# If Alpha is 0, then Image is transparent
# If it's 255, then its completely opaque

red = Image.open('red_color.jpg')
red.show()


blue = Image.open('blue_color.png')
newblue = blue.convert('RGB')
newblue.save("newblue.jpg")          # new file
blue = Image.open('newblue.jpg')    # importing new file as blue
blue.show()

# Transparent:
blue.putalpha(0) # transparent
blue.show()


blue.putalpha(150) # transparent
blue.show()


red.putalpha(90)
red.show()


blue.paste(im = red, box = (0,0), mask = red)
blue.show()



# Save a new color:
blue.save("purple.png")
purple = Image.open("purple.png")

