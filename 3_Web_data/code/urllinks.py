import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()

#beautify the html object
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
#this code below returns a list
tags = soup('a')

#extract the href key or nothing
for tag in tags:
    print(tag.get('href', None))

#print('')