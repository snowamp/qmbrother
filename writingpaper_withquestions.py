###########################################
#combine images to generate the writing paper
#
#
###########################################

import sys
import os
from PIL import Image

def readquestions(path):
	questions = []
	with open(os.path.join(path, 'questions.txt'), 'r') as f:
		for line in f.readlines():
			questions.append(line.strip())
	background = []
	illusts = []

	for filename in os.listdir(path):
		if '_blend.png' in filename:
			background.append(filename)
		
	obtain_latex(questions, background, path)

def obtain_latex(questions, background, path):

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
	e = 0
	with open(os.path.join(path,'commonpaper_snow.txt'), 'w+') as f:
		for c in range(len(questions)):
			f.write('\\thispagestyle{empty}\n')
			f.write('\\textblockorigin{0cm}{0cm}\n')
			f.write('\\begin{textblock*}{20cm}(-0.6cm, -0.1cm)\n')
			f.write('\drawline{{')
			f.write(','.join(first) + '}}{{')
			f.write(','.join(second) + '}}{{')
			f.write(','.join(third) + '}}{'+ os.path.join(path, background[d]) + '}{'+questions[c]+'};\n')
			d += 1
			if d >= len(background):
				d = 0
			
			f.write('\end{textblock*}\n')
			f.write('\\null\\newpage\n')
		print("Done")

def main():
	readquestions('/Users/lxb/Documents/yyc/scripts/booksproject/snow/')

if __name__ == '__main__':
	main()


	


