#generate picture with text
# the whole process is listed in process.txt
# set up project folder
# set up wordcandidate.txt
# set up folders: img, text
# revise path in downloadpics.py
# run downloadpics.py
# revise path in convertimpage.py and run it
# run generatewriting.py to generate text files
# add materials to text files
# run testimage_gui.py
# click translate button

import os, sys
import re
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import wand.image 
import tkinter.scrolledtext as tkst
from cleantext import cleaner
from generatepicwords import combinepicword
from translate_chinese import translate



class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.nnps = '../panama/wordcandidate.txt'
		self.path = '../panama/'
		self.words = []
		self.image = []
		self.text = []
		self.textselection = 0
		self.imageselection = 0
		self.wordselection = ''
		self.t = StringVar(self) #save default word
		self.currentcount_image = 0 #save how many image showed
		self.currentcount_text = 0
		self.readdata()
		self.master.title('Hello, Tkinter!')
		self.master.geometry('1000x800')
		self.grid()
		self.createWidgets()
		self.imgcount = 20
		self.translate = {}
        
	def readdata(self):
		with open(self.nnps, 'r') as f:
			self.words = f.readline().strip().split('\t')
		self.t.set(self.words[0])
		self.wordselection = self.t.get()
		tmppath = self.path + 'img/'
		self.imgfile = []
		for filename in os.listdir(tmppath):
			if 'thumbnail' in filename and self.wordselection in filename:
				self.imgfile.append(os.path.join(tmppath, filename))

		self.image = []
		self.text = []
    	# convert images
		images = [Image.open(item) for item in self.imgfile]
		for img in images:
			temp = ImageTk.PhotoImage(image = img)
			self.image.append(temp)
		
		tmppath_1 = self.path + 'text/'
		clean_text = cleaner()
		for item in os.listdir(tmppath_1):
			if self.wordselection in item:
				with open(os.path.join(tmppath_1,item), 'r') as f:
					texttmp = f.read()
					sents = clean_text.clean(texttmp)
					for item in sents:
						self.text.append(item)
		
	
	def wordsel(self,value):
		if self.wordselection != value:
			self.wordselection = value
			print('^^^^^^^')
			print(self.wordselection)
			self.currentcount_image = 0
			self.currentcount_text = 0
	    	#read imagefile
			tmppath = self.path + 'img/'
			self.imgfile = []
			for filename in os.listdir(tmppath):
				if 'thumbnail' in filename and self.wordselection in filename:
					self.imgfile.append(os.path.join(tmppath, filename))

			self.image = []
			self.text = []
	    	# convert images
			images = [Image.open(item) for item in self.imgfile]
			for img in images:
				temp = ImageTk.PhotoImage(image = img)
				self.image.append(temp)

			for i in range(0, 6):
				self.imageradio[i].configure(image = self.image[i])

			# extract text related
			tmppath = self.path + 'text/'
			clean_text = cleaner()
			for file_name in os.listdir(tmppath):
				if self.wordselection in file_name:
					with open(os.path.join(tmppath,file_name), 'r') as f:
						texttmp = f.read()
						sents = clean_text.clean(texttmp)
						for item in sents:
							self.text.append(item)
			for i in range(0, 6):
				self.textvalue[i].delete('1.0', END)
				self.textvalue[i].insert('1.0',self.text[i])
			print(self.textvalue[-1].get('1.0', END+'-1c'))

	def imagesel(self):
		self.imageselection = self.v.get()

	def textsel(self):
		self.textselection = self.s.get()

	def imageprev(self):
		if self.currentcount_image == 0:
			return
		else:
			self.currentcount_image -= 1
			for i in range(0, 6):
				tmp = self.currentcount_image * 6 + i
				self.imageradio[i].configure(image = self.image[tmp])

	def imagenext(self):

		if (self.currentcount_image + 1) * 6 < len(self.image):
			self.currentcount_image += 1
			for i in range(0, 6):
				tmp = self.currentcount_image * 6 + i 
				if tmp < len(self.image):
					self.imageradio[i].configure(image = self.image[tmp] )
				else:
					self.imageradio[i].configure(image = None)

	def textprev(self):
		if self.currentcount_text == 0:
			return
		else:
			self.currentcount_text -= 1
			for i in range(0, 6):
				tmp = self.currentcount_text * 6 + i
				self.textvalue[i].delete('1.0', END)
				self.textvalue[i].insert('1.0', self.text[tmp])

	def textnext(self):
		if (self.currentcount_text + 1) * 6 < len(self.text):
			self.currentcount_text += 1
			for i in range(0, 6):
				tmp = self.currentcount_text * 6 + i 
				if tmp < len(self.text):
					self.textvalue[i].delete('1.0', END)
					self.textvalue[i].insert('1.0', self.text[tmp])
				else:
					self.textvalue[i].delete('1.0', END)

	def match(self):
		if self.imageselection < 0 or self.textselection < 0:
			return
		else:
			tmp_image = self.currentcount_image * 6 + self.imageselection
			string = self.textvalue[self.textselection].get('1.0', END+'-1c')
			matcher = combinepicword()
			matcher.combine(string, self.imgfile[tmp_image])
			self.translate[self.imgfile[tmp_image]] = string

	def toChinese(self):
		if len(self.translate.keys()) == 0:
			return
		filename = "translate.txt"
		translator = translate()
		f = open(os.path.join(self.path, filename), 'w+')
		for key in self.translate.keys():
			index = key.find('_thumbnail')
			title = key[0:index]
			f.write(title)
			f.write('\n')
			string_chinese = translator.translate_to_chinese(self.translate[key])
			for subkey in string_chinese.keys():
				f.write(subkey+':')
				for subitem in string_chinese[subkey]:
					f.write(subitem+' ')
				f.write('\n')
			f.write('\n')
			f.write('\n')
		f.close()

	def updateoption(self):
		pass

	
	def createWidgets(self):
   		#add the frames for the widges
		self.frame1 = Frame(self).grid(row = 0, column = 0, columnspan = 6, sticky = "n")
		self.frame2 = Frame(self).grid(row = 2, column = 4, columnspan = 6, sticky = "n")
		self.frame3 = Frame(self).grid(row = 2, column = 12, columnspan = 2, sticky = "n")
		self.frame4 = Frame(self).grid(row = 2, column = 16, columnspan = 6, sticky = "n")
		self.frame5 = Frame(self).grid(row = 2, column = 24, columnspan = 6, sticky = "n")

   		#add droplist for frame1
		
		choices = self.words
		self.option = OptionMenu(self.frame1, self.t, *choices, command = self.wordsel)
		self.option.grid(row = 0, column = 0, columnspan = 6, sticky = "n")
		
		#add the images for frame2
		self.v = IntVar(self)
		self.v.set(0)
		self.imageradio = []
		for i in range(0, 6):
			tmp = self.currentcount_image * 6 + i
			self.imageradio.append(Radiobutton(self.frame2,padx=20, pady = 20, variable = self.v, value = tmp, image = self.image[tmp], command = self.imagesel))
			self.imageradio[i].grid(row = i*2+2, column = 0, columnspan = 6)

		self.button1 = Button(self.frame2, text = "prev", command = self.imageprev)
		self.button1.grid(row = 1, column = 0, columnspan = 2)

		self.button2 = Button(self.frame2, text = "next", command = self.imagenext)
		self.button2.grid(row = 1, column = 3, columnspan = 2)
		#add the ordernumber to frame3
		self.s = IntVar(self)
		self.s.set(0)
		self.textradio = []
		for i in range(0, 6):
			self.textradio.append(Radiobutton(self.frame3, padx=20, variable = self.s, value = i, text = str(i), command = self.textsel))
			self.textradio[i].grid(row = i*2 +2, column = 6, columnspan = 2)
		
		self.textvalue = []
		for i in range(0, 6):
			tmp = self.currentcount_text * 6 + i
			self.textvalue.append(tkst.ScrolledText(master = self.frame4, wrap = WORD, height = 8, width = 60))
			self.textvalue[i].grid(row = i*2 + 2, column = 8, columnspan = 6)

		for i in range(0, 6):
			tmp = self.currentcount_text* 6 + i
			self.textvalue[i].insert('1.0', self.text[tmp])
		print(self.textvalue[tmp].get('1.0', END+'-1c'))

		self.button3 = Button(self.frame4, text = "prev", command = self.textprev)
		self.button3.grid(row = 1, column = 8, columnspan = 2)

		self.button4 = Button(self.frame4, text = "next", command = self.textnext)
		self.button4.grid(row = 1, column = 11, columnspan = 2)

		self.button5 = Button(self.frame1, text = "match", command = self.match)
		self.button5.grid(row = 0, column = 18, columnspan = 2)

		self.button6 = Button(self.frame1, text = "translate", command = self.toChinese)
		self.button6.grid(row = 1, column = 18, columnspan = 2)

		self.wordcandidate = tkst.ScrolledText(master = self.frame5, wrap = WORD, height = 100, width = 30)
		self.wordcandidate.grid(row = 6, column = 24, columnspan = 6)
		self.wordlabel = Label(master=self.frame5, text="Word List")
		self.wordlabel.grid(row = 5, column =24, columnspan = 6)

		self.button8 = Button(master=self.frame5, text = "confirm", command = self.updateoption)
		self.button8.grid(row=4, column = 24, columnspan = 2)

		

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

print(translate)


