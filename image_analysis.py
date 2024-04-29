# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:08:10 2024

@author: amber
part code sourced from: https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv
"""

import cv2
import numpy as np
import os

directory = 'images'
radii = []

for filename in os.listdir(directory):
    #get filename
    f = os.path.join(directory, filename)
    #checking if f is a file
    if os.path.isfile(f):
        #apply mask to file
        img=cv2.imread(f)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # lower mask (0-10)
        lower_red = np.array([0,50,50])
        upper_red = np.array([50,255,255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
        # upper mask (170-180)
        lower_red = np.array([130,50,50])
        upper_red = np.array([230,255,255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
        #join the two masks
        mask = mask0+mask1
        #output mask as image, translate to greyscale
        output_hsv = img_hsv.copy()
        output_hsv[np.where(mask==0)] = 0
        rgb_img = cv2.cvtColor(output_hsv, cv2.COLOR_HSV2RGB)
        grey_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        #get brightnesses of all pixels in first row
        first_row = grey_img[0, :]
        bright_list = []
        #add all pixel indices where brightness is > 0 to a list.
        for i, value in enumerate(first_row):
            if value != 0:
                bright_list.append(i)
       #find the distance between the start of the first peak and end of the second peak in pixels
        pixel_distance = bright_list[len(bright_list) - 1] - bright_list[0]
        #use predetermined pixel scale of 150 px/cm to get a real diameter of the circle
    diameter = pixel_distance * 1/150
    #append the radius of each circle to a list
    radii.append(diameter / 2)
#print the list of radii for each image, going from IMG_4790 -> IMG_4805
print(radii)  
        