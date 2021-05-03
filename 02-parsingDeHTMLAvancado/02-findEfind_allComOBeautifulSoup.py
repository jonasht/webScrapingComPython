from urllib.request import urlopen
from bs4 import BeautifulSoup
print()
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
# nameList = bs.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# nameList = bs.findAll('span', {'class': {'green', 'red'}})
# nameList = bs.findAll(text='the prince')
# print(len(nameList))
title = bs.findAll(id='title', class_='text')
print(len(title))


# for name in nameList:
#     print(name.get_title())