#########################################
#Generate the word products for one book
#Include New words cards
#And Word hunt
#And Word net
#And verbs and adj
#Some questions 
#Some Funny sentences
#And Word Wheels
# Must pay attention to readline encoding problem, sometime it is coded as ISO-8859-1
##########################################

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
from editDistance import Solution

def aquire_text(path):
	filename = os.path.join(path, 'picscontent.txt')
	replacer = RegexpReplacer()
	content = ''
	with open(filename, 'r', encoding = "ISO-8859-1") as f:
		for line in f.readlines():
			if len(line) < 2 or '.jpg' in line or '.png' in line:
				continue
			else:
				content = content + ' ' + line.strip()
	words = word_count(content)
	singlewords = []
	for key in words.keys():
		singlewords.append(key)
	content_update = replacer.replace(content)
	content_sent = sent_tokenize(content_update)
	words_content = []
	for item in content_sent:
		words_content.append(nltk.pos_tag(word_tokenize(item)))
#to generate word card
	word_list(words, path)
#to classify word by tag class
	word_classify(words_content, words, path)

# to get the vowel of words
	find_vowel(singlewords, path)

# to get the distance of words
	word_distance(singlewords, path)


def word_classify(words_content, words, path):
	words_total = [val for sublist in words_content for val in sublist]
	words_class = {}
	others = []
	orders = {'VB':0, 'NN':1, 'MD':2, 'JJ':3, 'RB':4, 'RP':5, 'PR':6,'DT':7}
	for word in words_total:
		if word[0] in words.keys() and word[1][0:2] in orders.keys():
			if word[0] in words_class:
				if orders[word[1][0:2]] < orders[words_class[word[0]]]:
					words_class[word[0]] = word[1][0:2]
			else:
				words_class[word[0]] = word[1][0:2]
		else:
			others.append(word)
	with open(os.path.join(path, 'wordclass.txt'), 'w+') as g:
		for key in orders.keys():
			g.write(key + '\n')
			for word_key in words_class.keys():
				if key == words_class[word_key]:
					g.write(word_key + '\t')
			g.write('\n')
	print('word_classify done')






def word_count(context):
	words_count = {}
	transtable = str.maketrans('', '', string.punctuation)
	clean_context = context.translate(transtable)
	words = clean_context.split(' ')

	for word in words:
		if word.lower() in words_count:
			words_count[word.lower()] += 1
		else:
			words_count[word.lower()] = 1
	return(words_count)

def word_list(words, path):
	basicwords = {}
	with open('../othertxts/basicwords.txt', 'r') as f:
		for line in f.readlines():
			splits = line.strip().split('\t')
			basicwords[splits[0]] = splits[1]

	sortedwords = sorted(words.items(), key=lambda x:x[1], reverse = True)
	with open(os.path.join(path,'word_list.txt'), 'w+') as g:
		for item in sortedwords:
			if item[0] not in basicwords.keys():
				g.write(item[0] + '\t' + str(item[1]) + '\t' + 'not'  + '\t' + '\n')
			else:
				g.write(item[0] + '\t' + str(item[1]) + '\t' + 'yes' + '\t' + basicwords[item[0]] + '\n')
	print("word_list done")
	
def find_vowel(singlewords, path):
	compound = ['ee', 'ea', 'ie', 'ei', 'er', 'ur', 'ir', 'or', 'ar', 'ear', 'ai', 'ay', 'ey', 'uy', 'ou', 'ow', 'aw', 'au','ought', 'al', 'oi'\
	'ew', 'eu', 'ue', 'ui']
	single = [ 'e e', 'a e', 'i e', 'o e', 'u e']

	vowelcompound = defaultdict(list)

	vowel = {'i:':['ee', 'ea', 'ie', 'ei', 'e e'], '&r':['er', 'ur', 'ir', 'or', 'ar', 'ear'], 'e':['ea', 'e e'], 'ei':['ai', 'ay', 'ei', 'ey', 'ea', 'a e'],\
			'a:':['ar'], 'ai':['ie', 'uy'], 'au':['ou', 'ow'], 'o:':['aw', 'au', 'ought', 'al', 'o e'], 'oi':['oi', 'oy'], 'ou':['oa', 'ow'],\
			'yu:':['ew', 'eu', 'ue', 'ui','ou'], 'u':['oo', 'ou', 'o e', 'u e']}


	words_vowel = defaultdict(list)
	for w in singlewords:
		for item in compound:
			if item in w:
				words_vowel[item].append(w)
		for item in single:
			p = re.compile(item[0]+'[b-z]'+item[-1])
			if p.search(w):
				words_vowel[item].append(w)


	for key in vowel:
		for item in vowel[key]:
			vowelcompound[item].append(key)

	with open(os.path.join(path,'vowelwords.txt'), 'w+') as g:
		for key in words_vowel.keys():
			for item in words_vowel[key]:
				g.write(key+'\t')
				for j in vowelcompound[key]:
					g.write(j+'\t')
				g.write(item+'\n')
	print("find vowel done")

class node:
	def __init__(self, k):
		self.index = k
		self.flag = 0
class printnode:
	def __init__(self, word, parent, index):
		self.word = word 
		self.parent = parent
		self.index = index

def get_maxlength(sublist):
	maxlength = 0
	for itm in sublist:
		if len(itm) > maxlength:
			maxlength = len(itm)

	return(maxlength)

def connect_words(i, distance):
	temp = []
	if i not in distance.keys():
		return([[i]])
	for item in distance[i]:
		if item.flag == 0:
			item.flag = 1
			result = connect_words(item.index, distance)
			for sub in result:
				temp.append([i]+sub)
	if len(temp) == 0:
		return([[i]])
	return(temp)

def word_distance(words, path):
	distance = defaultdict(list)
	wordlist = []
	linkresult = []
	for i in range(0, len(words)-1):
		for j in range(i+1, len(words)):
			if Solution().minDistance(words[i], words[j]) == 1:
				distance[i].append(node(j))

	for key in distance.keys():
		wordlist.append(key)
	wordlist = sorted(wordlist)

	for i in wordlist:
		result = connect_words(i, distance)
		if len(result) > 1:
			linkresult.append(result)

	combineresult = {}

	for item in linkresult:
		
		total = {}
		
		first = item[0][0]
		total[first] = 1
		combineresult[first] = []
		combineresult[first].append(printnode(item[0][0], 0, 1))
		maxlength = get_maxlength(item)
		for i in range(1, maxlength):
			subtemp = []
			for point in item:
				if i < len(point) and (point[i] not in subtemp) and (point[i] not in total.keys()):
					subtemp.append(point[i])
					index = str(i)+str(len(subtemp) + 1)
					total[point[i]] = index 
					combineresult[first].append(printnode(point[i], total[point[i-1]], index))


	


	with open(os.path.join(path, 'linkresult.txt'), 'w+') as g:
		for key in combineresult:
			g.write(words[key] + '\t')
			for sub in combineresult[key]:
				g.write(words[sub.word]+':'+ str(sub.parent) +':' + str(sub.index) + '\t')
			g.write('\n')
	print("word_distance done")


def main():
	aquire_text('../millioncats/')

if __name__ == '__main__':
	main()


