from tkinter import *
import os
import re
from microsofttranslator import Translator
import sys
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # to save the public variables for the function
        self.allIntLinks = set()  #save all the links for the websites
        self.count = 0    #save how many inner websites for this website
        self.current = 1    #save current sub link
        self.currentpage = 0 #save current page for the sub_link
        self.content = []   #save the content of the sub_link
        self.volume = 40  #save the text lines for each text widges
        self.weblinkdic = {} #code the subweblink


        self.userpasswd = {"boliu":"pwfbBe660uJoi0yQrfyCurzfhoXYsNRkXhmaocNKInY=", "shiguangyang@hotmail.com":"rJB5LJCcYxMHS9aVae2rNPrUr3ouKBy1Ac8pTKdUvi4=", 
        "yanchunyang@hotmail.com":"WKWl9s710GB7g08fC8H3ilnSgEipvF8YaZI6YsgHOdE=", "jieyang_jerry@outlook.com":
        "aYphOd7GUpKGBoO9Uu+dsyZlY0VTjaOGC0uRwHCnyus="}
        self.master.title('Hello, Tkinter!')
        self.master.geometry('1000x800')
        self.grid()
        self.createWidgets()  #get the main function

    def createWidgets(self):
        #input the website name
        self.inputlabel = Label(self, text="please etner the website")  
        self.inputlabel.grid(row=0, column=0, columnspan=6)
        self.websitename = Entry(self)
        self.websitename.grid(row=1, column=0, columnspan = 6)
        
        #save the input account for translator

        self.selectlabel = Label(self, text="please select the account for translator")
        self.selectlabel.grid(row = 0, column = 14, columnspan = 6)

        #listbox inserted here
        self.variable = StringVar(self)
        self.variable.set("boliu")
        self.droplist = OptionMenu(self, self.variable, "boliu", "yanchunyang@hotmail.com", 
            "shiguangyang@hotmail.com", "jieyang_jerry@outlook.com")
        self.droplist.grid(row=1, column = 14, columnspan=6)

        
        #show current sub website name
        self.subwebsitelabel = Label(self, text="subwebsite")
        self.subwebsitelabel.grid(row = 2, column= 0, columnspan = 4)

        self.subwebsite = Text(self, width = 30, height = 2, wrap=WORD)
        self.subwebsite.grid(row = 3, column = 0, columnspan = 16, sticky = W)

        #button to show the next sub website name
        self.nextsubwebsite = Button(self, text="Next", command = self.nextwebpage)
        self.nextsubwebsite.grid(row = 3, column = 32, columnspan = 1)

        #button to run the whole process
        self.submitwork = Button(self, text="Submit", command = self.submitwork)
        self.submitwork.grid(row=3, column = 34, columnspan = 1)


        #text to show all the result
        self.showresult = Text(self, width = 40, height = self.volume, wrap = WORD)
        self.showresult.grid(row = 4, column = 2, columnspan = 20)

        #button the show the next page
        self.nextpagebutton = Button(self, text="Nextpage", command = self.nextpage)
        self.nextpagebutton.grid(row =44, column = 20, columnspan = 2)

        self.prepagebutton = Button(self, text="prepage", command = self.prepage)
        self.prepagebutton.grid(row =44, column = 16, columnspan = 2)
    
    def nextwebpage(self):
        self.current += 1
        self.content = []
        self.currentpage = 0
        self.showresult.delete(0.0,END)
        self.readcontent()

    # run the real program

    def submitwork(self):
        websitename = self.websitename.get()
        print("extract the innerlink......")
        self.getAllInternalLinks(websitename)
        print("Begin translating.....")
        self.translate()
        print("reading content......")
        self.readcontent()
        
    def getAllInternalLinks(self,siteUrl):
        try:
            html = urlopen(siteUrl)
            domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc # get the main part of the website
            bsObj = BeautifulSoup(html, "html.parser")
            internalLinks = self.getInternalLinks(bsObj,domain)
            for link in internalLinks:
                if link not in self.allIntLinks:
                    self.allIntLinks.add(link)
                    self.count += 1  #total website count increase one
                    self.weblinkdic[self.count] = link
                    #self.translate(bsObj, link)
                    if self.count > 10:
                        return
                    else:
                        self.getAllInternalLinks(link)  #recursive search the links
                    
        except:
            sys.exit("getAllInternalLinks wrong")

    def getInternalLinks(self, bsObj, includeUrl):
        try:
            includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc #get the main part of the website
            internalLinks = []
            for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")): #begin with / or include main part of website
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in internalLinks:
                        if(link.attrs['href'].startswith("/")):
                            internalLinks.append(includeUrl+link.attrs['href'])
                        else:
                            internalLinks.append(link.attrs['href'])
        except:
            sys.exit("getinternallink wrong")
        return internalLinks

    def translate(self):

        #prepare the translate environment
        client_id = self.variable.get()
        client_secret = self.userpasswd[client_id]
        translator = Translator(client_id, client_secret)

        #prepare the phantom server
        #driver = webdriver.PhantomJS()
        #print("server ready")
        for i in range(1,20):
            link = self.weblinkdic[i]
        
            try:
                html = urlopen(link)
                bsObj = BeautifulSoup(html.read())
                description = bsObj.p.get_text().encode('utf-8')
                print(description)
            
                print(link)
                g = open("../translate/" +str(i)+".txt", 'w+')
                for line in description.split('\n'):
                    if len(line)>5:
                        line = line.strip()
                        try:
                            trans_line = translator.translate(line, 'zh-CHS', 'en')
                            g.write(trans_line + '\n')
                        except:
                            sys.exit("Error message")
                        

                g.close()

        
            except:
                sys.exit("Error Message")
        return


    def readcontent(self):

        link = self.weblinkdic[self.current]
        self.subwebsite.delete(0.0,END)
        self.subwebsite.insert(END, link)


        filename = str(self.current)
        f = open("../translate/"+filename+".txt", 'r')
        i = 0
        for line in f.readlines():
            self.content.append(line)
        self.showresult.insert(END,self.content[self.currentpage: self.currentpage+self.volume])  
        self.currentpage += self.volume
        f.close()
        return


    def nextpage(self):
        self.showresult.delete(0.0,END)
        if self.currentpage < len(self.content):
            self.showresult.insert(END,self.content[self.currentpage: min(self.currentpage+self.volume, len(self.content))])
            self.currentpage = min(self.currentpage+self.volume, len(self.content))
        else:
            return
    def prepage(self):
        self.showresult.delete(0.0,END)
        if self.currentpage > 0:
            self.showresult.insert(END,self.content[max(self.currentpage-self.volume, 0): self.currentpage])
            self.currentpage = max(self.currentpage-self.volume, 0)
        else:
            return

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
