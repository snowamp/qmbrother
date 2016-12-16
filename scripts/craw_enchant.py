#get enchant word categories

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


def get_urlList():
	siteUrl = "http://www.enchantedlearning.com/wordlist/"
	indexVocabulary = {}
	urlList = []
	html = urlopen(siteUrl)
	domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
	bsObj = BeautifulSoup(html, "html.parser")
	alink = bsObj.findAll("a", href = re.compile("/wordlist/.*.shtml"))
	for link in alink:
		urlList.append(domain+link.attrs['href'])
	urlList = urlList[1:]
	for link in urlList:
		get_wordlist(link)
		

def analysis(text):
	word = []
	splits = text.split('\n')
	for sub in splits:
		if len(sub) > 0:
			sep_word = sub.split(',')
			for ss in sep_word:
				if len(ss) < 10 and re.match(re.compile('^[a-z]'), ss):
					word.append(ss)
	return(word)
	




def get_wordlist(link):
	print(link)
	html = urlopen(link)
	index = link.find('wordlist/')
	name = link[index+8:]
	bsObj = BeautifulSoup(html, "html.parser")
	table = bsObj.findAll("table", {'width': '100%'})
	with open('../vocabulary/'+name+'.txt', 'w') as f:
		for subtable in table:
			for sub in subtable.children:
				text = sub.get_text()
				t = analysis(text)
				for item in t:
					f.write(item)
					f.write('\n')


def main():
	get_urlList()

if __name__ == '__main__':
	main()