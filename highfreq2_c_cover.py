import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
import os

N = 8 # how many words should serve
M = 7 # the longest word
D = 6 # the circle radius
extra = 3
fixpos = 3

for filename in os.listdir('../vowel/'):
	
	vowel = filename[0:filename.index('.')]



	axle1 = 1
	axle2 = axle1+D
	distance = axle1 + axle2

	fig = plt.figure()
	plt.axis("equal")


	ax1 = fig.add_subplot(111)

	ax1.axis('equal')

	

	circle2 = plt.Circle((0,0), radius = axle2+1, fc = 'none')
	ax1.add_artist(circle2)

	#rectangle1 = plt.Rectangle((axle1,2), (axle2 - axle1), 2, fill = 'red')

	ax1.add_patch(
		patches.Rectangle((axle2*1/M,-1), (axle2 - axle2*1/M), 2, edgecolor = 'r', fc = 'none')

		)

	

	for i in range(len(vowel)):
		tempx = axle2*1.0*(fixpos+1.5+i)/M
		tempy = 0
		plt.text(tempx, tempy, vowel[i], size=20, color = 'r')

	plt.plot([axle2*1.0*(fixpos+1)/M,axle2*1.0*(fixpos+1)/M ],[1,-1],'r-')
	plt.plot([axle2*1.0*(fixpos+len(vowel)+1)/M, axle2*1.0*(fixpos+len(vowel)+1)/M],[1,-1],'r-')
		
	for i in range(0, N):
		degree = i*math.pi*2/N
		plt.plot([0,axle1*math.cos(degree)],[0, axle1*math.sin(degree)])

	ax1.set_xlim(-1*(distance+extra), (distance+extra))
	ax1.set_ylim(-1*(distance+extra), (distance+extra))

	#fig.savefig('../wheels/cover.pdf')

	plt.show()
	break




