#set up vocabulary for picture books

import sys
import os
import nltk
import re
from replacers import RegexpReplacer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer


#read the novels inside the code

filenamelist = {}
stops = set(stopwords.words('english'))

def tokenize(text):
	regex = re.compile(r'^[a-zA-Z]')
	replacer = RegexpReplacer()
	lemmatizer = WordNetLemmatizer()
	temp = replacer.replace(text)
	sent_temp = sent_tokenize(temp)
	word_temp = [word_tokenize(doc) for doc in sent_temp]
	wordlist = [item for sub in word_temp for item in sub]
	x = re.compile('[%s]' % re.escape(string.punctuation))
	y = re.compile('^[a-zA-Z]')
	newwordlist = []
	for word in wordlist:
		if (not bool(re.search(x, word))) and (word.lower() not in stops) and bool(re.search(y, word)):
			t = lemmatizer.lemmatize(word.lower())
			newwordlist.append(t)
	return newwordlist

def tfidf(filepath):
	for filename in os.listdir(filepath):
		with open(os.path.join(filepath, filename)) as f:
			filenamelist[filename] = f.read()
	tfidf = TfidfVectorizer(tokenizer = tokenize)
	tfs = tfidf.fit_transform(filenamelist.values())
	feature_names = tfidf.get_feature_names()
	for row in tfs.nonzero()[0]:
		for col in tfs.nonzero()[1]:
			print(feature_names[col], '-', tfs[row, col])

	
	




		



def main():
	tfidf('/Users/yanchunyang/Documents/NLP/kidbooks/')

if __name__ == '__main__':
	main()




