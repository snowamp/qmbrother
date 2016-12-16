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
import enchant #online dictionary
from nltk.corpus import wordnet as wn


basicwordfile = 'highfreq.txt'

g = open(basicwordfile, 'r+')
basicwords = g.readline().strip().split(' ')
g.close()

stopwords_one = set(stopwords.words('english') + list(punctuation))


class translate(object):
	def __init__(self, basic = basicwords, stop = stopwords_one):
		self.basic = basicwords
		self.stop = stopwords_one
		self.d = enchant.Dict("en_US")
		self.lemmatizer = WordNetLemmatizer()
		self.replacer = RegexpReplacer()

	def translate_to_chinese(self, string):
		translate_result = {}
		org_string = self.replacer.replace(string)
		sent_word = word_tokenize(org_string)
		for word in sent_word:
			word = self.lemmatizer.lemmatize(word)
			if (word.lower() not in self.stop) and (word not in self.basic) and self.d.check(word):
				translate_result[word] = []
				syns = wn.synsets(word)
				for item in syns:
					name = item.name()
					result = wn.synset(name).lemma_names('cmn')
					for subitem in result:
						translate_result[word].append(subitem)
		return translate_result

