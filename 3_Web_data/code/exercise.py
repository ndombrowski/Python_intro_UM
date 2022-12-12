import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

#url = 
url = 'http://py4e-data.dr-chuck.net/comments_1701459.html'
html = urllib.request.urlopen(url).read()

#beautify
soup = BeautifulSoup(html, 'html.parser')

#retrieve span tags
tags = soup('span')

#pull out nrs
numlist = list()

for tag in tags:
    tag_string = int(tag.contents[0])
    numlist.append(tag_string)

print('Count', len(numlist))
print('Sum', sum(numlist))
