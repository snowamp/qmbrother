###########################################
#combine images to generate the writing paper
#
#
###########################################

import sys
import os
from PIL import Image

def obtain_latex(path):

	beginline_h = -2
	lastline_h = -26

	beginline_v = 0.6
	lastline_v = 19


	
	insidedistance = 0.6

	horizon = []
	vertical = []
	
	l1 = beginline_h
	while True:
		if l1 > lastline_h:
			horizon.append(format(l1,'.2f'))
			l1 = l1 - insidedistance
		else:
			break
	l2 = beginline_v
	while True:
		if l2 < lastline_v:
			vertical.append(format(l2, '.2f'))
			l2 = l2 + insidedistance
		else:
			break

	with open(os.path.join(path,'coordinate.txt'), 'w+') as f:
		
		f.write('\\thispagestyle{empty}\n')
		f.write('\\textblockorigin{0cm}{0cm}\n')
		f.write('\\begin{textblock*}{20cm}(-0.6cm, -0.1cm)\n')
		f.write('\drawline{{')
		f.write(','.join(horizon) + '}}{{')
		f.write(','.join(vertical) + '}};\n')
			
		f.write('\end{textblock*}\n')
		f.write('\\null\\newpage\n')

def main():
	obtain_latex('/Users/lxb/Documents/yyc/scripts/booksproject/maths/')

if __name__ == '__main__':
	main()


	


