#! coding = 'utf-8'
# 本脚本功能，为爬取 豆瓣读书 最受关注图书榜--非虚拟类前十书籍信息

import requests
import re
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from pandas import DataFrame

def getAttendtionBook(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'html.parser')
	AttendtionBook = []

	for book in soup.select('.media'):

		# 获取书籍html信息
		bookInfo = book.select('p')[0].text.split('/')
		bookName = book.select('a')[1].text

		# 部分书籍作者存在多个，数组长度不一致，对多用户数组，需特殊处理
		if len(bookInfo)>5:
			for bookAuthor in bookInfo[:-4]:
				bookAuthor += bookAuthor
		else:
			bookAuthor = bookInfo[:-4][0].strip()
		# 以上代码，均为判断

		bookDistributeTime = bookInfo[-4].strip()
		bookDistributor = bookInfo[-3].strip()
		bookPrice = bookInfo[-2].strip()
		bookURL = book.select('a')[1].get('href')

		#书籍评分，10.0问特殊分数，采用正则表达式来判断
		starRule = re.compile(r'[0-9].[0-9]|10.0')
		bookStar = starRule.match(book.select('p')[1].text.strip()).group()
		
		AttendtionBook.append((bookName, bookAuthor, bookDistributeTime, bookDistributor, bookPrice, bookStar, bookURL))
	return AttendtionBook

if __name__ == "__main__":
    url = 'https://book.douban.com/chart?subcat=I'
    
    # 通过padans的DataFrame函数，按照格式输出，并将信息保存至excel文件
    df = DataFrame(getAttendtionBook(url), columns=['bookName', 'bookAuthor', 'bookDistributeTime', 'bookDistributor', 'bookPrice', 'bookStar', 'bookURL'])
    df.to_excel('d:\\books.xlsx')
    print(df)
