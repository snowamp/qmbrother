#test codes to run images in tkinter

import os, sys
import re
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import wand.image 
import tkinter.scrolledtext as tkst

root = Tk()
global nnps
global words 
global image 
global text 
global textselection 
global imageselection 
global wordselection 
global imgfile
nnps = '../sf/wordcandidate.txt'
path = '../sf/'
words = []
image = []
text = []
textselection = 0
imageselection = 0
wordselection = 0
t = StringVar() #save default word
currentcount = 0 #save how many image showed
      

with open(nnps, 'r') as f:
	words = f.readline().strip().split('\t')
print(words)
t.set(words[0])
wordselection = t.get()
		#read image file
		#print("******************")
		#print(self.wordselection)
tmppath = path + 'img/'

imgfile = []
for filename in os.listdir(tmppath):
	if 'thumbnail' in filename and wordselection in filename:
		imgfile.append(os.path.join(tmppath, filename))


    	# convert images
images = [Image.open(item) for item in imgfile]
for img in images:
	temp = ImageTk.PhotoImage(image = img)
	image.append(temp)
		
tmppath_1 = path + 'text/'
		
for item in os.listdir(tmppath_1):
	if wordselection in item:
		with open(os.path.join(tmppath_1,item), 'r') as f:
			texttmp = f.read()
			text = texttmp.split('\n')

print("wordselection is")
print(wordselection)	
	
def wordsel(value):
	global wordselection
	global imgfile 
	global image 
	global text 
	if wordselection != value:
		wordselection = value

	    	#read imagefile
		tmppath = path + 'img/'
		imgfile = []
		for filename in os.listdir(tmppath):
			if 'thumbnail' in filename and wordselection in filename:
				imgfile.append(os.path.join(tmppath, filename))

		image = []
		text = []
	    	# convert images
		images = [Image.open(item) for item in imgfile]
		for img in images:
			temp = ImageTk.PhotoImage(image = img)
			image.append(temp)

			# extract text related
		tmppath = path + 'text/'
		for fileanme in os.listdir(tmppath):
			if wordselection in filename:
				with open(os.path.join(tmppath,filename), 'r') as f:
					texttmp = f.read()
					text = texttmp.split('\n\n')

def imagesel():
	imageselection = str(v.get())

def textsel():
	textselection = str(s.get())



root.geometry('1000x800')


frame1 = Frame(root).grid(row = 0, column = 0, columnspan = 8, sticky = "n")
frame2 = Frame(root).grid(row = 2, column = 0, columnspan = 8, sticky = "n")
frame3 = Frame(root).grid(row = 2, column = 10, columnspan = 2, sticky = "n")
frame4 = Frame(root).grid(row = 2, column = 12, columnspan = 8, sticky = "n")

   		#add droplist for frame1
	
choices = words[1:]
print("**********")
print(choices)
option = OptionMenu(frame1, t, *choices, command = wordsel)
option.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
	
		#add the images for frame2

v = IntVar()
print("&&&&&&&&&&&&")
print(len(image))
imageradio = [Radiobutton(frame2,padx=60, pady = 60, variable = v, value = i, image = image[currentcount*9+i], command = imagesel) for i in range(6)]
for i in range(6):
	imageradio[i].grid(row = i*2+2, column = 0, columnspan = 8, sticky = "n")
		#add the ordernumber to frame3
s = IntVar()
textradio = []
for i in range(0, 6):
	tmp = currentcount * 9 + i
	textradio.append(Radiobutton(frame3, padx=20, variable = s, value = tmp, text = str(tmp), command = textsel))
	textradio[i].grid(row = i*2+2, column = 10, columnspan = 2, sticky = "n")
		

textvalue = [tkst.ScrolledText(master = frame4, wrap = WORD, height = 5, width = 10) for i in range(6)]

for i in range(0, 6):
	tmp = currentcount * 9 + i
	textvalue[i].grid(row = i*2+2, column = 12, columnspan = 20, sticky = "n")
	textvalue[i].insert(END, text[tmp])
		


root.mainloop()
root.destroy()






