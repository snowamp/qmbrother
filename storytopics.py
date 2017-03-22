##################################################
# This is a code to present the story of topics
#
##################################################
import os

ideas = []
pics = []

with open('../writing_skills/kidideas.txt', 'r') as f:
	for line in f.readlines():
		if len(line) < 2:
			continue
		ideas.append(line.strip())

path = '/Users/lxb/Documents/yyc/scripts/booksproject/pics/'

for filename in os.listdir(path):
	if 'jpg' in filename or 'png' in filename or 'jpeg' in filename:
		pics.append(filename)

c = 0
with open('comicnote.txt', 'w+') as g:
	i = 0
	while i < len(ideas):
		g.write('\\textblockorigin{0cm}{0cm}\n')
		g.write('\\begin{textblock*}{10cm}(7cm, 6cm)\n')
		g.write('\Cloud{0}{0}{')
		g.write(ideas[i] + '}{'+ os.path.join(path,pics[c]) + '}\n')
		g.write('\end{textblock*}\n')
		c += 1
		if c == len(pics):
			c = 0

		if i + 1 < len(ideas):
			i += 1
			g.write('\\begin{textblock*}{10cm}(14cm, 13cm)\n')
			g.write('\Cloud{0}{0}{')
			g.write(ideas[i] + '}{'+ os.path.join(path,pics[c]) + '}\n')
			g.write('\end{textblock*}\n')
			c += 1
			if c == len(pics):
				c = 0

		if i + 1 < len(ideas):
			i += 1
			g.write('\\begin{textblock*}{10cm}(7cm, 20cm)\n')
			g.write('\Cloud{0}{0}{')
			g.write(ideas[i] + '}{'+ os.path.join(path,pics[c]) + '}\n')
			g.write('\end{textblock*}\n')
			c += 1
			if c == len(pics):
				c = 0

		i += 1
		g.write('\\null\\newpage\n')




