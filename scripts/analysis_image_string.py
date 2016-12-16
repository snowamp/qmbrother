import nltk
import os
import sys
import re, codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from operator import itemgetter
from nltk.corpus import stopwords
from replacers import RegexpReplacer
from string import punctuation
import enchant
from nltk.corpus import wordnet as wn

d = enchant.Dict("en_US")

path = sys.argv[1]

basicwordfile = 'highfreq.txt'

g = open(basicwordfile, 'r+')
basicwords = g.readline().strip().split(' ')
g.close()

stopwords_one = set(stopwords.words('english') + list(punctuation))
lemmatizer = WordNetLemmatizer()

#f = open(os.path.join(path, "exp.txt"), 'w+')

for filename in os.listdir(path):
	if '.txt' in filename:
		sys.stdout.write(filename)
		sys.stdout.write('\n')
		replacer = RegexpReplacer()
		with codecs.open(os.path.join(path, filename), "r", encoding='utf-8', errors='ignore') as f:
			orgtext = f.read()
		orgtext1 = replacer.replace(orgtext)
		sent_text = sent_tokenize(orgtext1)	
		for sent in sent_text:
			sent_word = word_tokenize(sent)
			for word in sent_word:
				word = lemmatizer.lemmatize(word)
				if (word.lower() not in stopwords_one) and (word not in basicwords) and d.check(word):
					sys.stdout.write(word)
					sys.stdout.write('\t')
					syns = wn.synsets(word)
					for item in syns:
						name = item.name()
						result = wn.synset(name).lemma_names('cmn')
						for subitem in result:
							sys.stdout.write(subitem)
							sys.stdout.write(" ")



f.close()