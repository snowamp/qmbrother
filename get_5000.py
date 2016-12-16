import re



words = []

fn = open("../wheels/highfreq.rtf", 'r')

k = 0

for line in fn.readlines():
	k += 1
	if k<= 7:
		continue
	a = re.sub('\\\'a0', '', line.strip())
	b = a[3:len(a)-1]
	words.append(b)

fn.close()

f = open("../wheels/highfreq.txt", 'w+')

f.write('the'+'\t')

i = 1

for item in words:
	i += 1
	f.write(item+'\t')

f.close()

print(str(i))