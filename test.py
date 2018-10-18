import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

# url = "http://www.gutenberg.org/files/2554/2554-0.txt"
# response = request.urlopen(url)
# raw = response.read().decode('utf8')

# url = open("sample.json")
# raw = url.read()

# print(len(raw))

# tokens = word_tokenize(raw)
# text = nltk.Text(tokens)
# print(text[:60])
# print(text.collocations())


# start = raw.find("PART I")
# end = raw.rfind("End of Project Gutenberg's Crime")
# print(end)
# newRaw = raw[start:-end]
# print(newRaw)

import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
text = llog['feed']['title']
print(llog.entries[2].title)
print(text)

# print(text.concordance())
