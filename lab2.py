from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
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
final_list = []
word_tokens = nltk.word_tokenize(str(text_r))
for w in word_tokens:
    if w not in list_stop_words:
        final_list.append(w)
final_text = ' '.join(map(str, final_list))
# spell checker
spell = SpellChecker()
misspelled = spell.unknown(final_text)
# for word in misspelled:
#     print(word)
# detection language
b = TextBlob(final_text)
# print(b.detect_language())
# tokenize
# print(nltk.word_tokenize(final_text))
# count the number of occurrences of a word
str(final_text).count("python")
len(final_text)
# write file
# f = open('mytext.txt', "w")
# f.write(final_text)
# f.close()
# lemmatizer and stemmer
wordnet_lemmatizer = WordNetLemmatizer()
stemer = PorterStemmer()
sentence_words = nltk.word_tokenize(final_text)
print("{0:20}{1:20}{2:20}".format("original", "lemmatize", "stememer"))
for word in sentence_words:
    print("{0:20}{1:20}{2:20}".format(word, wordnet_lemmatizer.lemmatize(word, pos="v"),
    stemer.stem(word)))
