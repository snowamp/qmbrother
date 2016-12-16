import os
import re
from nltk.tokenize import sent_tokenize
from replacers import RegexpReplacer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
from nltk.stem import LancasterStemmer

filename = []
outputstring = ""
secondoutput = ""
wordlist = {}


f = open("picturebooks.txt", 'r')

flag = 0

replacer = RegexpReplacer()
tokenizer = RegexpTokenizer("[\w']+")

for line in f.readlines():
	line = line.strip()
	line = replacer.replace(line)
	if not line:
		continue

	if 'pdf' in line:
		filename.append(line)
		
	elif 'www' in line:
		continue
	elif 'the end' in line.lower() or 'about the author' in line.lower() or 'more books' in line.lower():
		continue

	else:
		if len(line) >= 2:
			outputstring += " "+line
		
f.close()

#g1 = open("effective.txt", 'w+')
#g2 = open("ineffective.txt", 'w+')

stemmer = LancasterStemmer()

j = 0
sents = sent_tokenize(outputstring)
for item in sents:
	words = tokenizer.tokenize(item)
	for word_un in words:
		word = stemmer.stem(word_un)
		try:
			temp = wordnet.synsets(word.lower())
			if temp:
				if word.lower() in wordlist:
					wordlist[word.lower()] += 1
				else:
					wordlist[word.lower()] = 1
			#else:
				#g2.write(word+'\t')
		except:
			print(word)
		
	

#g1.close()
#g2.close()
g1 = open("effective.txt", 'w+')
for key, value in [(k,wordlist[k]) for k in sorted(wordlist, key=wordlist.get)]: 
	g1.write(key+":"+'\t')
	g1.write(str(wordlist[key]))
	g1.write('\n')
	
g1.close()

print(len(sents))
print(j)

print("over")

