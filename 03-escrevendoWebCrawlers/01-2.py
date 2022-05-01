from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re



random.seed(datetime.datetime.now())

def get_links(articleUrl):
    html = urlopen(f'https://en.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

    

links = get_links('/wiki/Brazil')


while len(links)> 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
