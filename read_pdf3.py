from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from microsofttranslator import Translator

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

pdfFile = open("/Users/yanchunyang/Documents/kidscode/ScratchReferenceGuide.pdf", 'rb')
outputString = readPDF(pdfFile)
pdfFile.close()

#local file
#pdfFile = open("../pages/warandpeace/chapter1.pdf", 'rb')

#translate the pdf
print("read over")
client_id = "boliu"
client_secret = "pwfbBe660uJoi0yQrfyCurzfhoXYsNRkXhmaocNKInY="
translator = Translator(client_id, client_secret)

outputlist = outputString.split('\n')

fname = open("Reference.txt", 'w+')

for line in outputlist:
	if len(line)> 10:
		try:
			translate_text = translator.translate(line, 'zh-CHS', 'en')
			fname.write(translate_text+'\n')
		except:
			print("error")
fname.close()
