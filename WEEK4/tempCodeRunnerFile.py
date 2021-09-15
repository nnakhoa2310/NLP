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