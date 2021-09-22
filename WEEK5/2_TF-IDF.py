from bs4 import BeautifulSoup
from urllib import request
import re

url="https://baodanang.vn/ytesuckhoe/202108/phai-xac-dinh-chinh-xac-cac-vung-do-de-co-bien-phap-xet-nghiem-giam-sat-phu-hop-3888676/"
html= request.urlopen(url).read().decode("utf8")
raw = BeautifulSoup(html,'html.parser')

url1="https://baodanang.vn/ytesuckhoe/202109/ngay-13-9-da-nang-co-13-ca-mac-covid-19-0-ca-cong-dong-3889473/"
html1= request.urlopen(url1).read().decode("utf8")
raw1 = BeautifulSoup(html1,'html.parser')

data1 = raw.find("h1").getText()
data2= raw1.find("h1").getText()
S1=str(data1)
S2=str(data2) 
documents = [S1,S2]
processed_docs = [doc.lower().replace(".","") for doc in documents]
print(processed_docs)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform(processed_docs)

#IDF for all words in the vocabulary
print("IDF for all words in the vocabulary",tfidf.idf_)
print("-"*10)
#All words in the vocabulary.
print("All words in the vocabulary",tfidf.get_feature_names())
print("-"*10)

#TFIDF representation for all documents in our corpus 
print("TFIDF representation for all documents in our corpus\n",bow_rep_tfidf.toarray()) 
print("-"*10)

temp = tfidf.transform(["dog and man are friends"])
print("Tfidf representation for 'dog and man are friends':\n", temp.toarray())