from urllib.request import urlopen
from bs4 import BeautifulSoup
print()
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
# nameList = bs.findAll('span', {'class': 'green'})
nameList = bs.findAll('', {'class': 'green'})


for name in nameList:
    print(name.get_title())