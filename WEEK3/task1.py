from bs4 import BeautifulSoup
from urllib import request
import re
url="http://elearning.vku.udn.vn/login/index.php"

html= request.urlopen(url).read().decode("utf8")
raw = BeautifulSoup(html,'html.parser').getText()
data=str(html)

""" Số điện thoại """
sdt= re.findall(r'\d{3,4}.\d{3,4}.\d{3,4}', data)
print(sdt)
""" Email """

email=re.findall('[^\s"]+@[^\s"]+',data)
print(email)
""" link """
link = re.findall('https?://[^\s"]+',data)

print(link)

with open("G:/HK 1 N 4/NLP/T3/text.txt", mode="w") as file:
    for content in sdt:
        file.write(f"{content.lower()}\n")
    for content in email:
        file.write(f"{content.lower()}\n")
    for content in link:
        file.write(f"{content.lower()}\n")
file.close()