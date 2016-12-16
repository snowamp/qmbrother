# get the active verb lists

from PyPDF2 import PdfFileReader
import re
import sys
from collections import defaultdict

words = []
active = []
activewords = defaultdict(list)

def readpdf():
	filename = './analysis/Active-Verbs-List.pdf'
	input1 = PdfFileReader(filename, "rb")
	totalpages = input1.getNumPages()
	for i in range(totalpages-1):
		temppage = input1.getPage(i)
		clean(temppage.extractText())
	with open('./analysis/mainverbs.txt') as f:
		temp = []
		for line in f.readlines():
			if len(line.strip()) > 0:
				active.append(line.strip())
	

def clean(text):
	splits = text.split('\n')
	subwords = []
	p = re.compile('[A-Z][a-z]*[\s]*[a-z]*')
	for line in splits:
		if 'Angela' in line:
			index = line.index('Angela')
			if len(line[:index-2])>0:
				words.append(line[:index-2])
			break
		if '(see' in line or 'ACTIVE VERBS LIST' in line:
			continue
		if len(line.strip())>0:
			result = re.findall(p, line.strip())
			for item in result:
				words.append(item)

def combine():
	temp = ''
	active_1 = sorted(active)
	pos = active_1.index('play')
	active_1[pos]= 'pick'
	active_1[pos-1] = 'play'

	print(active_1)
	first = ''
	second = ''
	i = 0
	second = active_1[0]
	
	for item in words:
		if item.lower() != second:
			activewords[first].append(item)
		else:
			first = second
			i += 1
			if i < len(active_1):
				second = active_1[i]
			else:
				second = ""
			activewords[first].append(item)

	g = open('./analysis/verbs.txt', 'w')
	for key in sorted(activewords.keys()):
		for item in activewords[key]:
			g.write(item+'\t')
		g.write('\n')
	g.close()
	
	'''
	for item in words:
		if item.lower() in active:
			sys.stdout.write('\n')
			sys.stdout.write(item+'   ')
		else:
			sys.stdout.write(item+ '   ')
	'''

def main():
	readpdf()
	combine()

if __name__ == '__main__':
	main()


