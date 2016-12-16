#make the discontinue long vowel

import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
import os
import random

'''

fn = open("../wheels/highfreq.txt", 'r')

k = 0

line = fn.readline()
words = line.strip().split('\t')

fn.close()
	
print(len(words))

pattern = []



pattern.append('[ ]*[.]*[b-df-hj-np-tv-z][a][b-df-hj-npqstv-z][e]$') #find the patter a_e
pattern.append('[ ]*[.]*[b-df-hj-np-tv-z][i][b-df-hj-npqstv-z][e]$')  # find the pattern i_e
pattern.append('[ ]*[.]*[b-df-hj-np-tv-z][u][b-df-hj-npqstv-z][e]$')
pattern.append('[ ]*[.]*[b-df-hj-np-tv-z][o][b-df-hj-npqstv-z][e]$')

vow = ['a_e', 'i_e', 'u_e', 'o_e']

for i in range(0, len(pattern)):
	filename = '../d_vowel/'+vow[i]+'.txt'
	f = open(filename, 'w+')
	for item in words:
		if re.search(pattern[i], item) and len(item) <= M:
			f.write(item+'\n')
	f.close()
'''

N = 6 # how many words should serve
M = 7 # the longest word
D = 6 # the circle radius
extra = 5  #for saving some space

usedwords = []

for filename in os.listdir('../d_vowel/'):
	vowel = filename[0: filename.index('.')]
	usedwords = []
	f = open(os.path.join('../d_vowel/', filename), 'r+')
	for line in f.readlines():
		if line.strip() not in usedwords and len(line.strip())	> 0:
			usedwords.append(line.strip())
	f.close()


	T = int(len(usedwords)/N) # how many wheels
	Left = T % N  # how many left

	if Left > 0:
		for k in range(0, T-Left):
			temp = random.randint(0, N-1)
			usedwords.append(usedwords[temp])
		T += 1
	tt = 0  #count the words number in the usedowrds
	j = 0
	while tt < len(usedwords):
		axle1 = 1
		axle2 = axle1+D
		distance = axle1 + axle2
		out_radius = distance

		fig = plt.figure()
		plt.axis("equal")
		ax = fig.add_subplot(111)
		ax.axis('equal')

		i = 0
		for i in range(0, N):
			degree = i*math.pi*2/N
			if tt < len(usedwords):
				w2 = usedwords[tt]
				tt += 1
			else:
				break
			for z in range(0, len(w2)):
				flag = 0
				if z <= 2:
					temp = axle2*1.0*(M - z - 0.5)/M
				else:
					temp = axle2*1.0*(M - z - 1.5)/M
				tempx = temp*math.cos(degree)
				tempy = temp*math.sin(degree)

				if z != 0 and z!= 2:
					t1 = plt.text(tempx, tempy, w2[len(w2)-z-1], rotation = (360/N)*i, size=20, color='r')
				else:
					t1 = plt.text(tempx, tempy, " ", rotation = (360/N)*i, size=20, color='r')

				ax.add_artist(t1)

			plt.plot([0.4,0.4+0.5*math.cos(degree)],[0.4, 0.4+0.5*math.sin(degree)])

		ax.set_xlim(-1*(axle2+extra), (axle2+extra))
		ax.set_ylim(-1*(axle2+extra), (axle2+extra))
		circle1 = plt.Circle((0.4,0.4),radius = axle2+1, fc = 'none')
		ax.add_artist(circle1)
		filename = 'word'+str(j)+'_'+vowel+'.png'
		fig.savefig('../wheels/'+filename)
		#plt.show()

		plt.clf()

		# draw the cover

		fig1 = plt.figure()
		plt.axis("equal")
		ax1 = fig1.add_subplot(111)
		ax1.axis('equal')
		ax1.set_xlim(-1*(axle2+extra), (axle2+extra))
		ax1.set_ylim(-1*(axle2+extra), (axle2+extra))
		circle2 = plt.Circle((0.4,0.4),radius = axle2+1, fc = 'none')
		ax1.add_artist(circle2)
		vowels = vowel.split('_')
		print(vowels)
		for z in [0,2]:
			if z == 0:
				tempx = axle2*1.0*(M-z)/M
				tempy = 0
				plt.text(tempx, tempy, vowels[1], size=20, color = 'r')
			else:
				tempx = axle2*1.0*(M-z-0.5)/M
				tempy = 0
				plt.text(tempx, tempy, vowels[0], size=20, color = 'r')

		plt.plot([axle2-0.2, axle2-0.2],[1,-1],'r-')
		plt.plot([axle2*1.0*(M-2-1)/M, axle2*1.0*(M-2-1)/M],[1,-1],'r-')
		plt.plot([axle2*1.0*(M-2+0.5)/M, axle2*1.0*(M-2+0.5)/M],[1,-1],'r-')
		ax1.add_patch(
			patches.Rectangle((axle2*1/M,-1), (axle2), 2, edgecolor = 'r', fc = 'none')

		)
		for i in range(0, N):
			degree = i*math.pi*2/N
			plt.plot([0.4,0.4+0.5*math.cos(degree)],[0.4, 0.4+0.5*math.sin(degree)])

		save_filename = 'word'+str(j)+'_'+vowel+'_cover'+'.png'
		fig1.savefig('../wheels/'+save_filename)
		plt.clf()

		j += 1
		

	plt.close()







			






