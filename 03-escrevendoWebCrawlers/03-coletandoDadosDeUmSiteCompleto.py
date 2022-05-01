from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# para daixar a pagina mais elegante 
def l():
    print('=-'*30+'=')

pages = set()
print('tipo pages:', type(pages))

def get_links(page_url):
    global pages
    
    html = urlopen('https://en.wikipedia.org{}'.format(page_url))
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p'[0]))
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except:
        print('esta pagina está faltando algo, continuando...')
        print('this page is missing sth, continueing...')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                
                l()
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links('')

