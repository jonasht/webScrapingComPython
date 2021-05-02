from urllib.request import urlopen

print()
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())