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
#Build the vocabulary
vocab = {}
count = 0
for doc in processed_docs:
    for word in doc.split():
        if word not in vocab:
            count = count +1
            vocab[word] = count
print(vocab)
#Get one hot representation for any string based on this vocabulary. 
#If the word exists in the vocabulary, its representation is returned. 
#If not, a list of zeroes is returned for that word. 
def get_onehot_vector(somestring):
    onehot_encoded = []
    for word in somestring.split():
        temp = [0]*len(vocab)
        if word in vocab:
            temp[vocab[word]-1] = 1 # -1 is to take care of the fact indexing in array starts from 0 and not 1
        onehot_encoded.append(temp)
    return onehot_encoded

print(processed_docs[0])
print(get_onehot_vector(processed_docs[0]))
print(processed_docs[1])
print(get_onehot_vector(processed_docs[1])) #one hot representation for a text from our corpus.
