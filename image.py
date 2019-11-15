# import the necessary packages
from PIL import Image
from itertools import permutations
import pytesseract
import argparse
import requests
import enchant
import time
import cv2
import os
import re


def findmeaning():

	app_id = '<app_id>'
	app_key = '<app_key>'
	language = 'en'

	for i in final:
		url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + i.lower()
		#url Normalized frequency
		urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + i.lower()
		r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
		response = r.json()
		print(i.upper(),":\n")
		for n in range (10):
			try:
				print("[{}]".format(n), response['results'][n]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
			except IndexError:
				break
			except KeyError:
				continue

 
start_time = time.time()




dictionary = enchant.Dict("en_US")


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

text = pytesseract.image_to_string(Image.open(filename), lang='eng')
os.remove(filename)
print(text)

listOfText = text.split()
# listOfText = ['OR','RUN','JAU','SE','AS','DEO','CE','AR','IG','NTI','INV','LY','PAN','OFF','BOO','TI','ATE','CA','VI','TTA']


perms = []
for i in range(2,5):
	perms.append([''.join(p) for p in permutations(listOfText,i)])

perms = sum(perms,[])
print("Length of perms : ",len(perms))

final = []

for i in perms:
	if(dictionary.check(i)):
		final.append(i)
print("LIST : ",listOfText)
final.sort(key=len)
print("The result : \n",final)

# word_id = 'Shanghai'






# show the output images
print("--- %s seconds ---" % (time.time() - start_time))
if args.showoutput:
	cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	cv2.waitKey(0)