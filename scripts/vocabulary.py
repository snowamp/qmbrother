import os
import sys


vocab = {}

path = '/Users/yanchunyang/Documents/highschools/vocabulary/'

filename = []


for name in  os.listdir(path):
	filename.append(name)


for item in filename:
	f = open(os.path.join(path,item), 'r+')
	words = []
	for line in f.readlines():
		if len(line) > 0:
			words.append(line.strip().lower())
	vocab[item] = words


basicwordfile = '/Users/yanchunyang/Documents/highschools/scripts/highfreq.txt'

wordlist = open(basicwordfile,'r').readline().strip().split(' ')

print(len(wordlist))


for item in filename:
	print(item)
	print(str(len(vocab[item])))
	i = 0
	for word in vocab[item]:
		if word in wordlist:
			i += 1
	print(str(i))

print(wordlist)