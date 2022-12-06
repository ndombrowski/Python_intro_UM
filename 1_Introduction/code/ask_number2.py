largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num_int = int(num)
        if largest is None or num_int > largest:
            largest = num_int
        if smallest is None or num_int < smallest:
            smallest = num_int
    except:
        print('Invalid input. \nEnter either a number or done')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)