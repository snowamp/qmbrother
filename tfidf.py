"""
https://radimrehurek.com/gensim/models/ldamodel.html 

Detail information for the LDA

"""


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
import math
import string
import operator
from collections import defaultdict
from gensim import corpora, models


def obtain_text():
	text = []
	replacer = RegexpReplacer()
	st = LancasterStemmer()
	stops = stopwords.words('english')
	path = '/Users/yanchunyang/Documents/highschools/subtext/'
	for filename in os.listdir(path):
		if '3' in filename:
			with open(os.path.join(path, filename), 'r') as f:
				text.append(replacer.replace(f.read()))

	word_content = []

	for sub in text:
		temp = word_tokenize(sub)
		word_content.append([st.stem(word) for word in temp if word not in stops])

	dictionary = corpora.Dictionary(word_content)

	corpus = [dictionary.doc2bow(text) for text in word_content]

	get_tdidf_lda(corpus, dictionary)

def get_tdidf_lda(corpus, dictionary):

	corpus_update = []

	corpus_new = []

	tfidf = models.TfidfModel(corpus)

	corpus_tfidf = tfidf[corpus]

	for i in range(len(corpus_tfidf)):

		temp = sorted(corpus_tfidf[i], key = lambda x:x[1], reverse=True)

		corpus_update.append(temp)

	#get the important words
	corpus_new = [temp[0:200] for temp in corpus_update]

	corpus_1 = []

	for i in range(0, len(corpus)):
		temp = [word[0] for word in corpus_new[i]]
		new_temp = []
		for item in corpus[i]:
			if item[0] in temp:
				new_temp.append(item)

		corpus_1.append(new_temp)

	model = models.LdaModel(corpus_1, id2word=dictionary, num_topics=10)

	document2topic = model[corpus]

	print(document2topic[0])


def main():
	obtain_text()


if __name__ == '__main__':
	main()











