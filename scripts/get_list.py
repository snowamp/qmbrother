from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
from urlparse import urlparse
from bs4 import BeautifulSoup
import re
import sys
import os

def statesCategory():

	stateslink = []
	try:
		html = urlopen("https://en.wikipedia.org/wiki/Category:Private_high_schools_in_the_United_States_by_state")
		bsObj = BeautifulSoup(html.read())
		hreflist = bsObj.findAll("a", {"href":re.compile("/wiki/Category:Private_high_schools_in_\.*")})
		i = 0
		for item in hreflist:
			i += 1
			if i <= 51:
				tempitem = item["href"].strip()
				stateslink.append(tempitem)
		
	except HTTPError as e:
		print(e)
	except URLError as e:
		print("The server could not be found!")
	else:
		pass
		#print("It worked!")
	return stateslink

def schoolCategory(url):
	schoollinks = []
	try:
		html = urlopen("http://en.wikipedia.org" + url)
		bsObj = BeautifulSoup(html.read())
		for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
			if 'href' in link.attrs:
				if 'Main_Page' not in link.attrs['href']:
					schoollinks.append(link.attrs['href'])
#					print(link.attrs['href'])
	except HTTPError as e:
		print(e)
	except URLError as e:
		print("The server could not be found")
	else:
		pass
		#print("schoolCategory worked!")
	return schoollinks

def get_school_infor(url, statename, toFile):
	externalLinks = []
	filename = statename +".txt"
	try:
		html = urlopen("http://en.wikipedia.org" + url)
		bsObj = BeautifulSoup(html.read())
		schoolname = bsObj.find("h1").get_text()
		description = bsObj.body.get_text().encode('utf-8')
		links = bsObj.findAll("a", {"class" : "external text"})
		
		for item in links:
			if (item.attrs['href'] is not None) and ("http" in item['href'] or "www" in item['href']):
				tmp = urlparse(item.attrs['href']).scheme + "://" + urlparse(item.attrs['href']).netloc
				if tmp not in externalLinks:
					externalLinks.append(tmp)
		toFile.write(schoolname.encode('utf-8')+ '\t')
		if len(externalLinks) > 0:
			toFile.write(externalLinks[0].encode('utf-8') + '\n')
		else:
			toFile.write('\n')

	except HTTPError as e:
		toFile.write('\n')
	except URLError as e:
		toFile.write('\n')
	else:
		toFile.write('\n')

def main():
	
	stateschool = {}
	stateslink = statesCategory()
	for item in stateslink:
		statesname = item[39:len(item)]
		templist = schoolCategory(item)
		stateschool[statesname] = templist
	total = 0

	for key in stateschool.keys():
		total += len(stateschool[key])
		filename = key + ".txt"
		f = open(filename, "w+")
		for subitem in stateschool[key]:
			get_school_infor(subitem, key, f)
		f.close()
	
	
	
	


if __name__ == "__main__":
	main()