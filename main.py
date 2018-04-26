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
import pandas as pd

# open image 
#img = Image.open('test.jpg')

# we crop image to sizes that we want
#(left, upper, right, lower)
#crop_rectabgle = (100,150,300,200)
#back_img2 = back_img.crop(crop_rectabgle)



#getting the backgrounds
import glob


back_grounds_files = glob.glob('back_ground/*.jpg')
length = len(back_grounds_files)
back_grounds = []
for i in range (0,length):
    back_grounds.append(Image.open(back_grounds_files[i]))
    

#getting the datasets
datasets_files = glob.glob('dataset/*.jpg')
dataset = []
for i in range(0,len(datasets_files)):
    dataset.append(Image.open(datasets_files[i]))


#input_image = Image.open('PNG.png')
#bc_width , bc_height = img.size

DataOut =[['image_name','xmin','xmax','ymin','ymax','class_id']]

# the size of image we putting inside the data generator

i = 0
#preparing the image generator
for i in range(1,10):
    #getting a random background
    random_background = back_grounds[random.randint(0,len(back_grounds)-1)]
    bc_width , bc_height = random_background.size
    
    # getting a random input image from dataset
    random_input = dataset[random.randint(0,len(dataset)-1)]
    #input_width , input_height = random_input.size
    #random_size_for_input = random.randint(input_width/25 , input_width/4)
    #random_input = random_input.resize((int(random_size_for_input) , int(random_size_for_input/5)), Image.ANTIALIAS)
    random_input = random_input.resize((50,int(50/4)),Image.ANTIALIAS)
    #plt.imshow(random_input)
    #print(random_input.size)
    
    
    input_width , input_height = random_input.size
    
    #pick a random place for the image
    random_left = random.randint(0 ,bc_width - input_width-700)
    random_upper = random.randint(0, bc_height - input_width-700)
    right = random_left + input_width +700
    lower = random_upper + input_height + 700
    
    #crop the background image to place  and make a copy of it
    crop_rectangle = (random_left , random_upper , right , lower)
    new_image=  random_background.crop(crop_rectangle)
    new_image = new_image.resize((70,70),Image.ANTIALIAS)
    
    #generating random location for input image on background 
    new_image_width , new_image_height = new_image.size
    out_put_left = random.randint(0,70 - input_width )
    out_put_upper = random.randint(0,70 - input_height)
    new_image.paste(random_input,(out_put_left,out_put_upper))
    appendable = [str(i)+'.jpg' , out_put_left,out_put_left+input_width , out_put_upper , out_put_upper+input_height , 1]
    DataOut.append(appendable)
    new_image.save('images/'+str(i)+'.jpg',quality=95)
#    final_images[i] = new_image
#    plt.imshow(new_image)
    #Image._show(new_image)
    

#get image putput size 



DataOut = np.array(DataOut)

DataOut=pd.DataFrame(DataOut,index=None,columns=None)

DataOut.to_csv('train.csv',header=False,index=None)





#bc = image.imread('bird.jpg')
#bc2 = image.imread('image_tutorial-1.png')


#bcw = bc[:100 , : 100]

#bc.setflags(write=1)

#new_image = bc[:100 , :100 ] = bcw

#lum_img = plt.imshow(bc[:200,:100 , :])

#plt.imshow(new_image)
















