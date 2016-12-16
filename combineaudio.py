import os
import sys
from pydub import AudioSegment

fileinwait = []
filelist = []

for filename in os.listdir("../audio/"):
	if '_0.wav' in filename:
		fileinwait.append(filename[:-5])

	filelist.append(filename)

for item in fileinwait:
	temp = item+'0.wav'
	combine = AudioSegment.from_wav("../audio/"+temp)
	i = 1
	while item + str(i) +'.wav' in filelist:
		print(item+str(i)+'.wav')
		combine = combine + AudioSegment.from_wav("../audio/"+item+ str(i) +'.wav')
		i += 1
	combine.export("../audio/"+item+'_combine'+'.wav', format = "wav")
	print("item done")