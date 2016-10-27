from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import os
import sys

filename = sys.argv[1]
content = {}
path = "/Users/yanchunyang/Documents/highschools/k9/"
path_txt = "/Users/yanchunyang/Documents/highschools/k9_txt/"

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


def list_files():

    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path,name)):
            filename.append(name)
    return

def get_string():

    i = 0
    
    
    try:
        newpath = os.path.join(path,filename)
        pdfFile = open(newpath, 'rb')
        outputString = readPDF(pdfFile)
        pdfFile.close()
        content[name] = outputString
        i += 1
            
        print(outputString)
    except:
        print("error")
    
    print(i)
    return

#local file
#pdfFile = open("../pages/warandpeace/chapter1.pdf", 'rb')

#translate the pdf



def main():
    #list_files()
    get_string()
    



if __name__ == "__main__":
    main()









