#get enchant word categories

from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import wget
import os


path = "/Users/yanchunyang/Documents/highschools/text/"
def get_urlList():
	siteUrl = "http://textfiles.com/stories/"
	indexVocabulary = {}
	urlList = {}
	html = urlopen(siteUrl)
	domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
	bsObj = BeautifulSoup(html, "html.parser")
	alink = bsObj.findAll("a", href = re.compile("/*.txt"))
	for link in alink:
		#print(link.attrs['href'])
		urlList[link.attrs['href']] = domain+'/stories/'+link.attrs['href']
	for key in urlList.keys():
		urlretrieve(urlList[key], os.path.join('../text/', key))
		
'''
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
'''

def main():
	get_urlList()

if __name__ == '__main__':
	main()