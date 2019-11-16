#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2019, Shishir Ashok
# All rights reserved.

# import the necessary packages
from PIL import Image
from itertools import permutations
import pytesseract
import argparse
import requests
import enchant
import time
import json
import cv2
import os
import re


start_time = time.time()

def findmeaning(finallist):
	data = json.load(open("dictionary.json"))
	for word in finallist:
		try:
			meaningslist.append(data[word.lower()])
		except KeyError:
			meaningslist.append("Sorry, no meaning found")



dictionary = enchant.Dict("en_US")


pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
ap.add_argument("-i", "--image", required=True,
	help="-Usage : /Path/to/input/image")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="-Usage : thresh | blur")
ap.add_argument("-s", "--show", action="store_true",
	help="-Display image files (2) (Before and after preprocessing)")

args = ap.parse_args()

# load the example image and convert it to grayscale
image = cv2.imread(args.image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
if args.preprocess == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args.preprocess == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

text = pytesseract.image_to_string(Image.open(filename), lang='eng')
os.remove(filename)


listOfText = text.split()
# listOfText = ['OR','RUN','JAU','SE','AS','DEO','CE','AR','IG','NTI','INV','LY','PAN','OFF','BOO','TI','ATE','CA','VI','TTA']


perms = []
for i in range(2,5):
	perms.append([''.join(p) for p in permutations(listOfText,i)])

perms = sum(perms,[])


final = []
meaningslist = []
for i in perms:
	if(dictionary.check(i)):
		final.append(i)
final.sort(key=len)
findmeaning(final)

if args.verbose:
	print("Data from the image : ",text)
	print("Length of perms : ",len(perms))
	print("Number of words found : ",len(final))
	
	print("List of words based on the number of letters :")
	for word in final:
		print(word, end=", ")
	print("DEFINITIONS")
	print(final)
	for i in range(len(final)):
		print("{} \n {}".format(final[i],meaningslist[i]))



if args.quiet:
	print("List of words :")
	for word in final:
		print(word, end=", ")

# show the output images
if args.show:
	cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	cv2.waitKey(0)

print("Processing time --- %s seconds ---" % (time.time() - start_time))