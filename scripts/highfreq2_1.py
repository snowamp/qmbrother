import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches

N = 8 # how many words should serve
M = 6 # the longest word
D = 6 # the circle radius
extra = 3


axle1 = 1
axle2 = axle1+D
distance = axle1 + axle2

fig = plt.figure()
plt.axis("equal")


ax1 = fig.add_subplot(111)

ax1.axis('equal')

ax1.set_xlim(-1*(distance+extra), (distance+extra))
ax1.set_ylim(-1*(distance+extra), (distance+extra))

circle2 = plt.Circle((0,0), radius = axle2+1, fc = 'none')
ax1.add_artist(circle2)

#rectangle1 = plt.Rectangle((axle1,2), (axle2 - axle1), 2, fill = 'red')

ax1.add_patch(
	patches.Rectangle((axle1,-1), (axle2 - axle1), 2, edgecolor = 'r', fc = 'none')

	)

pos_special = [0, 2]
char_special = ['e', 'a']
degree = math.pi*2/N
celldis = (axle2 - axle1)/M

for i in [0,1]:
	temp = axle1 + (axle2 - axle1)*1.0*(M-pos_special[i]-0.8)/M
	tempx = temp
	tempy = 0
	plt.text(tempx, tempy, char_special[i], size=20, color = 'r')

	plt.plot([(axle2 - celldis*pos_special[i]), (axle2 - celldis*pos_special[i])], [1,-1], 'r-')
	plt.plot([(axle2 - celldis*(pos_special[i]+1)), (axle2 - celldis*(pos_special[i]+1))], [1,-1], 'r-')

for i in range(0, N):
	degree = i*math.pi*2/N
	plt.plot([0,axle1*math.cos(degree)],[0, axle1*math.sin(degree)])



#fig.savefig('../wheels/cover.pdf')

plt.show()




