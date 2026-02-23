try:
    a = input('Enter the First Number: ')
    b = input('Enter the Second Number: ')
    
    a = int(a)
    b = int(b)

    print('Sum= ', a+b)

    if b == 0:
        print('Cannot divide by zero')
    else:
        print('Division= ', a/b)

except ValueError:
    print('Invalid input')