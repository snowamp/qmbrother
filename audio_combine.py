import os
import sys
from pydub import AudioSegment
from aws_polly import get_audio_command
from translate_chinese import translate

file_export = "audiocombine.wav"
trans_export = "translate.txt"
filelist = []
candidate = {}
text = ""

path = '/Users/yanchunyang/Documents/highschools/scripts/hurricanes/'



with open(os.path.join(path, "Englishwords.txt"), 'r') as f:
	tmp = f.read()
	sents = tmp.split('\n')
	for item in sents:
		if len(item) > 0:
			can = item.split('\t')
			candidate[can[0]] = can[1]


with open(os.path.join(path, "order.txt"), 'r') as f:
	for item in f.readlines():
		if len(item) > 0:
			filelist.append(item.strip())

for key in filelist:
	if key in candidate.keys():
		text += '\n' + candidate[key]

print(text)

n = int(len(text)/900)
'''
# obtain the audio
for i in range(n):
	get_audio_command(text[900*i: 900*(i+1)], path, i)

get_audio_command(text[900*n:], path, n)

'''

# combine the audios

for i in range(n+1):
	filename = "speech" + str(i) + '.mp3'
	if i == 0:
		combine = AudioSegment.from_mp3(os.path.join(path, filename))
	else:
		combine = combine + AudioSegment.from_mp3(os.path.join(path, filename))

combine.export(os.path.join(path, "speech.wav"), format = "wav")
print("item done")





'''

#obtain the  traslator
translator = translate()
with open(os.path.join(path, trans_export), 'w') as f:
	for key in filelist:
		if key in candidate.keys():
			string_chinese = translator.translate_to_chinese(candidate[key])
			for subkey in string_chinese.keys():
				f.write(subkey+':')
				for subitem in string_chinese[subkey]:
					f.write(subitem+' ')
				f.write('\n')
			f.write('\n')
			f.write('\n')
'''		