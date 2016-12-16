import sys
import os
import shutil

statesname = []

f = open("statesname.txt", 'r')

for line in f.readlines():
	splits = line.strip().split('\t')
	statesname += splits

f.close()

#print statesname
'''
filename = os.listdir('./detail_org_ch')


for item in  filename:
	if '.txt' in item:
		for state_name in statesname:
			if state_name in item:
				shutil.copy('./detail_org_ch/'+item, './'+state_name+'/')
'''

for item in statesname:
	shutil.move('./'+item, './States/')