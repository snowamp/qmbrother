
import nltk
import os
import sys
import re, codecs
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from operator import itemgetter
from nltk.corpus import stopwords
from replacers import RegexpReplacer
from string import punctuation
import enchant #online dictionary
from nltk.corpus import wordnet as wn
import pymysql
import pymysql.cursors

class handle_word:
	def __init__(self):
		self.words = []
		self.word_cn = {}
		self.word_class={}
		self.filename = '/Users/yanchunyang/Documents/highschools/scripts/analysis/verbs.txt'
		self.database = 'activewords'
		self.theme = ''

	def read_basicwords(self):
		with open(self.filename, 'r') as f:
			i = 0
			for line in f.readlines():
				i += 1
				splits = line.strip().split('\t')
				for item in splits:
					if len(item)>0:
						self.words.append(item)
						self.word_class[item] = i 
		self.obtain_cn()
							
			
			#self.obtain_cn()

			
	def obtain_cn(self):
		self.d = enchant.Dict("en_US")
		for item in self.words:
			if self.d.check(item):
				cn = ''
				syns = wn.synsets(item)
				for subitem in syns:
					name = subitem.name()
					result = wn.synset(name).lemma_names('cmn')
					for r in result:
						cn = cn + ' ' + r
				self.word_cn[item] = cn 
			else:
				self.word_cn[item] =" "
		self.write_mysql()
		

	def write_mysql(self):
		connection = pymysql.connect(host='localhost', user='root', password='sunnyvale2016', db='words')
		try:
			with connection.cursor() as cursor:
				for word in self.words:
					sql = """INSERT INTO `activewords` (`word_class`,`word`, `word_cn`) VALUES (%s, %s, %s)"""
					try:
						cursor.execute(sql, (self.word_class[word], word, self.word_cn[word].encode(encoding='utf8', errors='ignore')))
					except Exception as inst:
						print(type(inst))
						print(isnt.args)
						print(word+self.word_cn[word])
						continue
					
			connection.commit()
		except:
			print("Error")
		finally:
			connection.close()


def main():
	handle = handle_word()
	handle.read_basicwords()
	

if __name__ == '__main__':
	main()