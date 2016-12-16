
import os
import re
from microsofttranslator import Translator
import sys
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Application():
    def __init__(self,para):
        
        self.allIntLinks = set()  #save all the links for the websites
        self.count = 0    #save how many inner websites for this website
        self.current = 1    #save current sub link
        self.currentpage = 0 #save current page for the sub_link
        self.content = []   #save the content of the sub_link
        self.volume = 40  #save the text lines for each text widges
        self.weblinkdic = {} #code the subweblink
        self.linkcount = int(para[1])
        self.link = para[2]
        self.client_id = "boliu"
        self.client_secret = "pwfbBe660uJoi0yQrfyCurzfhoXYsNRkXhmaocNKInY="
        

    
    def getAllInternalLinks(self,siteUrl):

        if len(self.allIntLinks) > 200:
            return

        try:
            print(siteUrl)
            html = urlopen(siteUrl)
            domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc # get the main part of the website
            bsObj = BeautifulSoup(html, "html.parser")
            internalLinks = self.getInternalLinks(bsObj,domain)
            print(len(internalLinks))

            if len(internalLinks)>0:
                for link in internalLinks:
                    if link not in self.allIntLinks:
                        self.allIntLinks.add(link)
                        self.count += 1  #total website count increase one
                        self.weblinkdic[self.count] = link
                        self.getAllInternalLinks(link)  #recursive search the links
                    
        except:
            return
        return

    def getInternalLinks(self, bsObj, includeUrl):
        internalLinks = []
        try:
            includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc #get the main part of the website 
            for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")): #begin with / or include main part of website
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in internalLinks:
                        if(link.attrs['href'].startswith("/")):
                            internalLinks.append(includeUrl+link.attrs['href'])
                        else:
                            internalLinks.append(link.attrs['href'])
        except:
            return internalLinks
        return internalLinks

    def translate(self):

        #prepare the translate environment
        
        translator = Translator(self.client_id, self.client_secret)

        #prepare the phantom server
        driver = webdriver.PhantomJS()
        print("server ready")
        for i in range(1,self.linkcount+1):
            link = self.weblinkdic[i]
        
            driver.get(link)
            time.sleep(3)
            print("get link")
            description = driver.find_element_by_tag_name("body").text
            
            print(link)
            g = open("../translate/" +str(i)+".txt", 'w+')
            for line in description.split('\n'):
                if len(line)>5:
                    line = line.strip()
                    try:
                        trans_line = translator.translate(line, 'zh-CHS', 'en')
                    except:
                        sys.exit("Error message")
                    g.write(line + '\n')
                    g.write(trans_line + '\n')

            g.close()

        driver.close()
        return


    

print(sys.argv[1])
print(sys.argv[2])
app = Application(sys.argv)
app.getAllInternalLinks(sys.argv[2])
app.translate()
print("Run Done")


'''
        self.userpasswd = {"boliu":"pwfbBe660uJoi0yQrfyCurzfhoXYsNRkXhmaocNKInY=", "shiguangyang@hotmail.com":"rJB5LJCcYxMHS9aVae2rNPrUr3ouKBy1Ac8pTKdUvi4=", 
        "yanchunyang@hotmail.com":"WKWl9s710GB7g08fC8H3ilnSgEipvF8YaZI6YsgHOdE=", "jieyang_jerry@outlook.com":
        "aYphOd7GUpKGBoO9Uu+dsyZlY0VTjaOGC0uRwHCnyus="}
'''
        

