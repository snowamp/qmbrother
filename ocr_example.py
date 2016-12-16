#this code to organize the filename, class and english title for the free picture books

import os
import sys
from PIL import Image
import pytesseract
from collections import defaultdict
import pandas as pd
from shutil import copyfile


path = '/Users/yanchunyang/Documents/highschools/k9_img/yang/'
folder = []
filetype = {}
english_title = {}

for foldername in os.listdir(path):
	if 'DS_Store' not in foldername and '_' in foldername:
		folder.append(foldername)


for subpath in folder:
	'''
	if 'children' in subpath:
		filetype[subpath] = 2
	elif 'toddler' in subpath:
		filetype[subpath] = 1
	elif 'young' in subpath:
		filetype[subpath] = 3
	'''

	tmp = path + subpath + '/'
	tmp1 = '/Users/yanchunyang/Documents/highschools/k9_img/cover/'

	copyfile(os.path.join(tmp, '0.png'), os.path.join(tmp1, subpath+'_'+'0.png') )

	'''
	try:
		sub_string = pytesseract.image_to_string(Image.open(os.path.join(tmp, '0.png')))
	except:
		sub_string = " "
	english_title[subpath] = sub_string

with open(os.path.join(path, 'result.txt'), 'w') as f:
	for key in folder:
		f.write(key)
		f.write('\t')
		f.write(str(filetype[key]))
		f.write('\t')
		f.write('\n')


df1 = pd.DataFrame({'folder_name':folder, 'filetype':filetype, 'englishtitle': english_title}, index = range(len(folder)))

df1.to_csv(path+'summary.csv', sep = ',')
'''









