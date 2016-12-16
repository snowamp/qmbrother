from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

#pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf");

pdfFile = open("/Users/yanchunyang/Documents/highschools/k9/6.pdf", 'rb')
outputString = readPDF(pdfFile)
pdfFile.close()

#local file
#pdfFile = open("../pages/warandpeace/chapter1.pdf", 'rb')

#translate the pdf
print("read over")

print(outputString)