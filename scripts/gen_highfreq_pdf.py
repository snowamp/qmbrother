#generate the pdf for png
from fpdf import FPDF 
import os
import sys

pdf = FPDF()

path = '../wheels/'

filenames = []

for filename in os.listdir(path):
	if '.png' in filename and 'cover' not in filename:
		filenames.append(filename)

for item in filenames:
	index = item.index('.')
	covername = item[0:index]+'_cover'+'.png'
	pdf.add_page()
	pdf.image(os.path.join(path, item), w=170)
	pdf.image(os.path.join(path,covername), w=170)

pdf.output("../wheels/test.pdf", 'F')
