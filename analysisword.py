####################################################

# This code is to analyze the text file among

# the directory /NLP/kidbooks/

# I try to find the words frequency, verbs, nouns

# adjs and also comparing with 850 words and give

# its importance index

###################################################

import os

import sys

from textblob import TextBlob

from nltk.stem import LancasterStemmer

from replacers import RegexpReplacer

from textblob import Word

import pandas as pd

print("here")

class analysiswords:

	def __init__(self):

		self.filecontent = {}

		self.file_statistics = []

		self.basicwords = []

		self.objectivewordlist = []

		self.objectivewordtag = []

		self.objectivename = ''

		self.objectiveoutstring = ''

		self.objectivecount = {}

		self.second_frequency = []

		self.basicoverlap = 0
		self.weirdwords = []

	# obtain the original words from txt files

	def initialization(self):

		replacer = RegexpReplacer()

		basicwordfile = '/Users/yanchunyang/Documents/highschools/scripts/highfreq.txt'

		g = open(basicwordfile, 'r+')

		self.basicwords = g.readline().strip().split(' ')

	# upload the analysis objective

	def obtain_analysis_objective(self, filename):

		replacer = RegexpReplacer()

		pathname = filename

		pos = pathname.rindex('/')

		self.objectivename = pathname[int(pos)+1:len(pathname)]

		f = open(pathname, 'r+')

		for line in f.readlines():

			line = replacer.replace(line)

			self.objectiveoutstring += line

	# tag the file and count the frequency

	def obtain_the_tags_frequency(self):

		b = TextBlob(self.objectiveoutstring)

		# b, pass frequecy, pass Lancaster stemming, pass 850, pass wordnet, pass nn/vb
		# save dictionary

		wordtags = b.correct().tags

		
		# The first frequency saving
		stemmer = LancasterStemmer()
		first_frequecy = {}
		for item in wordtags:
			temp = stemmer.stem(item[0])
			if Word(temp).synsets and temp not in self.basicwords:
				if temp not in first_frequecy:
					first_frequecy[temp] = []
					first_frequecy[temp].append(item[1])
				else:
					try:
						first_frequecy[temp].append(item[1])
					except:
						print(temp)
						print(item)
			elif temp in self.basicwords:
				self.basicoverlap += 1
			else:
				self.weirdwords.append(item[0])




		
		for key in first_frequecy.keys():
			length = len(first_frequecy[key])
			tags_length = len(set(first_frequecy[key]))
			t1 = 0
			t2 = 0
			t3 = 1
			for it in set(first_frequecy[key]):
				if 'NN' in it:
					t1 = 1
					t3 = 0
				else:
					if 'VB' in it:
						t2 = 1
						t3 = 0
			self.second_frequency.append((key, length, tags_length, t1, t2, t3))





		

	

# start the analysis process

	def start_analysis(self, filename):

		self.obtain_analysis_objective(filename)

		self.obtain_the_tags_frequency()


		

	def output(self,filename):

		pos = filename.rindex('/')

		file_name = filename[pos+1:]

		file_name = '../csv/'+file_name+'.csv'

		df = pd.DataFrame(data = self.second_frequency, columns = ['word', 'freq', 'tag_freq', "noun", 'vb', 'other'])

		df.to_csv(file_name, sep = '\t')

def main():

	print("begin to run")

	analysis_begin = analysiswords()

	analysis_begin.initialization()

	path = "/Users/yanchunyang/Documents/NLP/kidbooks/"

	for name in os.listdir(path):

		filename = os.path.join(path, name)

		analysis_begin.start_analysis(filename)

		analysis_begin.output(filename)

if __name__ == '__main__':

	print("here")

	main()

	print("over")



'''
		path = '/Users/yanchunyang/Documents/NLP/kidbooks/'

		for name in os.listdir(path):

			filename = os.path.join(path,name)

			f = open(filename, 'r+')

			outstring = ''

			for line in f.readlines():

				outstring += replacer.replace(line)

			self.filecontent[name] = outstring
'''