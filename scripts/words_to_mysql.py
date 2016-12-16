
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

	def read_basicwords(self):
		with open('highfreq.txt', 'r') as f:
			splits = f.readline().split(' ')
			for item in splits:
				if len(item) > 0:
					self.words.append(item.strip())
			print(len(self.words))
			
	

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
		

	def write_mysql(self):
		connection = pymysql.connect(host='localhost', user='root', password='sunnyvale2016', db='words',charset='utf8mb4')
		try:
			with connection.cursor() as cursor:
				for word in self.words:
					sql = """INSERT INTO `basicwords` (`words`, `words_cn`) VALUES (%s, %s)"""
					try:
						cursor.execute(sql, (word, self.word_cn[word].encode(encoding='utf8', errors='ignore')))
					except:
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
	handle.obtain_cn()
	handle.write_mysql()

if __name__ == '__main__':
	main()