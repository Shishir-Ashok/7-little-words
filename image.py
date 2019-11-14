# import the necessary packages
from PIL import Image
from itertools import permutations
import pytesseract
import argparse
import time
import json
import cv2
import os
import re

 
start_time = time.time()
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="Type of preprocessing to be done (thresh <default> | blur)")
ap.add_argument("-s", "--showoutput", action="store_true",
	help="Display output image files")
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

text = pytesseract.image_to_string(Image.open(filename), lang='eng', config='A-Z -pms 7')
os.remove(filename)
print(text)
# print("\n\n",text[0])
# print("\nText[1]",text[1],text[2],type(text))

listOfText = text.split()


perms = []
for i in range(2,4):
	perms.append([''.join(p) for p in permutations(listOfText,i)])

perms = sum(perms,[])
print(perms[0],perms[1],perms[4],perms[88],perms[888])
print("Length of perms : ",len(perms))
print("Length of set(perms) : ",len(set(perms)))
print(listOfText)

final = []
# file = open('words.txt')
# lines = file.read()

jd = json.loads(open('words copy.json').read())

for i in perms:
	# if (re.findall('\\b{}\\b'.format(i), lines)):
	# if (re.search('\\b{}\\b'.format(i), lines)):
	if(i in jd):
		final.append(i)

print("The result : \n",final)
# show the output images
print("--- %s seconds ---" % (time.time() - start_time))
if args.showoutput:
	cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	cv2.waitKey(0)