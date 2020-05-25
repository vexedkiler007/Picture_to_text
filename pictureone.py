"""
12/2/2019

Plan: Create an image of zeros and ones from any image. 

000011110000
000011100000
000011000000
000010000000

1. Convert image to array of zeros and ones
	i) convert into black and white using cv2 (not gray scale)
	ii) convert into numpy array
	
2. specify how many ones and zeros fit per line 
	i)check if there are differences in all zeros and all ones 



12/3/2019

-numpy array might not work since there is limit per line 
-downscale image maybe..
-np.array(blackAndWhiteImage[0].tolist())
-using csv to save to text document

-0 and ones work but will look to see if .text can recognize other non alpha numeric symbols
-looking for way to get it to recognize emojis

"""



import numpy as np
import cv2
import csv
import emoji

#Loads original image 
originalImage = cv2.imread('mona.jpg')

#chnage to desired dimentions
originalImage = cv2.resize(originalImage, (200,200)) 

#Turns image into black and white
"""First turns it into gray scale, then uses a value where its considered 
black and white  a 'threshold'"""

###Gray
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

### Blackk and white

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

#Shows image to screen 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Determines width and length should be 184 x 274 pixel dimentions 
width = len(blackAndWhiteImage[0])
length = len(blackAndWhiteImage)

#creates a pythonlist from numpy array
ListOfPixels = blackAndWhiteImage.tolist()
NewListOfPixels = []

#replaces all 255 with ones 
for main_index, row in enumerate(ListOfPixels):
	temp_list = []
	#print(temp_list)
	
	for index, pixel in enumerate(row):
		if pixel == 255:
			row[index] == 1
			temp_list.append(emoji.emojize(":white_large_square:"))
		else:
			temp_list.append(emoji.emojize(":black_large_square:"))
		
		if index == (width-1):
			NewListOfPixels.append(temp_list)
			#print(temp_list)
			
print(NewListOfPixels)

with open('test.txt', 'w', encoding='utf-8') as f:
	csv.writer(f, delimiter=' ').writerows(NewListOfPixels)
#























