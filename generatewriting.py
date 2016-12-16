#based on NNP word lists and generate the text
#obtain the sentences for these views
import os
import sys
import re
import nltk
from cleantext import cleaner
from generatepicwords import combinepicword
from collections import defaultdict
from tkinter import *

class analysis_nnps:
	def __init__(self):
		self.nnps = []
		self.nnp_sent = defaultdict(list)
		self.path = '../panama/text/'

	def readwords(self):
		with open('../panama/wordcandidate.txt', 'r') as f:
			self.nnps = f.readline().split('\t')
			for item in self.nnps:
				filename = item+'.txt'
				g = open(os.path.join(self.path, filename), 'w+')
				g.write(' ')
				g.close()

	
def main():
	analysis = analysis_nnps()
	analysis.readwords()
	

if __name__ == '__main__':
	main()





