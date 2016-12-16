# recording the audio 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyaudio, wave, sys
import time

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 200
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE,input = True,input_device_index = 5,frames_per_buffer = CHUNK)

total = []
for i in range(0,2):
    frames = []
    for k in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    total.append(frames)
        

print("* done recording")
stream.stop_stream()    # "Stop Audio Recording
stream.close()          # "Close Audio Recording
p.terminate()           # "Audio System Close

    
for j in range(len(total)):
    WAVE_OUTPUT_FILENAME = 'new'+'_Audio_'+str(j)+'.wav'
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(total[j]))
    wf.close()

print('done')