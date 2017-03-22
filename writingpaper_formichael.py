###########################################
#combine images to generate the writing paper
#
#
###########################################

import sys
import os
from PIL import Image

def readquestions(path):
	
	background = []
	illusts = []

	for filename in os.listdir(path):
		if '_blend.png' in filename:
			background.append(filename)
		
	obtain_latex(background, path)

def obtain_latex(background, path):

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
			first.append(format(l1,'.2f'))
			second.append(format(l2,'.2f'))
			third.append(format(l3, '.2f'))
			l1 = l1 - distance
		else:
			break
	c = 0
	d = 0
	e = 0
	with open(os.path.join(path,'commonpaper.txt'), 'w+') as f:
		for c in range(len(background)):
			f.write('\\thispagestyle{empty}\n')
			f.write('\\textblockorigin{0cm}{0cm}\n')
			f.write('\\begin{textblock*}{20cm}(-0.6cm, -0.1cm)\n')
			f.write('\drawline{{')
			f.write(','.join(first) + '}}{{')
			f.write(','.join(second) + '}}{{')
			f.write(','.join(third) + '}}{'+ os.path.join(path, background[c]) + '};\n')
			
			f.write('\end{textblock*}\n')
			f.write('\\null\\newpage\n')

def main():
	readquestions('/Users/lxb/Documents/yyc/latex/picsbackground/')

if __name__ == '__main__':
	main()


	


