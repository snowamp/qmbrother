#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import re


school = []
new = {}
content = ""
for line in sys.stdin:
	line = line.strip()
	if len(line) == 0:
		continue
	if u'Schoolname' in line:
		if new:
			new['Introduction'] = content
			school.append(new)
			new = {}
		content = ""
		new['Schoolname'] = line
	elif u'Address' in line:
		new['Address'] = line
	else:
		content += ' '+line
new['Introduction'] = content
school.append(new)

f = open("school.json", 'w+')

jsonStr = json.dumps(school,ensure_ascii=False)

f.write(jsonStr)

f.close()











'''

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)

print(json_str)
'''