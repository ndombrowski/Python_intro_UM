import urllib.request, urllib.parse, urllib.error
import json
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#get data
url='http://py4e-data.dr-chuck.net/comments_1701462.json'
input = urllib.request.urlopen(url, context=ctx)
data = input.read()

#convert
info = json.loads(data)

#extract counts
num_list = list()

for item in info['comments']:
    num = int(item['count'])
    num_list.append(num)

print('Sum:', sum(num_list))