from urllib.request import urlopen

print()
# no site a um texto em latim, trarah um texto para imprimir
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
