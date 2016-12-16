#clean text and generate the nnp list for picture snatching
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from replacers import RegexpReplacer
from highfreq import commonwords
from collections import defaultdict


class obtain_nnp(object):

	def obtain(self, text):
		nnp_result = []
		result = defaultdict(int)
		replacer = RegexpReplacer()
		text1 = replacer.replace_simple(text)
		text = replacer.replace(text)
		sent = sent_tokenize(text)
		for sen in sent:
			words = word_tokenize(sen)
			pos_result = pos_tag(words)
			highfreq = commonwords().words()
			string = ""
			flag = -1
			for item in pos_result:
				if item[1] == 'NN':
					string += " " + item[0]
					if flag < 0:
						flag = 0
				elif item[1] == 'NNP':
					string += " " + item[0]
					flag = 1
				else:
					if len(string) > 0:
						if flag == 0:
							result[string] += 1
						else:
							if string not in nnp_result:
								nnp_result.append(string)
					string = ""
			if len(string) > 0:
				if flag == 0:
					result[string] += 1
				else:
					nnp_result.append(string)
			
		for item in sorted(result.items(),key = lambda x: x[1]):
			if item[0] not in highfreq:
				nnp_result.append(item[0])

		#nnp_set = set(nnp_result)

		return(nnp_result)


