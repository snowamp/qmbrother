#####################################################################################
# Generate the answer paper for book questions
# Rainbow writing size: (108, 60), (358, 60), (147, 176), (375, 160), fontsize = 28
# 20 characters per line and totally 14 lines.
# for other circle line we can try to write in a circle area and cut as rectange
# attach on the page as circle or ellipse
# fontsize = 28, width per character 10pt, height 14pt
# Peter rabbit format
#####################################################################################

import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import math
import numpy as np

char_width = 24
char_height = 28
def read_questions():
	booksquestion = []
	with open('questions.txt', 'r') as f:
		for line in f.readlines():
			if len(line) < 3:
				continue
			booksquestion.append(line.strip())
	
	pics = [ ]
	path = '/Users/lxb/Documents/yyc/latex/pics/'
	for filename in os.listdir(path):
		if 'cloud' in filename or 'star' in filename:
			pics.append(filename)

	c = 0 # control the image used

	for item in booksquestion:
		x = get_radius(item)
		pic = pics[c]
		c += 1
		if c == len(pics):
			c = 0
		begins = []
		positions = []
		currentindex = 0
		height = 0.618 * x
		while currentindex < len(item):
			
			currentlength = 2 * x
			index = int(currentlength/char_width)
			if index + currentindex >= len(item):
				begins.append([-1 * x + 10, height])
				positions.append([currentindex, min(len(item),currentindex + index)])
				break
			else:
				while currentindex + index < len(item) and item[currentindex + index]!=' ':
					index += 1
				begins.append([-1 * x + 10, height])
				positions.append([currentindex, currentindex + index])
				currentindex += index
			height = height - 2*char_height
		generate(item, pic, begins, positions, x, path)


def get_radius(item):
	# 2*x/char_width + 0.618*2*x/2*char_height = length
	length = len(item)
	x = int(math.sqrt(2*length * char_width*char_height/(4*0.618)))+1
	return(x)

def generate(item, pic, begins, positions, x, path):
	font = ImageFont.truetype(os.path.join(path, 'Italic.ttf'), 28)
	im = Image.open(os.path.join(path,pic))
	index = pic.find('.')
	shape = im.size
	cropx = shape[0]/2
	cropy = shape[1]/2
	if 3 * x > shape[0] or 3 *0.618*x > shape[1]:
		ratio = max(int(3 * x/shape[0]), int(3*0.618*x/shape[1]))
		im1 = im.resize((shape[0] * ratio, shape[1] * ratio),PIL.Image.ANTIALIAS)
		#im1.save(os.path.join(path, pic[0:index]), "png")
		im = im1
		shape = im.size
		cropx = shape[0]/2
		cropy = shape[1]/2
	draw = ImageDraw.Draw(im)
	for i in range(len(begins)):
		point = begins[i]
		position = positions[i]
		print(pic)
		draw.text((cropx+point[0], cropy-point[1]), item[position[0]:position[1]],'black', font=font)
	index = pic.find('.')
	filename = item[0:3] + pic[0:index]+'_crop'+'.png'
	im.save(os.path.join(path, filename), 'png')


'''
def generate(item, pic, begins, positions, radius, path):

	font = ImageFont.truetype(os.path.join(path, 'BBC.ttf'), 28)
	im = Image.open(os.path.join(path,pic))
	shape = im.size
	cropx = shape[0]/2
	cropy = shape[1]/2
	draw = ImageDraw.Draw(im)
	for i in range(len(begins)):
		point = begins[i]
		position = positions[i]
		draw.text((cropx+point[0], cropy-point[1]), item[position[0]:position[1]], (255, 255, 255), font=font)

	im2 = im.crop((cropx-2*radius, cropy-radius, cropx+2*radius, cropy+radius))
	index = pic.find('.')
	filename = pic[0:index]+'_crop'+'.png'
	im2.save(os.path.join(path, filename), 'png')
'''
def main():
	read_questions()

if __name__ == '__main__':
	main()













