from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

        # html = urlopen('http://pythonscraping.com/pages/page1.html')
def getTitle():
    
    print()

    try:
        html = urlopen(url)

    except HTTPError as e:
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('title could not be found')
        print('titulo não poode ser encontrado')
        
getTitle()