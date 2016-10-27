import os
import re
from microsofttranslator import Translator
import sys
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.PhantomJS()

link = "http://www.readingrockets.org/article/basic-spelling-vocabulary-list"

driver.get(link)

time.sleep(3)

html = driver.page_source

bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class":"formatted"})

rows = []

words = []

for ta in table:
	for row in ta.findAll("tr"):
		for l in row.findAll('td'):
			for item in l.findAll('br'):
				temp = re.sub(r'<[ ]*[/]{0,1}[ ]*br[ ]*[/]{0,1}>', '  ',str(item))
				temp = re.sub(r'\*', ' ', temp)
				rows.append(temp)
			
f = open("highfreq.txt", 'w+')	
for item in rows:
	for subitem in item.strip().split(' '):
		if len(subitem) > 0 and subitem.strip() not in words:
			words.append(subitem.strip())
			f.write(subitem.strip())
			f.write(' ')

f.close()
print(len(words))
print(words[0:10])
