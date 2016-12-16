#call the youtube audio

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyaudio, wave, sys
import time
import numpy as np
import array
import struct

youtubelink = []
youtubename = []
try:
    f = open('readlist.txt', 'r')
    for line in f.readlines():
        if len(line.strip()) == 0:
            continue
        splits = line.strip().split('\t')
        youtubelink.append(splits[0])
        youtubename.append(splits[1])
    f.close()
except:
    print("file not open correctly")



chrome_options = Options()
chrome_options.add_argument("user-data-dir=/Users/yanchunyang/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(chrome_options=chrome_options)


for i in range(len(youtubelink)):
    driver.get(youtubelink[i])
    print(youtubelink[i])
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'element_id'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    oldpage = driver.current_url
    newpage = oldpage


    CHUNK = 8192
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 240

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE,input = True,input_device_index = 5,frames_per_buffer = CHUNK)
    print("* recording")

    flag = 0
    total = []
    while oldpage == newpage and flag == 0:
        print(newpage)
        #frames = []
        frames = array.array('f')
        for k in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            #data = stream.read(CHUNK)
            #frames.append(data)
            frames.fromstring(stream.read(CHUNK))
            if k % 49 == 0:
                newpage = driver.current_url
                if oldpage != newpage:
                    flag = 1
                    break
        total.append(frames)
    

    print(youtubelink[i])

    print("* done recording")
    stream.stop_stream()    # "Stop Audio Recording
    stream.close()          # "Close Audio Recording
    p.terminate()  
    if len(total) > 0:
        for j in range(len(total)):
            WAVE_OUTPUT_FILENAME = youtubename[i]+'_Audio_'+str(j)+'.wav'
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            buf = struct.pack('%sf' % len(total[j]), *total[j])
            wf.writeframes(buf)
            wf.close()

driver.close()
print("End of recording")

