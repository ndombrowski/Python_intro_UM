fname = input('Enter the filename: ')

try:
    fname = open(fname)
except:
    print('This file does not exist: ', fname)
    quit()

for line in fname:
    line = line.rstrip().upper()
    print(line)

