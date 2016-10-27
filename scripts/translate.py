import os
import re
from microsofttranslator import Translator
import sys

client_id = "boliu"
client_secret = "pwfbBe660uJoi0yQrfyCurzfhoXYsNRkXhmaocNKInY="
translator = Translator(client_id, client_secret)

def translate(filename):
	print(filename)
	f = open("./detail_org/" + filename, 'r+')
	g = open("./detail_org_ch/ch_" + filename, 'w+')
	for line in f.readlines():
		line = line.strip()
		trans_line = translator.translate(line, 'zh-CHS', 'en')
		g.write(trans_line + '\n')

	f.close()
	g.close()


def get_file():

	filelist = os.listdir("./detail_org")
	for item in filelist:
		if item.endswith(".txt"):
			translate(item)

def get_file_test():
	filename = "Worcester_Academy_Massachusetts.txt"
	translate(filename)



def main():
	#get_file()
	get_file()

if __name__ == "__main__":
	main()