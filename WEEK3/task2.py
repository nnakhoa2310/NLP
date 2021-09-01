from bs4 import BeautifulSoup
from urllib import request
import re
url="https://baodanang.vn/ytesuckhoe/202108/phai-xac-dinh-chinh-xac-cac-vung-do-de-co-bien-phap-xet-nghiem-giam-sat-phu-hop-3888676/"

html= request.urlopen(url).read().decode("utf8")
raw = BeautifulSoup(html,'html.parser').getText()
data=str(html)
deta = str(raw)

link = re.findall('https?://[^\s"]+',data)
print(link)
cau=re.findall('.*',deta)
print(cau)
try:
 f = open("Noidung2.txt",encoding = 'utf-8',mode='w')
 f.write("link\n")
 f.write("\n".join(link))
 f.write("cau\n")
 f.write("\n".join(cau))
finally:
 f.close()