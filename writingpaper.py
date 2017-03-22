###########################################
#combine images to generate the writing paper
#
#
###########################################

import sys
import os
from PIL import Image


question_path = '/Users/lxb/Documents/yyc/latex/pics/'
image_path = '/Users/lxb/Documents/yyc/scripts/booksproject/the_tale_of_peter_rabbit/'

question_images = []
images = []

for filename in os.listdir(question_path):
	if '_crop' in filename:
		question_images.append(filename)

for filename in os.listdir(image_path):
	if '_crop' in filename:
		images.append(filename)

beginline = -3
lastline = -26

distance = 1.8
insidedistance = 0.6

first = []
second = []
third = []
l1 = beginline
while True:
	l2 = l1 - 0.6
	l3 = l2 - 0.6
	if l3 > lastline:
		first.append(str(l1))
		second.append(str(l2))
		third.append(str(l3))
		l1 = l1 - distance
	else:
		break
c = 0
d = 0
with open('commonpaper_format.txt', 'w+') as f:
	for c in range(len(question_images)):
		f.write('\\thispagestyle{empty}\n')
		f.write('\\textblockorigin{0cm}{0cm}\n')
		f.write('\\begin{textblock*}{20cm}(0cm, 0cm)\n')
		f.write('\\begin{tikzpicture}\n')
		f.write('\\node(txt) at (16,0)[fontscale=0.4]{GM Brothers@2017};\n')
		f.write('\drawline{{')
		f.write(','.join(first) + '}}{{')
		f.write(','.join(second) + '}}{{')
		f.write(','.join(third) + '}};\n')
		f.write('\\node(fig) at (3,-3){\includegraphics[width=8cm]{' + os.path.join(question_path, question_images[c]) + '}};\n')
		f.write('\\node(fig1) at (16,-23){\includegraphics[width = 6cm]{' + os.path.join(image_path, images[d]) + '}};\n' )
		d += 1
		if d >= len(images):
			d = 0
		f.write('\end{tikzpicture}\n')
		f.write('\end{textblock*}\n')
		f.write('\\null\\newpage\n')


	


