# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
from urllib.request import urlopen
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from wand.image import Image 

def download(path, terms, helpterm):

    browser = webdriver.Chrome()

    
    for searchterm in terms:
        #searchterm = 'Pier39' # will also be the name of the folder
        combineterm = searchterm + ' ' + helpterm
        url = "https://www.google.co.in/search?q=" + combineterm + "&source=lnms&tbm=isch"
        #chrome_options = Options()
        #chrome_options.add_argument("user-data-dir=/Users/yanchunyang/Library/Application Support/Google/Chrome/Default")
        #browser = webdriver.Chrome()
        browser.get(url)
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        counter = 0
        succounter = 0

        '''
        if not os.path.exists(searchterm):
            os.mkdir(searchterm)
        '''
        

        '''
        for _ in range(2):
            browser.execute_script("window.scrollBy(0,100)")
            #browser.execute_script("window.scrollBy(0,10000)")
        '''
        for x in browser.find_elements_by_xpath("//div[@class='rg_meta']"):
            counter = counter + 1
            if counter > 15:
                break
            print("Total Count:"+str(counter))
            print("Succsessful Count:"+str(succounter))
            print ("URL:"+json.loads(x.get_attribute('innerHTML'))["ou"])

            img = json.loads(x.get_attribute('innerHTML'))["ou"]
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
            try:
                req = urlopen(img)
                output = open(os.path.join(path , searchterm + "_" + str(counter) + "." + imgtype), "wb")
                output.write(req.read())
                output.close()
                succounter = succounter + 1
            except:
                    print("can't get img")

        print(str(succounter)+"pictures succesfully downloaded")
    browser.close()

def convert_img(path):
    
    for filename in os.listdir(path):
            index = filename.find('.')
            if len(filename) == index + 1:
                os.rename(os.path.join(path,filename), os.path.join(path,filename+'jpg'))


    for filename in os.listdir(path):
        index = filename.find('.')
        if filename[index+1:] in ('jpeg', 'jpg', 'png') and 'thumbnail' not in filename:
            try:
                with Image(filename = os.path.join(path, filename)) as img:
                    if img.size[0] > 400 and img.size[1] > 400:
                        img.resize(60, 60)
                        tmp =filename[0:index] + '_' +'thumbnail' + '.'+filename[index+1:]
                        img.save(filename = os.path.join(path, tmp))
            except:
                print(Exception(" error"))
                pass














