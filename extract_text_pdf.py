# extract the text from pdf text file
# from wand.image import Image
# Converting first page into JPG
#with Image(filename="/thumbnail.pdf[0]") as img:
#    img.save(filename="/temp.jpg")
#

'''
from tesseract import image_to_string

print image_to_string(Image.open('test.png'))
print image_to_string(Image.open('test-english.jpg'), lang='eng')

import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

'''

from PyPDF2 import PdfFileReader
from wand.image import Image
from PIL import Image as img
import os, sys, re
import pytesseract

path = "/Users/yanchunyang/Documents/highschools/k9/"

for filename in os.listdir(path):

	if '.pdf' in filename and bool(re.search(re.compile('^[1-9]'), filename)):
		input1 = PdfFileReader(open(os.path.join(path, filename), "rb"))
		index = filename.index('.')
		ordernumber = filename[:index]
		outpath = "/Users/yanchunyang/Documents/highschools/k9_img/" + str(ordernumber)+'/'

		if not os.path.isdir(outpath):
			os.mkdir(outpath)

		totalpages = input1.getNumPages()
		openfile = os.path.join(path, filename)
		for i in range(totalpages):
			with Image(filename = openfile+'['+str(i)+"]") as img_1:
				img_1.save(filename = os.path.join(outpath, str(i)+'.png'))
			
'''
for filename in os.listdir(path):
	print(filename)
	index = filename.index('.')
	ordernumber = filename[0:index]
	pic = img.open(os.path.join(path, filename))
	pic = pic.resize((3600, 3600))
	text = pytesseract.image_to_string(pic)
	textInfo[ordernumber] = text


for key in textInfo.keys():
	print(key)
	print(textInfo[key])
	print("-----------------")


textInfo = {}

for i in range(totalpages):
	temppage = input1.getPage(i)
	text = temppage.extractText()
	if len(text) == 0 or (not bool(re.search(re.compile('[a-zA-Z'), text))):
		with Image(filename = openfile+'['+str(i)+"]") as img_1:
			img_1.save(filename = os.path.join(path, str(i)+'.png'))
	else:
		textInfo[str(i)] = text

for filename in os.listdir(path):
	print(filename)
	index = filename.index('.')
	ordernumber = filename[0:index]
	pic = img.open(os.path.join(path, filename))
	pic = pic.resize((3600, 3600))
	text = pytesseract.image_to_string(pic)
	textInfo[ordernumber] = text
'''









