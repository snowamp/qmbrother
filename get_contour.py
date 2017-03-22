#####################################
# Try to get contour of Mickey Mouse
#######################################

import numpy as np 
import cv2
from matplotlib import pyplot as plt
import math

im = cv2.imread('/Users/lxb/Documents/yyc/scripts/mickey.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



img = np.empty(im.shape, np.uint8)

cnt = contours[12]
img = cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

print(im.shape)

centerx = im.shape[0]/2
centery = im.shape[1]/2


#plt.imshow(img)
#plt.show()
pointslist = []
minx = 1000
maxx = 0
miny = 1000
maxy = 0

count = 0
for cnt in contours:
	newpoints = []
	for i in range(cnt.shape[0]):
		count += 1
		if count == 5:
			newpoints.append(list(cnt[i][0]))
			if cnt[i][0][0] > maxx:
				maxx = cnt[i][0][0]
			if cnt[i][0][0] < minx:
				minx = cnt[i][0][0]
			if cnt[i][0][1] > maxy:
				maxy = cnt[i][0][1]
			if cnt[i][0][1] < miny:
				miny = cnt[i][0][1]
			count = 0
	pointslist.append(newpoints)
diffx = (maxx-minx)/2.0 - centerx
diffy = (maxy-miny)/2.0 - centery

print(str(diffx))
print(str(diffy))
crop_image = im[minx:maxx, miny:maxy]
cv2.imwrite('mickey_crop.jpg', im)

reversepointlist = []

for newpoints in pointslist:
	if len(newpoints) < 2:
		continue
	reverse = []
	for point in newpoints:
		updatex = maxx - (point[0]-minx)
		updatey = point[1] - miny
		reverse.append([updatex, updatey])
	reversepointlist.append(reverse)

print(diffx)
print(diffy)

c1 = (maxx-minx)/2.0
c2 = (maxy-miny)/2.0

scale = (maxx-minx)/20.0

questions = []

with open('questions.txt', 'r') as g:
	for line in g.readlines():
		if len(line) > 2:
			questions.append(line.strip())
q_pointer = 0

colors = ['red!10', 'yellow!10', 'blue!10', 'green!10']
c=0
with open('coordinate.txt', 'w+') as f:
	f.write('\\textblockorigin{0cm}{0cm}\n')
	f.write('\\begin{textblock*}{20cm}(0cm, 1cm)\n')
	f.write('\\begin{tikzpicture}\n')
	f.write('\\node(fig1) at(0,0){\includegraphics[width='+ format((maxx-minx)/scale,'.2f')+ 'cm]{/Users/lxb/Documents/yyc/scripts/mickey_crop.jpg}};\n')
	f.write('\end{tikzpicture}\n')
	f.write('\end{textblock*}\n')
	f.write('\\null\\newpage\n')
	while q_pointer < len(questions):
		f.write('\\begin{textblock*}{20cm}(0cm, 1cm)\n')
		f.write('\\begin{tikzpicture}\n')
		
		for newpoints in reversepointlist:
			if len(newpoints) < 2:
				continue
			f.write('\\filldraw[color='+colors[c] +'] ')
			c += 1
			if c == len(colors):
				c=0
			for point in newpoints:
				f.write('('+format((c1-point[0])/scale,'.2f')+ ',' + format((c2-point[1])/scale,'.2f') + ') --')
			f.write('cycle;\n')
			break
		f.write('\\node(txt) at (-7, 7)[fontscale=2, text width=5cm]{'+questions[q_pointer] + '};\n')
		q_pointer += 1
		if q_pointer < len(questions):
			f.write('\\node(txt) at (5.5, 7)[fontscale=2, text width=5cm]{'+questions[q_pointer] + '};\n')
			q_pointer += 1
		
		f.write('\end{tikzpicture}\n')
		f.write('\end{textblock*}\n')
		f.write('\\null\\newpage\n')





'''
newx = []
newy = []
newpoint = []
edge = []





shape = im.shape

for item in contours:
	for i in range(item.shape[0]):
		temp = list(item[i][0])
		if temp[0] == 0 or temp[0] == shape[1]:
			edge.append(temp)
		elif temp[1] == 0 or temp[1] == shape[0]:
			edge.append(temp)
		else:
			newpoint.append(temp)
center = [im.shape[1]/2, im.shape[0]/2]

angle = {}
currentdis = 0
for i in range(len(newpoint)):
	vector = -1*np.array(newpoint[i]) - (-1)*np.array(center)
	dis = np.sqrt(math.pow(vector[0],2) + math.pow(vector[1],2))
	if currentdis == 0:
		currentdis = dis

	if abs(dis-currentdis) > 50:
		continue
	alpha = np.arccos(vector[0]/dis)
	if vector[1] < 0:
		alpha = 2*np.pi - alpha
	angle[i] = alpha
	currentdis = dis

points = sorted(angle, key = lambda x: angle[x])

for point in points:
	newx.append(newpoint[point][0])
	newy.append(newpoint[point][1])

plt.plot(newx, newy, '-')
plt.show()

'''