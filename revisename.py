import os

path = os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
	if filename[-1] != 'y':
		os.rename(filename, filename+".pdf")