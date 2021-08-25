from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import re
# Thu thập nội dung của bài viết
URL = "https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html"
getHTML = BeautifulSoup(urlopen(URL), 'html.parser')
getdiv = getHTML.find_all('p', {'class':'Normal'})
# Xóa bỏ các Tag HTML
text = ''
for sense in getdiv:
    text += sense.text
# lowercasting and remove punctuation
text_r = re.sub(r'[^\w\s]','',text).lower()
# remove stop words
list_stop_words = stopwords.words('english')
final_text = {text_r.replace(stop_word, '') for stop_word in list_stop_words}
# spell checker
spell = SpellChecker()
misspelled = spell.unknown(str(final_text))
# for word in misspelled:
#     print(word)
# detection language
b = TextBlob(str(final_text))
# print(b.detect_language())
# tokenize
# print(nltk.word_tokenize(str(final_text)))
# count the number of occurrences of a word
str(final_text).count("python")
len(final_text)
# write file
f = open('mytext.txt', "w")
f.write(str(final_text))
f.close()