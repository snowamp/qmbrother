##################################################
#Draw the plate to learn English words version 1
#
###################################################


import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

'''
fn = open("highfreq.txt", 'r') 

words = fn.readline().strip().split(' ')

print(len(words))

pattern = '[ ]*[.]*[b-df-hj-np-tv-z][a][b-df-hj-npqstv-z][e]$'  #find the patter a_e

for item in words:
	if re.search(pattern, item):
		print(item)

fn.close()
'''
w1 = 'take'
w2 = 'place'
axle1 = 2
axle2 = 8

plt.figure(1)
plt.subplot(111)


for i in range(0, 6):
	degree = i*math.pi/3
	#print(degree)
	#plt.plot([axle1*math.cos(degree), axle2*math.cos(degree)], [axle1*math.sin(degree), axle2*math.sin(degree)], 'r--')
	rect_x = [axle1*math.cos(degree)-math.sin(degree), axle1*math.cos(degree)+math.sin(degree),axle2*math.cos(degree)+math.sin(degree), axle2*math.cos(degree)-math.sin(degree),axle1*math.cos(degree)-math.sin(degree)]
	rect_y = [axle1*math.sin(degree)+math.cos(degree), axle1*math.sin(degree)-math.cos(degree),axle2*math.sin(degree)-math.cos(degree), axle2*math.sin(degree)+math.cos(degree),axle1*math.sin(degree)+math.cos(degree)]
	
	plt.plot(rect_x, rect_y, 'r--')

	for j in range(1, 7):
		temp = axle1 + (axle2 - axle1)*1.0*j/6
		tempx = [temp*math.cos(degree)-math.sin(degree), temp*math.cos(degree)+math.sin(degree)]
		tempy = [temp*math.sin(degree)+math.cos(degree), temp*math.sin(degree)-math.cos(degree)]
		plt.plot(tempx, tempy, 'r--')
	
	for z in range(0, len(w2)):
		temp = axle1 + (axle2 - axle1)*1.0*(6-z)/6 - 0.8+i*0.1
		tempx = temp*math.cos(degree)
		tempy = temp*math.sin(degree)

		plt.text(tempx, tempy, w2[len(w2)-z-1], rotation = 60*i, size=18)


	#for j in range(2, 6):
		#plt.plot([i*math.cos(degree), i*math.cos(degree)], [1*math.sin(degree), 1*math.sin(degree)])

plt.show()