from urllib.request import urlopen
from bs4 import BeautifulSoup



html = urlopen('https://www.pythonscraping.com/pages/page3.html')
# html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
print('='*30)

for sibling in bs.find('table', {'id': 'giftList'}).tr:
    print(sibling)