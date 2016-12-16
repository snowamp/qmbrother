#analyze Harry Potter files and its vocabulary and terms and statistics.
#learning English from Harry Potter

import nltk
import os
import sys
import re, codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from collections import defaultdict
from operator import itemgetter
from nltk.corpus import stopwords
from replacers import RegexpReplacer

words = []
def readfile(path, filename):
	replacer = RegexpReplacer()
	with codecs.open(os.path.join(path, filename), "r", encoding='utf-8', errors='ignore') as f:
		orgtext = f.read()
	orgtext1 = replacer.replace(orgtext)
	temp = []
	parse_pattern = []
	sent_text = sent_tokenize(orgtext1)
	grammar = "NP:{<DT>?<JJ>*<NN><IN>?<NN>*}"
	find = nltk.RegexpParser(grammar)
	for sent in sent_text:
		sent_word = nltk.pos_tag(word_tokenize(sent))
		if find.parse(sent_word):
			parse_pattern.append(sent)
		temp.append(nltk.pos_tag(word_tokenize(sent)))
	print(len(parse_pattern))
	print(parse_pattern[0:5])
	#words = [word for item in temp for word in item]
	#tag_fd = nltk.FreqDist(tag[0:2] for (word, tag) in words)
	#analysis(words)

def analysis(words):
	noun = defaultdict(int)
	verb = defaultdict(int)
	jj = defaultdict(int)
	rb = defaultdict(int)
	other = defaultdict(int)
	lemmatizer = WordNetLemmatizer()
	stemmerlan = LancasterStemmer()
	i = 0
	
	for item in words:
		t = lemmatizer.lemmatize(item[0].lower())
		#t = stemmerlan.stem(item[0].lower())
		t.replace('\'', '')
		if len(item[0]) > 0:
			i += 1
			if item[1][0:2] == 'NN':
				noun[t] += 1
			elif item[1][0:2] == 'VB':
				verb[t] += 1
			elif item[1][0:2] == 'JJ':
				jj[t] += 1
			elif item[1][0:2] == 'RB':
				rb[t] += 1
			else:
				other[t] += 1

	
	output(noun, "noun")
	output(verb, "verb")
	output(jj, "adj")
	output(rb, "adv")
	output(other, "other")
	

def output(diction, filename):
	with open(filename+'.txt', 'w+') as f:
		for key, value in sorted(diction.items(), key = itemgetter(1), reverse = True):
			#print(key+' '+str(value))
			f.write(key+' '+str(value))
			f.write('\n')
	




def main():
	path = "/Users/yanchunyang/Documents/NLP/kidbooks/"
	filename = "harrypotter1.txt"
	readfile(path, filename)
	

if __name__ == '__main__':
	main()

