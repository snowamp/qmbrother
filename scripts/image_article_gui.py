#generate picture with text
#similar to testimage_gui.py

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
from obtainnnp import obtain_nnp
from dppk_2 import download, convert_img
from aws_polly import get_audio



class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.words = ['test']  #save the selected nnp words
		self.t = StringVar(self) #save default word
		self.text = []
		self.currentcount_image = 0 #save how many image showed
		self.currentcount_text = 0
		self.readdata()
		self.master.title('Hello, Tkinter!')
		self.master.geometry('1000x800')
		self.grid()
		self.createWidgets()
		self.imgcount = 20
		self.translate = {}
		self.image = []
		self.imgfile = []
		self.sents = []
		self.imagefolder = ''
		self.wordselection = ''
		self.imageselection = 0
		self.textselection = 0
		

	def number(self):
		return 5


	def readdata(self):
		pass
		
	
	def wordsel(self,value):
		if self.wordselection != value:
			self.wordselection = value
			print('^^^^^^^')
			print(self.wordselection)
			self.currentcount_image = 0
	    	#read imagefile
			self.imgfile = []
			for filename in os.listdir(self.imagefolder):
				if 'thumbnail' in filename and self.wordselection in filename:
					self.imgfile.append(os.path.join(self.imagefolder, filename))

			self.image = []
			self.text = []
	    	# convert images
			images = [Image.open(item) for item in self.imgfile]
			for img in images:
				temp = ImageTk.PhotoImage(image = img)
				self.image.append(temp)

			for i in range(0, min(self.number(), len(self.image))):
				self.imageradio[i].configure(image = self.image[i])	

	def imagesel(self):
		self.imageselection = self.v.get()

	def textsel(self):
		self.textselection = self.s.get()

	def imageprev(self):
		if self.currentcount_image == 0:
			return
		else:
			self.currentcount_image -= 1
			for i in range(0, self.number()):
				tmp = self.currentcount_image * self.number() + i
				self.imageradio[i].configure(image = self.image[tmp])


	def imagenext(self):
		if (self.currentcount_image + 1) * self.number() <= len(self.image):
			self.currentcount_image += 1
			for i in range(0, self.number()):
				tmp = self.currentcount_image * self.number() + i 
				if tmp < len(self.image):
					self.imageradio[i].configure(image = self.image[tmp] )
				else:
					self.imageradio[i].configure(image = None)
		else:
			if (self.currentcount_image+1)*self.number() > len(self.image) and self.currentcount_image * self.number() < len(self.image):
				left = len(self.image) - (self.currentcount_image * self.number())
				for i in range(0, left):
					tmp = self.currentcount_image * self.number() + i
					self.imageradio[i].configure(image = self.image[tmp])

	def textprev(self):
		if self.currentcount_text == 0:
			return
		else:
			self.currentcount_text -= 1
			for i in range(0, self.number()):
				print(self.currentcount_text)
				tmp = self.currentcount_text * self.number() + i
				self.textvalue[i].delete('1.0', END)
				self.textvalue[i].insert('1.0', self.text[tmp])


	def textnext(self):
		if (self.currentcount_text + 1) * self.number() <= len(self.sents):
			self.currentcount_text += 1
			for i in range(0, self.number()):
				tmp = self.currentcount_text * self.number() + i 
				if tmp < len(self.sents):
					self.textvalue[i].delete('1.0', END)
					self.textvalue[i].insert('1.0', self.sents[tmp])
				else:
					self.textvalue[i].delete('1.0', END)
		else:
			if (self.currentcount_text + 1) * self.number() >= len(self.sents) and self.currentcount_text * self.number() < len(self.sents):
				for i in range(0, self.number()):
					self.textvalue[i].delete('1.0', END)
				left = len(self.sents) - self.currentcount_text * self.number()
				for i in range(0, left):
					tmp = self.currentcount_text * self.number() + i
					self.textvalue[i].insert('1.0', self.sents[tmp])
				self.currentcount_text += 1



	def match(self):
		if self.imageselection < 0 or self.textselection < 0:
			return
		else:
			tmp_image = self.currentcount_image * self.number() + self.imageselection
			string = self.textvalue[self.textselection].get('1.0', END+'-1c')
			matcher = combinepicword()
			matcher.combine(string, self.imgfile[tmp_image])
			self.translate[self.imgfile[tmp_image]] = string

	def toChinese(self):
		if len(self.translate.keys()) == 0:
			return
		filename = "translate.txt"
		translator = translate()
		f = open(os.path.join(self.imagefolder, filename), 'w+')
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
		filename = "Englishwords.txt"
		g = open(os.path.join(self.imagefolder, filename), 'w+')
		for key in self.translate.keys():
			g.write(key+'\t')
			g.write(self.translate[key])
			g.write('\n')
		g.close()



	def textanalysis(self):
		filepath = self.inputpath.get('1.0', END+'-1c').strip()
		clean_text = cleaner()
		obtain_word = obtain_nnp()
		with open(filepath, 'r') as f:
			text = f.read()
			self.sents = clean_text.clean(text)
			for item in self.sents:
				if len(item) > 0:
					self.text.append(item)
			nnp_words = obtain_word.obtain(text)
			for item in nnp_words:
				self.wordcandidate.insert(END, item+'\n')
			for i in range(0, self.number()):
				self.textvalue[i].insert('1.0', self.sents[i])
		index = filepath.find('.')
		foldername = filepath[0:index]
		self.imagefolder = './' + foldername + '/'
		if not os.path.exists(self.imagefolder):
			os.makedirs(self.imagefolder)
		print("folder generated")

	def updateOption(self):
		self.words = []
		tmp_string = self.wordlabel.get('1.0', END+'-1c').strip()
		self.helpterm = tmp_string
		string = self.wordcandidate.get('1.0', END+'-1c')
		splits = string.split('\n')
		for item in splits:
			if len(item) > 0:
				self.words.append(item)
		self.t.set(self.words[0])
		choices = self.words
		print(self.t)
		#add droplist
		self.option = OptionMenu(self.frame1, self.t, *choices, command = self.wordsel)
		self.option.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
	
	def download(self):
		download(path = self.imagefolder, terms = self.words, helpterm = self.helpterm )

	def convert(self):
		print(self.imagefolder)
		convert_img(self.imagefolder)
		self.imgfile = []
		self.wordselection = self.t.get()
		for filename in os.listdir(self.imagefolder):
			if 'thumbnail' in filename and self.wordselection in filename:
				self.imgfile.append(os.path.join(self.imagefolder, filename))
		self.image = []
		images = [Image.open(item) for item in self.imgfile]
		for img in images:
			temp = ImageTk.PhotoImage(image = img)
			self.image.append(temp)
		for i in range(0, min(self.number(), len(self.image))):
			self.imageradio[i].configure(image = self.image[i])
		
	def getAudio(self):
		get_audio(self.imagefolder)
		print("obtain the audio")
	
	def createWidgets(self):
   		#add the frames for the widges
		self.frame1 = Frame(self).grid(row = 0, column = 0, columnspan = 6, rowspan = 3, sticky = "n")
		self.frame2 = Frame(self).grid(row = 2, column = 4, columnspan = 6 , sticky = "n")
		self.frame3 = Frame(self).grid(row = 2, column = 12, columnspan = 2, sticky = "n")
		self.frame4 = Frame(self).grid(row = 2, column = 16, columnspan = 6, sticky = "n")
		self.frame5 = Frame(self).grid(row =2, column = 22, columnspan = 6, sticky = "n")

		# add widgets for frame1
   		
		self.label1 = Label(master = self.frame1, text = "text file path")
		self.label1.grid(row = 0, column = 4, columnspan = 4, sticky = "n")

		self.inputpath = Text(master = self.frame1, wrap = WORD, height = 2, width = 100)
		self.inputpath.grid(row = 0, column = 8, columnspan = 24, sticky = "n")

		self.button11 =Button(self.frame1, text="audio", command = self.getAudio)
		self.button11.grid(row = 1, column =4, columnspan = 2)

		self.button5 = Button(self.frame1, text = "match", command = self.match)
		self.button5.grid(row = 1, column = 8, columnspan = 2)

		self.button6 = Button(self.frame1, text = "translate", command = self.toChinese)
		self.button6.grid(row = 1, column = 12, columnspan = 2)

		self.button7 = Button(self.frame1, text = "input_text", command = self.textanalysis)
		self.button7.grid(row = 1, column = 16, columnspan = 2)

		self.button9 = Button(self.frame1, text = "convert_img", command = self.convert)
		self.button9.grid(row = 1, column = 20, columnspan = 2)

		self.button10 = Button(self.frame1, text = "download_pic", command = self.download)
		self.button10.grid(row = 1, column = 24, columnspan = 2)

		#self.label2 = Label(self.frame1, height = 1, width = 100, background = 'gray')
		#self.label2.grid(row = 2, column = 0, columnspan = 24)

		
		#add the images for frame2
		self.v = IntVar(self)
		self.v.set(0)
		self.imageradio = []
		for i in range(0, self.number()):
			tmp = self.currentcount_image * self.number() + i
			self.imageradio.append(Radiobutton(self.frame2,padx=20, pady = 20, variable = self.v, value = tmp,  command = self.imagesel))
			self.imageradio[i].grid(row = i*2+4, column = 0, columnspan = 6, rowspan = 2)

		self.button1 = Button(self.frame2, text = "prev", command = self.imageprev)
		self.button1.grid(row = 2, column = 0, columnspan = 2)

		self.button2 = Button(self.frame2, text = "next", command = self.imagenext)
		self.button2.grid(row = 2, column = 3, columnspan = 2)
		

		#add the ordernumber to frame3
		self.s = IntVar(self)
		self.s.set(0)
		self.textradio = []
		
		for i in range(0, self.number()):
			self.textradio.append(Radiobutton(self.frame3, padx=20, variable = self.s, value = i, text = str(i), command = self.textsel))
			self.textradio[i].grid(row = i*2 +4, column = 12, columnspan = 2)
			

		# add text sentence for frame4

		self.textvalue = []
		for i in range(0, self.number()):
			tmp = self.currentcount_text * self.number() + i
			self.textvalue.append(tkst.ScrolledText(master = self.frame4, wrap = WORD, height = 8, width = 60))
			self.textvalue[i].grid(row = i*2 + 4, column = 16, columnspan = 6)
		
		self.button3 = Button(self.frame4, text = "prev", command = self.textprev)
		self.button3.grid(row = 2, column = 16, columnspan = 2)

		self.button4 = Button(self.frame4, text = "next", command = self.textnext)
		self.button4.grid(row = 2, column = 18, columnspan = 2)

		#add text frame, wordlist for frame5

		self.wordcandidate = tkst.ScrolledText(master = self.frame5, wrap = WORD, height = 60, width = 30)
		self.wordcandidate.grid(row = 4, column = 22, columnspan = 6, rowspan = 60)
		self.wordlabel = Text(master=self.frame5, wrap = WORD, height = 1)
		self.wordlabel.grid(row = 2 ,column =24, columnspan = 6, rowspan = 1)

		self.button8 = Button(master=self.frame5, text = "confirm", command = self.updateOption)
		self.button8.grid(row=2, column = 22, columnspan = 2)

		
		

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

print(translate)


