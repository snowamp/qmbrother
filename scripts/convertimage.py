#convert image to thumbnail

from wand.image import Image 
import os

path = '../princess/img/'

'''
for filename in os.listdir(path):
	index = filename.find('.')
	if len(filename) == index + 1:
		os.rename(os.path.join(path,filename), os.path.join(path,filename+'jpg'))
'''

for filename in os.listdir(path):
	index = filename.find('.')
	if filename[index+1:] in ('jpeg', 'jpg', 'png') and 'thumbnail' not in filename:
		try:
			with Image(filename = os.path.join(path, filename)) as img:
				if img.size[0] > 400 and img.size[1] > 400:
					img.resize(60, 60)
					tmp =filename[0:index] + '_' +'thumbnail' + '.'+filename[index+1:]
					img.save(filename = os.path.join(path, tmp))
		except:
			print(filename)


