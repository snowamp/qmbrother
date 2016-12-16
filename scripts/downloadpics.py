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

nnp_file = '../princess/wordcandidate.txt'
with open(nnp_file, 'r') as f:
    terms = f.readline().strip().split('\t')

browser = webdriver.Chrome()

for searchterm in terms:
    #searchterm = 'Pier39' # will also be the name of the folder
    helpterm = 'Disney Princess'
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
    path = '../princess/img/'

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














