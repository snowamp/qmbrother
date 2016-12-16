#download txt files from textfiles
#based on the verbs list I got before and
#extract the sentences from these files
#setup database to save

import os
import sys
import re
import nltk
from cleantext import cleaner
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import codecs
import pymysql
import pymysql.cursors
from collections import defaultdict

verbs = set()
sents = {}
path = '/Users/yanchunyang/Documents/highschools/text/'
def obtain_verbs():
	filename = "/Users/yanchunyang/Documents/highschools/scripts/analysis/verbs.txt"
	with open(filename,'r') as f:
		for line in f.readlines():
			splits = line.strip().split('\t')
			for item in splits:
				verbs.add(item)

def go_through():

	clean = cleaner()
	lancaster_stemmer = LancasterStemmer()
	connection = pymysql.connect(host='localhost', user='root', password = 'sunnyvale2016', db = 'words')

	for filename in os.listdir(path):
		print(filename)
		sents = defaultdict(list)
		dotindex = filename.index('.')
		article = filename[0:dotindex]
		with codecs.open(os.path.join(path, filename), 'r',encoding='utf-8', errors='ignore') as f:
			text = f.read()
			text_array = clean.clean(text)
			for sub_sent in text_array:
				stem_temp = [lancaster_stemmer.stem(item) for item in word_tokenize(sub_sent)]
				temp = word_tokenize(sub_sent)
				for verb in verbs:
					verb = verb.strip().lower()
					verb_splits = verb.split(' ')
					if len(verb_splits) == 1:
						if lancaster_stemmer.stem(verb) in stem_temp:
							sents[verb].append(sub_sent)
					else:
						flag = 0
						#print(verb_splits)
						if lancaster_stemmer.stem(verb_splits[0]) in stem_temp:
							index = stem_temp.index(lancaster_stemmer.stem(verb_splits[0])) #leave a small bug since verbs can show multiple times
							for i in range(1, len(verb_splits)):
								if verb_splits[i] != temp[index+i]:
									flag = 1
									break
						if flag:
							continue
						else:
							sents[verb].append(sub_sent)

		with connection.cursor() as cursor:
			sql = """insert into `verbsents` (`verb`, `article`, `sents`) values (%s, %s, %s) """
			for key in sents.keys():
				try:
					for item in sents[key]:
						cursor.execute(sql, (key, article, item))
				except Exception as inst:
						print(type(inst))
						print(inst.args)
						print(key)
						continue
		connection.commit()

	connection.close()


def main():
	obtain_verbs()
	go_through()

if __name__ == '__main__':
	main()
