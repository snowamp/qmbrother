#reduce space and sentence separation
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from replacers import RegexpReplacer


class cleaner(object):
	def __init__(self):
		self.cleantext = ''

	def clean(self, text):
		result = []
		replacer = RegexpReplacer()
		text1 = replacer.replace_simple(text)
		text2 = replacer.replace(text1)
		sent_text = sent_tokenize(text2)
		for item in sent_text:
			if len(item) > 0:
				result.append(item)
		return(result)