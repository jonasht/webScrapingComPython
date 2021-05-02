from urllib.request import urlopen
from bs4 import BeautifulSoup
print()

try:
    
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e) 
except URLError as e:
    print(e)
    print('the server could not be found')
    print('o servidor não poode ser encontrado')

else:
    print('it worked')
    print('funcionou')


    
    
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.title)
print(bs.h1)

print('div : ')
print(bs.div)
