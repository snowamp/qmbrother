#for ee,ai, ay, igh other continue vowel

import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
import pandas as pd
import os
import random


'''
fn = open("../wheels/highfreq.txt", 'r')

k = 0

line = fn.readline()
words = line.strip().split('\t')
	
fn.close()

print(words[0:10])

print(len(words))

#pattern = []

#pat = ['ee', 'ea', 'ai', 'ay', 'igh', 'oa', 'ow', 'ar', 'ir', 'or', 'ur', 'oo', 'au', 'ear', 'air', 'ue', 'ui']
pat = ['ear', 'ore', 'ure']
#pattern = '[ ]*[.]*[b-df-hj-np-tv-z][a][b-df-hj-npqstv-z][e]$'  #find the patter a_e
#pattern = '[ ]*[.]*[b-df-hj-np-tv-z][i][b-df-hj-npqstv-z][e]$'  # find the pattern i_e
#pattern = '[ ]*[.]*[b-df-hj-np-tv-z][u][b-df-hj-npqstv-z][e]$' 
#pattern = '[ ]*[.]*[b-df-hj-np-tv-z][o][b-df-hj-npqstv-z][e]$'

pattern = '[ ]*[.]*[b-df-hj-np-tv-z][o][b-df-hj-npqstv-z]*'

for item in pat:
	f = open('../vowel/'+item+'.txt', 'w+')
	pattern = '[ ]*[.]*[b-df-hj-np-tv-z]'+item+'[b-df-hj-npqstv-z]*'
	print(pattern)
	for subitem in words:
		if re.search(pattern, subitem) and len(subitem) <= M:
			f.write(subitem+'\n')
	f.close()



for item in words:
	if re.search(pattern, item) and len(item) <= M:
		usedwords.append(item)
		
fn.close()

print(len(usedwords))
'''
N = 6 # how many words should serve
M = 7 # the longest word
D = 6 # the circle radius
extra = 4 #for saving some space
fixpos = 3 # fix the position of vowel
flag = 0

for filename in os.listdir('../vowel/'):
	usedwords = []
	f = open(os.path.join('../vowel/', filename))
	for line in f.readlines():
		if line.strip() not in usedwords and len(line.strip()) > 0:
			usedwords.append(line.strip())
	vowel = filename[0:filename.index('.')]


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
		#ax.set_xlim(-1*(distance+extra), (distance+extra))
		#ax.set_ylim(-1*(distance+extra), (distance+extra))

		i = 0
		for i in range(0, N):
			degree = i*math.pi*2/N

			while tt < len(usedwords):
				w2 = usedwords[tt]
				try:
					fixindex = w2.index(vowel)
				except:
					flag = 1
					print(vowel)
					print(w2)
					print('here')
					break
			
				if fixindex > fixpos:
					tt += 1
					continue
				elif len(w2) + fixpos - fixindex > M:
					tt += 1
					continue
				else:
					break
			if tt > len(usedwords):
				break
			else:
				tt += 1

			t = fixpos
			
			for z in range(fixindex-1,-1,-1):
				temp = axle2*1.0*(t+1.1)/M
				tempx = temp*math.cos(degree)
				tempy = temp*math.sin(degree)
				try:
					t1 = plt.text(tempx, tempy, w2[z], rotation = (360/N)*i, size=20, color='r')
				except:
					print(w2)
					print(str(z))
					flag = 1
					break
				t -= 1
				ax.add_artist(t1)

			t = fixpos
			#print("the second stage")
			for z in range(fixindex, fixindex+len(vowel)):
				t += 1
				temp = axle2*1.0*(1.05*t+1.5)/M
				tempx = temp*math.cos(degree)
				tempy = temp*math.sin(degree)
				t2 = plt.text(tempx, tempy, ' ', rotation = (360/N)*i, size=20, color='r')
				ax.add_artist(t2)

			t = (fixpos + len(vowel))*1.05 + 1.5
			#print("the third stage")
			for z in range(fixindex+len(vowel), len(w2)):
				temp = axle2*1.0*(t+1.5)/M
				tempx = temp*math.cos(degree)
				tempy = temp*math.sin(degree)
				t3 = plt.text(tempx, tempy, w2[z], rotation = (360/N)*i, size=20, color='r')
				

				t += 1
				#print(w2[len(w2)-z-1])
				ax.add_artist(t3)

			out_radius = max(temp+1.5, out_radius)


			plt.plot([0.4,0.4+0.5*math.cos(degree)],[0.4, 0.4+0.5*math.sin(degree)])

		if flag == 1:
			break
		ax.set_xlim(-1*(out_radius+extra), (out_radius+extra))
		ax.set_ylim(-1*(out_radius+extra), (out_radius+extra))
		circle1 = plt.Circle((0.4,0.4),radius = out_radius, fc = 'none')
		ax.add_artist(circle1)
		save_filename = 'word'+str(j)+'_'+vowel+'.png'
		
		#plt.show()
		fig.savefig('../wheels/'+save_filename)
		plt.clf()


		# draw the cover

		fig1 = plt.figure()
		plt.axis("equal")
		ax1 = fig1.add_subplot(111)
		ax1.axis('equal')
		ax1.set_xlim(-1*(out_radius+extra), (out_radius+extra))
		ax1.set_ylim(-1*(out_radius+extra), (out_radius+extra))
		circle2 = plt.Circle((0.4,0.4),radius = out_radius, fc = 'none')
		ax1.add_artist(circle2)
		for i in range(len(vowel)):
			tempx = axle2*1.0*(1.05*fixpos+1.5+i)/M
			tempy = 0
			plt.text(tempx, tempy, vowel[i], size=20, color = 'r')

		plt.plot([axle2*1.0*(1.05*fixpos+1.4)/M,axle2*1.0*(1.05*fixpos+1.4)/M ],[1,-1],'r-')
		plt.plot([axle2*1.0*(1.05*fixpos+len(vowel)+1.5)/M, axle2*1.0*(1.05*fixpos+len(vowel)+1.5)/M],[1,-1],'r-')
		ax1.add_patch(
			patches.Rectangle((axle2*1/M,-1), (out_radius - axle2*1/M), 2, edgecolor = 'r', fc = 'none')

		)
		for i in range(0, N):
			degree = i*math.pi*2/N
			plt.plot([0.4,0.4+0.5*math.cos(degree)],[0.4, 0.4+0.5*math.sin(degree)])

		save_filename = 'word'+str(j)+'_'+vowel+'_cover'+'.png'
		fig1.savefig('../wheels/'+save_filename)
		plt.clf()
		j += 1
	plt.close()

		
	
		#plt.show()




