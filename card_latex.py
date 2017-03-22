
###############################
#make card latex
#It is square
################################

import sys
import os


def readfile(filename, picpath):
	words = []
	with open(os.path.join(picpath,filename), 'r') as f:
		for line in f.readlines():
			splits = line.strip().split('\t')
			if len(splits[0]) > 1:
				words.append([splits[0], splits[-1]])

	pictures = []
	for pics in os.listdir(picpath):
		#if ('png' in pics or 'jpg' in pics or 'jpeg' in pics) and '_crop' in pics:
		if 'png' in pics or 'jpg' in pics or 'jpeg' in pics:
			pictures.append(pics)



	framewidth = 8
	x = 4
	y = 5
	h_dis = 10
	v_dis = 7
	row = 0
	colors = ['red!10', 'blue!10', 'yellow!10', 'green!10', 'pink!10', 'orange!10']
	p = 0
	c = 0
	print(len(words))
	print(len(pictures))
	with open(os.path.join(picpath, 'mkcards.txt'), 'w+') as g:
		g.write('\\textblockorigin{1cm}{1cm}\n')

		for i in range(0, len(words)):
			
			if i % 2 == 1:
				x = 14
			else:
				x = 5
			g.write('\\begin{textblock*}{' + str(framewidth) + 'cm}('+ str(x) + 'cm,'+ str(y) + 'cm)\n')
			g.write('\Cloud{0}{0}{'+words[i][0] + '}{'+os.path.join(picpath, pictures[p]) + '}{'+words[i][1]+'}{'+ colors[c]+'}\n')
			g.write('\end{textblock*}\n')
			p += 1
			if p == len(pictures):
				p = 0
			c += 1
			if c== len(colors):
				c = 0
			if i%2 == 1:
				y += v_dis
			if i % 6 == 5:
				g.write('\\null\\newpage\n')
				y = 5
			
			

def main():
	readfile('wordlist.txt', '/Users/lxb/Documents/yyc/scripts/booksproject/gusistree/pics/')

if __name__ == '__main__':
	main()

