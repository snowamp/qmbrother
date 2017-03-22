import numpy
from PIL import Image, ImageDraw
import os



def get_image(path):
	for filename in os.listdir(path):
		if 'jpg' in filename or 'jpeg' in filename or 'png' in filename:
			img = Image.open(filename)
			shape = img.size
			img2 = img.crop((10, 10, shape[0], shape[1]*0.7))
			index = filename.find('.')
			newname = filename[0:index] + '_crop' + filename[index:]
			img2.save(os.path.join(path,newname))


def main():
	get_image('/Users/lxb/Documents/yyc/scripts/booksproject/the_tale_of_peter_rabbit/')


if __name__ == '__main__':
	main()