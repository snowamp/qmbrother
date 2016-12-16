import re

replacement_patterns = [
  (r'won\'t', 'will not'),
  (r'can\'t', 'cannot'),
  (r'i\'m', 'i am'),
  (r'ain\'t', 'is not'),
  (r'(\w+)\'ll', '\g<1> will'),
  (r'(\w+)n\'t', '\g<1> not'),
  (r'(\w+)\'ve', '\g<1> have'),
  (r'(\w+)\'s', '\g<1> is'),
  (r'(\w+)\'re', '\g<1> are'),
  (r'(\w+)\'d', '\g<1> would'),
  (r'\s\s+', ' '),
  (r'^\s+', '')
]

class RegexpReplacer(object):
  def __init__(self, patterns=replacement_patterns):
    self.patterns = [(re.compile(regex), repl) for (regex, repl) in 
      patterns[0:10]]
    self.patterns_simple = [(re.compile(regex), repl) for (regex, repl) in patterns[-2:]]

  def replace(self, text):
    s = text
    for (pattern, repl) in self.patterns:
      s = re.sub(pattern, repl, s)
    return s

  def replace_simple(self, text):
    s = text
    for (pattern, repl) in self.patterns_simple:
      s = re.sub(pattern, repl, s)
    return s