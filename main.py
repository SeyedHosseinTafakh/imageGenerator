# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:24:15 2018

@author: hossein
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from PIL import Image
from resizeimage import resizeimage
import random

back_img = Image.open('image_tutorial-1.png')


# open image and resize it
img = Image.open('bird.jpg')
img = resizeimage.resize_cover(img , [200,200])

# showing the result
plt.imshow(back_img)
back_img.size()


# we crop image to sizes that we want
#(left, upper, right, lower)
crop_rectabgle = (100,150,300,200)
back_img2 = back_img.crop(crop_rectabgle)

plt.imshow(back_img2)




input_image = Image.open('Lenna.png')
bc_width , bc_height = back_img.size


# the size of image we putting inside the data generator
input_width , input_height = input_image.size
i = 0
#preparing the image generator
for i in range(0,10):
    random_left = random.randint(0 ,bc_width - input_width)
    random_upper = random.randint(0, bc_height - input_width)
#    print(random_left)
#    print(random_upper)
    right = random_left + input_width
    lower = random_upper + input_height
    crop_rectangle = (random_left , random_upper , right , lower)
    new_image=  input_image.crop(crop_rectangle)
#    final_images[i] = new_image
#    plt.imshow(new_image)
    Image._show(new_image)
    i +=1










#bc = image.imread('bird.jpg')
#bc2 = image.imread('image_tutorial-1.png')


#bcw = bc[:100 , : 100]

#bc.setflags(write=1)

#new_image = bc[:100 , :100 ] = bcw

#lum_img = plt.imshow(bc[:200,:100 , :])

#plt.imshow(new_image)
















