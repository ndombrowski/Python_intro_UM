numlist = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    
    #convert our input to a float
    try:
        value = float(inp)
    except: 
        print('Please, enter a number or done')
        continue
    
    #add the value to our list
    numlist.append(value)
    
#do math
average = sum(numlist) / len(numlist)
print('Average:', average)
