from PyPDF2 import PdfFileWriter, PdfFileReader


infile = PdfFileReader('dummy.pdf', 'rb')
infile2 = PdfFileReader('dummy2.pdf', 'rb')
output = PdfFileWriter()

p2 = infile2.getPage(0)

for i in xrange(infile.getNumPages()):
    p = infile.getPage(i)
    output.addPage(p)
    if i == 3:
        output.addPage(p2)

with open('newfile.pdf', 'wb') as f:
   output.write(f)