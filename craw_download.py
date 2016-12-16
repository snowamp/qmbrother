from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import os

html = []
for i in range(1, 14):
	html.append("https://freekidsbooks.org/?page="+str(i))


for ht in html:
	page = urlopen(ht)
	bsObj = BeautifulSoup(page, "html.parser")
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+")")):
		if(link.attrs['href'].startswith("/download/")):
			temp = "https://freekidsbooks.org"+link.attrs['href']
			os.system('wget %s' % temp)
			print(temp)


			

