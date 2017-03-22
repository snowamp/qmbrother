##########################################################
# Combine questions with pictures
# the writing paper questions are the title on the paper
# Refer the paper for gusistree
##########################################################

import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import math
import numpy as np


def obtain_files(path):
	images = []
	for filename in os.listdir(path):
		if 'png' in filename or 'jpg' in filename or 'jpeg' in filename:
			images.append(filename)

	for item in images:
		im = Image.open(os.path.join(path,item))
		shape = im.size
		newheight = int(shape[1]*2.0/3)
		newwidth = int(shape[0]/6.0)
		im1 = im.crop((newwidth, 0, shape[0],newheight))
		if newheight > 400:
			width = int(shape[0]/(newheight/400.0))
			im1 = im1.resize((width, 400))

		index = item.find('.')
		illustration_image_name = item[:index] + '_illust'+'.png'
		im1.save(os.path.join(path,illustration_image_name), "png")

		im2 = im.crop((0, 10, shape[0], newheight))
		if newheight > 400:
			ratio = newheight/400.0
			width = int(shape[0]*2.0/ratio)
			im2 = im2.resize((width, 400))

		title_image_name = item[:index] + '_title'+'.png'
		im2.save(os.path.join(path, title_image_name), "png")


def main():
	obtain_files('/Users/lxb/Documents/yyc/scripts/booksproject/gusistree/')

if __name__ == '__main__':
	main()




