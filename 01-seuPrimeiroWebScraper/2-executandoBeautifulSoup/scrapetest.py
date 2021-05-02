from urllib.request import urlopen
from bs4 import BeautifulSoup
print()
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.title)
# print o titulo da pagina "h1"
print(bs.h1)

print('div : ')
print(bs.div)

""" 
    qualquer uma das funcoes produziriam o mesmo resultado:
    bs.html.body.h1
    bs.body.h1
    bs.html.h1
"""

