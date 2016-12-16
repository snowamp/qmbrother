import os
import re


content = {}
filename = []
tempname = ''
outstring = ''
flag = 0
i = 0
f = open('picturebooks.txt', 'r')

for line in f.readlines():
	i += 1
	if len(line) == 0 or flag == 1:
		continue
	if '.pdf' in line.strip():
		if len(tempname) > 0 and len(outstring) > 0:
			filename.append(tempname)
			content[tempname] = outstring
		tempname = line.strip()
		outstring = ''
		flag = 0
	elif 'about author' in line.strip().lower() or 'the end' in line.strip().lower() or 'more books' in line.strip().lower():
		flag = 1
		continue

	else:
		outstring += line.strip()+' '

f.close()

g = open('temp.txt', 'w+')
for key in content:
	g.write(key+'\n')
	g.write(content[key]+'\n')

g.close()

print(i)
print(filename)

