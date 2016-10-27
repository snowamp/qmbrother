import sys
import os

name = os.listdir('./detail_org_ch')

namelist = []

for item in name:
	if ".txt" in item:
		namelist.append(item)



f = open("revised_goodlinkwithweb.txt", 'r')

for line in f.readlines():
	splits = line.strip().split('\t')
	subname = splits[0].split(" ")
	realname = subname[0]
	for t in subname[1:]:
		realname += "_"+t
	flag = 0
	for item in namelist:
		if realname in item:
			sys.stdout.write(item+'\t')
			sys.stdout.write(splits[-1] + '\n')
			flag = 1
			break
	if flag == 0:
		sys.stdout.write(line)	
		
	

f.close()




