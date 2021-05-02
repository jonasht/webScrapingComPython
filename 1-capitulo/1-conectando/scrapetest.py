from urllib.request import urlopen
from bs4 import BeautifulSoup
print()
# no site a um texto em latim, trarah um texto para imprimir
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)