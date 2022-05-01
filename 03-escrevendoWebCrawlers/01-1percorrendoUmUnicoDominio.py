from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
html = urlopen('https://en.wikipedia.org/wiki/Brazil')
bs = BeautifulSoup(html, 'html.parser')


for link in bs.find_all('a'):
    # print(link)
    if 'href' in link.attrs:
        print(link.attrs['href'])

print('=='*30)

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs1 = BeautifulSoup(html, 'html.parser')

for link in bs1.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])