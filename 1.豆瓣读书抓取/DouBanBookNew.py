import requests
from bs4 import BeautifulSoup

res = requests.get('https://book.douban.com/latest?icn=index-latestbook-all')
soup = BeautifulSoup(res.text,'html.parser')

for news in soup.select('.aside'):
	bookname = news.select('.detail-frame')
	#bookprice = 
	#introduce = 
	#comment = 
	print(bookname)

