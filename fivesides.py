##########################################
# Draw the five sides pythongon
##########################################

import numpy as np 
import os
import math

def get_alpha(r, radius, alpha, beta): # r the original radius, radius is the new radius, alpha is the x angle, beta is the new center angle
	center = [radius*np.cos(beta), radius*np.sin(beta)]
	vector = np.array([r * np.cos(alpha), r * np.sin(alpha)]) - np.array(center)
	mod = np.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
	cos = vector[0]/mod
	new_alpha = np.arccos(cos)
	if vector[1] < 0:
		new_alpha = -1 * new_alpha
	return(new_alpha)


def obtain_points(r, path):
	angles = []
	alpha = 2 * np.pi/10

	first = -1*np.pi/2 - alpha
	angles.append(first)
	for i in range(1, 5):
		first += 2 * alpha
		angles.append(first)

	radius = r/(2*np.cos(alpha))

	arcs = []

	for point in angles:
		beta = point + alpha
		begin_alpha = get_alpha(r, radius, point, beta)
		end_alpha = begin_alpha + 4 * alpha
		arcs.append((begin_alpha, end_alpha))

	words = []
	pics = []
	with open('/Users/lxb/Documents/yyc/scripts/booksproject/snow/snow.txt', 'r') as f:
		for line in f.readlines():
			splits = line.strip().split('\t')
			if len(splits) < 2:
				continue
			words.append([splits[0], splits[-1]])

	picpath = '/Users/lxb/Documents/yyc/scripts/booksproject/snow/'
	for filename in os.listdir(picpath):
		if 'jpg' in filename or 'png' in filename or 'jpeg' in filename:
			pics.append(os.path.join(picpath, filename))
 
	output(angles, arcs, words, pics, path, r, radius)

def output(angles, arcs, words, pics, path, r, radius):

	textblockpos = [(6.5, 8), (14, 18)]
	c = 0
	w = 0

	with open(os.path.join(path, 'fivesides.txt'), 'w+') as f:
		for i in range(len(words)):
			if i % 2 == 0:
				f.write('\\null\\newpage\n')
				f.write('\\textblockorigin{0cm}{0cm}\n')
				pos = 0
			else:
				pos = 1
			f.write('\\begin{textblock*}{10cm}('+str(textblockpos[pos][0]) + 'cm,' + str(textblockpos[pos][1]) + 'cm)\n')
			f.write('\\begin{tikzpicture}[overlay]\n')
			f.write('\draw')
			for point in angles:
				f.write('(' + format(r*np.cos(point), '.2f') + ',' + format(r*np.sin(point), '.2f') + ')')
				f.write(' --')
			f.write('cycle;\n')
			f.write('\\filldraw[color = blue!10]')
			for point in angles:
				f.write('(' + format(r*np.cos(point), '.2f') + ',' + format(r*np.sin(point), '.2f') + ')')
				f.write(' --')
			f.write('cycle;\n')


			for i in range(len(angles)):
				f.write('\draw(')
				f.write(format(r*np.cos(angles[i]), '.2f') + ',' + format(r*np.sin(angles[i]), '.2f') + ')')
				f.write(' arc(')
				begin = arcs[i][0]/(2*np.pi) * 360
				end = arcs[i][1]/(2*np.pi) * 360

				f.write(format(begin, '.2f') + ':' + format(end,'.2f') + ':' + format(radius, '.2f') + ');\n')
			f.write('\drawcontent{'+ str(-1+pos*2) + '}{3}{'+pics[c]+'}{'+words[w][0]+'}{'+words[w][1]+'};\n')
			f.write('\end{tikzpicture}\n')
			f.write('\end{textblock*}\n')
			c += 1
			if c == len(pics):
				c = 0
			w += 1
			if w == len(words):
				w = 0

def main():
	obtain_points(5, '/Users/lxb/Documents/yyc/latex/')

if __name__ == '__main__':
	main()









