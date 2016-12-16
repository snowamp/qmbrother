import speech_recognition as sr
from pprint import pprint


audiofile = "/Users/yanchunyang/Documents/Michaels/audio/kidsproject/afternoon_on_amazon.wav"
r = sr.Recognizer()
with sr.AudioFile(audiofile) as source:
	audio = r.record(source)
BING_KEY = "8300bf8c316f40e5adf65488bd8fc395" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Bing recognition results:")
    pprint(r.recognize_bing(audio, key=BING_KEY, show_all=True))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))