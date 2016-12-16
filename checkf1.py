import sys

compare = []
f = open("certified.txt", 'r')

for line in f.readlines():
	if len(line)> 2 and line.strip() not in compare:
		compare.append(line.strip())

f.close()




f = open("goodlink.txt", 'r')

for line in f.readlines():
	line1 = line.strip().split('\t')[0].lower()

	for i in range(0, len(compare)):
		if line1 in compare[i].lower():
			sys.stdout.write(line)


f.close()