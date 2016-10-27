import sys
import re
import os

# this is a classic common substring problem
def compare(s1, s2):
	i = 0
	j = 0
	
	while i < len(s1) and j < len(s2):
		if s1[i] == s2[j]:
			i += 1
			j += 1
		else:
			i += 1
	if j < len(s2)-2:
		return False
	else:
		return True



f_right = open("goodlink.txt", "w+")
f_mistake = open("badlink.txt", "w+")
f_blank = open("blanklink.txt", "w+")

for line in sys.stdin:
	splits = line.strip().split('\t')
	if len(splits) == 0:
		continue
	elif len(splits) == 1:
		f_blank.write(line)
	elif len(splits) == 2:
		# handle the weblink
		subsplits = splits[1].split('.')
		analysis_string = subsplits[1]
		i = 2
		while i < len(subsplits) -1:
			analysis_string = analysis_string.join(subsplits[i])
			i += 1
		if compare(splits[0].lower(), analysis_string.lower()):
			f_right.write(line)
		else:
			f_mistake.write(line)
	else:
		f_mistake.write(line)

f_right.close()
f_mistake.close()
f_blank.close()
		
