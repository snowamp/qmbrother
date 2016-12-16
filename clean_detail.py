import sys
import os
import re



def clean_file(filename):
	
	try:
		filename_1 = "./detail/"+filename
		f = open(filename_1, 'r+')
		g = open("./detail_org/"+filename, 'w+')
		for line in f.readlines():
			if len(line.strip()) == 0:
				continue
			else:
				line = re.sub("^\s", "", line.strip())
				line = re.sub("\s\s+", " ", line)
				if line in ["References[edit]", "Retrieved from", "Navigation menu"]:
					break
				g.write(line+'\n')
		f.close()
		g.close()


	except:
		print "error"


def get_file():

	filelist = os.listdir("./detail")
	for item in filelist:
		if item.endswith(".txt"):
			clean_file(item)

def get_file_test():
	filename = "Worcester_Academy_Massachusetts.txt"
	clean_file(filename)

def main():
	#get_file()
	get_file()

if __name__ == "__main__":
	main()

