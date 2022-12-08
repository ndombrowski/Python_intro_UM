fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0

for line in fhand:
    count = count + 1

print('There are', count, 'subject lines in', fname)