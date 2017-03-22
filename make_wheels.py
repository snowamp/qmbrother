import sys

vow={'ee':'i:', 'aw':'aw', 'er':'er', 'ay':'ei', 'ur':'ur', 'al':'o:', 'ea':'i:', 'ir':'ur', 'ear':'eer', 
'ow':'oh', 'ai':'ei', 'ou':'ou','ar':'ahr', 'or':'aw'}

pics = {'ee':'eevee', 'aw':'pawniard', 'er':'servine', 'ay':'inkay', 'ur':'lanturn', 'al':'baltoy', 'ea':'horsea', 'ir':'swirlix',
'ou':'bellsprout', 'ear':'pansear', 'ow':'taillow', 'ai':'raichu', 'ar':'larvitar', 'or':'torchic'}

pic_vowel = {'ee':'EE-vee', 'aw':'PAWN-yard', 'er':'SUR-vine', 'ay':'in-KAY', 'ur':'LAN-turn', 'al':'BAL-toy', 'ea':'HOR-sea', 'ir':'SWUR-licks',
'ou':'BELL-sprout', 'ear':'PAN-seer', 'ow':'TAY-low', 'ai':'RYE-choo', 'ar':'LAR-vuh-tar', 'or':'TOR-chick'}

words = {}
words_ch = {}
compound = ['ee', 'aw','ay', 'ur', 'al','ea', 'ou','ai', 'ar','or', 'er', 'ow']
compound_1 = ['er', 'ow']

colorstring = ['red!10', 'green!10', 'blue!10', 'yellow!10']

colorpointer = 0

filename = '/Users/yanchunyang/Documents/latex/wheel.txt'
path = '/Users/lxb/Documents/yyc/pokemonpics/vowel/'

for item in compound:
	words[item] = []
	words_ch[item] = []

with open('vowelwords_1.txt', 'r') as f:
	for line in f.readlines():
		splits = line.strip().split('\t')
		if splits[0] in compound:
			words[splits[0]].append(splits[2])
			words_ch[splits[0]].append(splits[3])

g = open(filename, 'w+')

for vowel in compound:
	currentpos = 0
	temp_store = []
	temp_store_ch = []
	pos1 = 2.5
	pos2 = 3
	pointer1 = 2.5
	pointer2 = 3
	for i in range(0, len(words[vowel])):
		s = words[vowel][i]
		s_cn= words_ch[vowel][i]
		if vowel not in ['er', 'ow']:
			pos1 = 2.5
			pos2 = 3
			pointer1 = 2.5
			pointer2 = 3
		else:
			pos1 = 3
			pos2 = 3.5
			pointer1 = 3
			pointer2 = 3.5

		index = s.find(vowel)
		print(s)
		print(index)
		if vowel not in ['er', 'ow']:
			if len(s[:index]) > 3 or len(s[index+2:])>3:
				continue
		else:
			if len(s[:index]) > 4 or len(s[index+2:])>3:
				continue
		for k in range(index-1, -1, -1):
			if s == 'see':
				print('I am here')
			temp_store.append(s[k]+'/'+str(pointer1-0.5)+'/'+str(currentpos))
			pointer1 -=0.5
		for k in range(index+2, len(s)):
			temp_store.append(s[k]+'/'+str(pointer2+0.5)+'/'+str(currentpos))
			pointer2 +=0.5
		temp_store_ch.append(s_cn[0]+'/'+str(5.3)+'/'+str(currentpos))
		if len(s_cn)>1:
			temp_store_ch.append(s_cn[1]+'/'+str(6)+'/'+str(currentpos))
		currentpos += 60
		#print(temp_store)
		if currentpos >= 360:
			g.write('\\null\\newpage'+'\n')
			g.write('\def\colorstring{' + colorstring[colorpointer] + '}'+'\n')
			colorpointer += 1
			if colorpointer > 3:
				colorpointer = 0
			g.write('\\textblockorigin{0cm}{0cm}'+'\n')
			g.write('\\begin{textblock*}{6cm}(1cm,2cm)'+'\n')
			g.write('\loopy{\colorstring} {{')
			for sub in temp_store:
				g.write(sub+',')

			for sub in temp_store_ch[0:len(temp_store_ch)-1]:
				g.write(sub+',')
			g.write(temp_store_ch[-1] + '}}')
			g.write('\n'+'\end{textblock*}'+'\n')
			g.write('\\textblockorigin{12cm}{18cm}'+'\n')
			g.write('\def\picstring{'+path+pics[vowel]+'.png}'+'\n')
			g.write('\\begin{textblock*}{6cm}(1cm,1cm)'+'\n')
			if vowel not in ['er', 'ow']:
				g.write('\inner {{'+vowel[0]+'/2.5,'+vowel[1]+'/3}}{'+vowel+'}{'+pic_vowel[vowel]+'}{\picstring}{\colorstring}{'+pics[vowel]+'}'+'\n')
			else:
				g.write('\innerfar {{'+vowel[0]+'/3,'+vowel[1]+'/3.5}}{'+vowel+'}{'+pic_vowel[vowel]+'}{\picstring}{\colorstring}{'+pics[vowel]+'}'+'\n')
			g.write('\end{textblock*}'+'\n')
			currentpos = 0
			temp_store = []
			temp_store_ch = []

	if len(temp_store)> 0:
		g.write('\\null\\newpage'+'\n')
		g.write('\def\colorstring{' + colorstring[colorpointer] + '}'+'\n')
		colorpointer += 1
		if colorpointer > 3:
			colorpointer = 0
		g.write('\\textblockorigin{0cm}{0cm}'+'\n')
		g.write('\\begin{textblock*}{6cm}(1cm,2cm)'+'\n')
		g.write('\loopy{\colorstring} {{')
		for sub in temp_store:
			g.write(sub+',')
		for sub in temp_store_ch[0:len(temp_store_ch)-1]:
			g.write(sub+',')
		g.write(temp_store_ch[-1] + '}}')
		g.write('\n'+'\end{textblock*}'+'\n')
		g.write('\\textblockorigin{12cm}{18cm}'+'\n')
		g.write('\def\picstring{'+path+pics[vowel]+'.png}'+'\n')
		g.write('\\begin{textblock*}{6cm}(1cm,1cm)'+'\n')
		if vowel not in ['er', 'ow']:
			g.write('\inner {{'+vowel[0]+'/2.5,'+vowel[1]+'/3}}{'+vowel+'}{'+pic_vowel[vowel]+'}{\picstring}{\colorstring}{'+pics[vowel]+'}'+'\n')
		else:
			g.write('\innerfar {{'+vowel[0]+'/3,'+vowel[1]+'/3.5}}{'+vowel+'}{'+pic_vowel[vowel]+'}{\picstring}{\colorstring}{'+pics[vowel]+'}'+'\n')
		g.write('\end{textblock*}'+'\n')

	

g.close()







	
		
		


