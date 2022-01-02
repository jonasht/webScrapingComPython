from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img',
                    {'src': re.compile('\.\.\/img\/gifts/img.*.jpg')})
print(images)
print('='*60)
for image in images:
    print(image['src'])
