#################################
#Basic idea:
# word is inserted into table by sequence of horizon and vertical 
# line or column is selected by probability of left space number
# The first step is to select line or column and put into the free space (more space more probability)
# The second step is to try to compact the word letter (share the letter as most as possible)
#################################

import sys
import numpy as np 
import random
import os

horizonNumber = 14
vertialNumber = 14

def words_input(words, picture,path):
	#words = ['habit', 'review', 'frequently', 'talent', 'productivity', 'constant', 'something', 'guess', 
	#'experience', 'experiment', 'simplicity', 'letter', 'most', 'compact']

	words.sort(key = lambda s:len(s), reverse = True)

	words_arrange(words, picture, path)

def obtain_index(num, option):
	if option == 'h':
		temp = int(num / vertialNumber)
	elif option == 'v':
		temp = num % vertialNumber
	else:
		print('mistake')
		temp = -1
	return(temp)

def words_arrange(words,  picture, path):
	candidate = []
	for i in range(horizonNumber * vertialNumber):
		candidate.append(i)
	letterMatrix = []
	for i in range(horizonNumber):
		temp = []
		for j in range(vertialNumber):
			temp.append('*')
		letterMatrix.append(temp)

	missed = []
	flag = -1
	for word in words:
		flag = flag * (-1)
		sign = 1
		count = 0
		while sign:
			count += 1
			if flag == 1 and count > 14:
				missed.append(word)
				break
			else:
				if flag == -1 and count > 9:
					missed.append(word)
					break
			selected = random.choice(candidate)
			hor = obtain_index(selected, 'h')
			ver = obtain_index(selected, 'v')
			coe = -1
			if flag == 1:
				coe  = hor
			else:
				coe = ver

			if letterMatrix[hor][ver] == '*':
				if put(word, letterMatrix, candidate, flag, hor, ver):
					sign = 0
				else:
					if putfromzero(word, letterMatrix, candidate,flag, coe):
						sign = 0
					else:
						continue
			else:
				if putfromzero(word, letterMatrix, candidate, flag, coe):
					sign = 0
				else:
					continue
	if len(missed) > 0:
		for word in missed:
			found = 0
			for i in range(0, horizonNumber):
				if putfromzero(word, letterMatrix, candidate, 1, i):
					found = 1
					missed.remove(word)
					break
			if found == 0:
				for j in range(0, vertialNumber):
					if putfromzero(word, letterMatrix, candidate, -1, j):
						found = 1
						missed.remove(word)
						break
	for word in missed:
		words.remove(word)



	words_output(letterMatrix, words, picture, path)
	#print(missed)


def put(word, letterMatrix, candidate, flag, hor, ver):
	if flag == 1:
		for i in range(0, len(word)):
			if (ver + i < vertialNumber and letterMatrix[hor][ver + i] != '*' and letterMatrix[hor][ver + i] != word[i]) or (ver+i >=vertialNumber):
				return(False)
		for i in range(0, len(word)):
			if letterMatrix[hor][ver + i] == '*':
				letterMatrix[hor][ver + i] = word[i]
				temp = hor * vertialNumber + ver + i
				candidate.remove(temp)
		return(True)
	else:
		for i in range(0, len(word)):
			if (hor+i < horizonNumber and letterMatrix[hor + i][ver] != '*' and letterMatrix[hor + i][ver] != word[i]) or (hor + i >= horizonNumber):
				return(False)
		for i in range(0, len(word)):
			if letterMatrix[hor + i][ver] == '*':
				letterMatrix[hor + i][ver] = word[i]
				temp = (hor + i) * vertialNumber + ver
				candidate.remove(temp)
				
		return(True)

# check if there are shared letter and then from 0-1 check put indpendently 

def putfromzero(word, letterMatrix, candidate, flag, coe):

	if flag == 1:
		for i in range(0, vertialNumber):
			if letterMatrix[coe][i] != '*':
				index = word.find(str(letterMatrix[coe][i]))
				if index >= 0 and i > index and put(word, letterMatrix, candidate, flag,coe, i - index):
						return(True)
		
		for i in range(vertialNumber-1, len(word)-1, -1):
			if letterMatrix[coe][i] == '*':
				if put(word, letterMatrix, candidate, flag, coe, i - len(word)):
					return(True)
	else:
		for i in range(0,horizonNumber):
			if letterMatrix[i][coe] != '*':
				index = word.find(str(letterMatrix[i][coe]))
				if index >= 0 and i > index and put(word, letterMatrix, candidate, flag, i - index, coe):
					return(True)

		for i in range(horizonNumber-1, len(word)-1, -1):
			if letterMatrix[i][coe] == '*':
				if put(word, letterMatrix, candidate,flag, i - len(word), coe):
					return(True)

	return(False)

def words_output(letterMatrix, words, picture,path):
	all_letters = 'abcdefghijklmnopqrstuvwxyz'
	alpha = []
	for char in all_letters:
		alpha.append(char)
	with open(os.path.join(path,'wordhunt.txt'), 'a') as f:
		f.write('\\begin{tikzpicture}\n')
		#f.write('\\textblockorigin{0cm}{0cm}' + '\n')
		f.write('\draw(7,18) node{WORDHUNT};\n')
		f.write('\\node(fig2) at(15,1){\includegraphics[width=1cm]{/Users/lxb/Documents/yyc/latex/gmbrothers.png}};\n')
		f.write('\\node(fig1) at(15,18){\includegraphics[width=3cm]{'+ picture+'}};\n')
		dis = 2 #move the table below
		for i in range(0, horizonNumber):
			for j in range(0, vertialNumber):

				f.write('\draw(' + format(i, '.2f') + ',' + format(15-j, '.2f') + ')+(-.5, -.5) rectangle++(.5, .5);' + '\n')
				f.write('\draw(' + format(i,'.2f') + ',' + format(15-j,'.2f') + ') node{')
				if letterMatrix[i][j] == '*':
					f.write(random.choice(alpha).upper() + '};\n')
				else:
					f.write(str(letterMatrix[i][j]).upper() + '};\n')
			f.write('\n')

		x = vertialNumber + 0.5
		y = dis + 1.5
		for word in words:
			f.write('\draw(' + format(x,'.2f')+','+ format(y,'.2f') + ')[text width = 2cm, anchor = west] node{' + word.upper() + '};\n')
			y += 0.8


		f.write('\end{tikzpicture}\n')
		f.write('\\null\\newpage\n')

def main():
	path = '/Users/lxb/Documents/yyc/scripts/booksproject/the_tale_of_peter_rabbit/'
	words = []
	with open(os.path.join(path,'wordlist.txt'), 'r') as f:
		for line in f.readlines():
			splits = line.strip().split('\t')
			if len(splits[0]) > 1:
				words.append(splits[0])

	pictures = []
	for pics in os.listdir(path):
		if ('png' in pics or 'jpg' in pics or 'jpeg' in pics) and '_crop' in pics:
			pictures.append(pics)
	total = 15
	i = 0
	
	c = 0

	while i < len(words):
		j = min(i+15, len(words))

		words_input(words[i:j], path+pictures[c], path)
		c += 1
		if c == len(pictures):
			c = 0
		i = j

if __name__ == '__main__':
	main()











	




