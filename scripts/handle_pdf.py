# this code need be run under python3

import os
import re
import sys
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urlparse
from bs4 import BeautifulSoup


url = 'http://web.eecs.umich.edu/~radev/coursera-slides/'
destination = '../NLPpdffile/'
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
try:
    includeUrl = urlparse(url).scheme + "://" + urlparse(url).netloc + '/' #get the main part of the website
    print(includeUrl)
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("nlpintro_.*pdf")): #begin with / or include main part of website
                if link.attrs['href'] is not None:
                    internalLinks.append(url+link.attrs['href'])
                    
                      
except:
    sys.exit("getinternallink wrong")
        
i= 0
for item in internalLinks:
	print(item)
	urlretrieve(item, destination+item[-30:]+".pdf")