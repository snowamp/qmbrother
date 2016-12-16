#obtain active verbs from the text books download and lists all the sentences containing these verbs.
import os
import sys
import re
import nltk
from cleantext import cleaner
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
import codecs

class analysis_activeverbs:
	def __init__:
		self.sentences = []
		self.verbs = []
		self.indexverbs = []
		self.verb_sent = {}

	def readverbs(self):
		with open('./analysis/verbs.txt', 'r') as f:
			for line in f.readlines():
				self.verbs.append(line.strip().split('\t'))

	def readtext(self):
		path = '/Users/yanchunyang/Documents/NLP/kidbooks/'
		for filename in os.listdir(path):
			with open(os.path.join(path, filename), 'r') as f:
				text = f.read()
				text_clean = cleaner.clean(text)
				for sent in text_clean:
					self.sentences.append(sent)

	def getindexverb(self):
		for sent in self.sentences:
			sent_word = nltk.pos_tag(word_tokenize(sent))

	def search(self,word):
		result = []
		for item in self.indexverbs:
			if bool(re.search(word, item)):
				for sent in self.verb_sent[item]:
					print(sent)

	def find(self,word):
		for item in self.indexverbs:
			if bool(re.search(word, item)):
				return True
		return False

	def count(self):
		unfindverbs = []
		for verb in self.verbs:
			for item in verb:
				if self.find(item):
					break
				unfindverbs.append(item)
		print(len(unfindverbs))
		print(unfindverbs)

def main():
	analysisverbs = analysis_activeverbs()
	analysisverbs.readverbs()
	analysisverbs.readtext()
	analysisverbs.getindexverb()
	analysisverbs.count()

if __name__ == '__main__':
	main()





