fname = input('Enter the filename: ')

try:
    fh = open(fname)
except:
    print('This file does not exist: ', fname)
    quit()

count = 0
total = 0 

for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    #find our numbers
    spos = line.find(':')
    num_s = line[spos + 1 :].strip()
    num = float(num_s)
    # get the sum
    total = total + num
    #get the count
    count = count + 1
    
print('Average spam confidence:', total/count)
