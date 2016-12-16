# generate cover img for the pic books and revise the folder names
from wand.image import Image 
import os

path = '../k9/titlelist_'
path1 = '../k9_img/'
name = ['children.txt', 'toddler.txt', 'young_adult.txt']
name1 = ['children', 'toddler', 'young_adult']
itemlist = []
foldername = []
children = []
toddler = []
young_adult = []

def generate(newpath):
	with Image(filename = os.path.join(newpath, "0.png")) as img:		
		img.resize(88, 66)
		tmp = "cover.png"
		img.save(filename = os.path.join(newpath, tmp))


for i in range(len(name)):
	with open(path+name[i], 'r') as f:
		splits = f.readline().split('\t')
		for item in splits:
			index = item.find('.')
			filefolder = item[0:index]
			if i == 0:
				children.append(filefolder)
			elif i == 1:
				toddler.append(filefolder)
			elif i == 2:
				young_adult.append(filefolder)
			else:
				continue
'''
for filename in os.listdir('../k9_img/'):
	if filename in itemlist:
		newpath = '../k9_img/' + filename +'/'
		generate(newpath)

'''


for filename in os.listdir(path1):
	if filename in children:
		os.rename(os.path.join(path1,filename), os.path.join(path1,"children_"+filename))
	elif filename in toddler:
		os.rename(os.path.join(path1,filename), os.path.join(path1,"toddler_"+ filename))
	elif filename in young_adult:
		os.rename(os.path.join(path1,filename), os.path.join(path1,"young_adult_" + filename))
	else:
		continue


