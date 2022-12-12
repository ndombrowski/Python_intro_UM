import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#read in data
url = 'http://py4e-data.dr-chuck.net/comments_1701461.xml'
input = urllib.request.urlopen(url, context=ctx)
data = input.read()

stuff = ET.fromstring(data)

#find comments
lst = stuff.findall('comments/comment')
#print('Comment count:', len(lst))

#extract numbers:
num_list = list()

for item in lst:
    num = int(item.find('count').text)
    num_list.append(num)

print('Sum:', sum(num_list))