astr = 'Hello'

try: 
    istr = int(astr)
except:
    istr = str('Can\'t convert to integer')

print('First:', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = str('Can\'t convert to integer')

print('Second:', istr)