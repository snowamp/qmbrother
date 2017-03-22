
"""
make card latex
Latex model is word.tex in labelmodel folder
"""

import sys
import os
import numpy as np 
import math 

def obtain_star_dataset(totalsides, inner_radius, out_radius):
	dataset = []
	alpha = np.pi / totalsides 
	current = np.pi / 2
	for i in range(0, 2 * totalsides):
		if i % 2 == 0:
			dataset.append((out_radius * np.cos(current), out_radius * np.sin(current)))
		else:
			dataset.append((inner_radius * np.cos(current), inner_radius * np.sin(current)))

	return(dataset)

def obtain_flower_dataset(totalsides, inner_radius , out_radius ):
	dataset = []
	#inner_radius is the height to polygon, not the inner radius of outside circle
	alpha = np.pi / totalsides
	# l is the length of half of polygon side
	l = inner_radius * np.tan(alpha)
	# h is the flower height to polygon side
	h = out_radius - inner_radius

	r = (h * h + l * l) / (2 * h)

	theta = np.arcsin(l / r)
	# polygon radius length
	p_r = inner_radius / np.cos(alpha)

	#center length is the petal's center position to center of flower

	center_length = h + inner_radius - r 

	current = np.pi / 2 - alpha

	for i in range(0, totalsides):
		temp = []

		point = np.array([p_r * np.cos(current), p_r * np.sin(current)])

		t1 = np.array([center_length * np.cos(current + alpha), center_length * np.sin(current + alpha)])

		vector = point - t1 

		beta = np.arccos(vector[0]/ math.sqrt(vector[0] * vector[0] + vector[1] * vector[1] ))

		if vector[1] < 0:
			beta = 2 * np.pi - beta

		temp.append([point[0], point[1], beta * 180 / np.pi, (beta + 2 * theta) * 180 / np.pi, r])

		dataset.append(temp)

	return(dataset)

	

def draw_star(dataset, color):
	returnstring = '\\filldraw[color=' + color + ']'
	for point in dataset:
		returnstring += '(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
	returnstring += 'cycle;\n'

	return(returnstring)



def draw_flower(dataset, color):
	returnstring = ''
	for point in dataset:
		returnstring += '\\filldraw[color=' + color + '](' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') arc ('
		returnstring += format(point[2], '.2f') + ':' + format(point[3], '.2f') + ':' + format(point[4], '.2f') + ');\n'

	return(returnstring)

def draw_circle(radius, color):
	returnstring = '\\filldraw[fill=' + color + '] (0,0) circle [radius=' + str(r) + 'cm];\n'
	return(returnstring)

def draw_square(width, height, color):
	returnstring = '\\node (rect) at (0, 0) [draw, minimum width ='
	returnstring += str(width) + 'cm, minimum height=' + str(height) + 'cm, fill=' + color + ', rounded corners=15pt]{};\n'
	return



def readfile(filename, picpath, type):
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



	framewidth = 5
	
	row_num = int(18 / 5)

	col_num = int(24 / 5)

	row_dis = int(18 / row_num)

	col_dis = int(26 / col_num)

	totalnumber = row_num * col_num 

	colors = ['red!10', 'blue!10', 'yellow!10', 'green!10', 'pink!10', 'orange!10']

	drawtype = ['circle', 'square', 'star', 'flower']

	draw = drawtype[type]

	p = 0
	c = 0
	
	current_num = 0

	begin = [2.5, 2.5 - col_dis]



	if draw == 'star':
		dataset = obtain_star_dataset(totalsides = 5, inner_radius = 3.5, out_radius = 5)

	if draw == 'flower':
		dataset = obtain_flower_dataset(totalsides, inner_radius = 3.5, out_radius = 5)

	with open('mkcards.txt', 'w+') as g:
		
		for i in range(0, len(words)):

			if draw == 'star':
				specialstring = draw_star(dataset, color=colors[c])

			if draw == 'flower':
				specialstring = draw_flower(dataset, color=colors[c])

			if draw == 'circle':
				specialstring = draw_circle(radius= 5, color =colors[c])

			if draw == 'square':
				specialstring = draw_square(width = 8, height = 6, color=colors[c])



			if i % totalnumber == 0:
				if i > 0:
					g.write('\\null\\newpage\n')
					begin = [2.5, 2.5 - col_dis]
				g.write('\\textblockorigin{1cm}{1cm}\n')
			if i % row_num == 0:
				begin[0] = 2.5
				begin[1] += col_dis
				
			else:
				begin[0] += row_dis

			g.write('\\begin{textblock*}{' + str(framewidth) + 'cm}('+ str(begin[0]) + 'cm,'+ str(begin[1]) + 'cm)\n')
			g.write('\\begin{tikzpicture}[overlay]\n')
			g.write(specialstring)
			g.write('\drawothers{'+words[i][0] + '}{'+ words[i][1] + '}{' +os.path.join(picpath, pictures[p]) + '}\n')
			
			g.write('\end{tikzpicture}\n')
			g.write('\end{textblock*}\n')
			p += 1
			if p == len(pictures):
				p = 0
			c += 1
			if c== len(colors):
				c = 0
			
			
			
			

def main():
	readfile('words.txt', '/Users/lxb/Documents/yyc/scripts/booksproject/ifgiveamouseacookie/', 2)

if __name__ == '__main__':
	main()

