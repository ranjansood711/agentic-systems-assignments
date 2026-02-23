try:
    name = input('Enter your name: ')
    age = input('Enter your age: ')

    age = int(age)

    if age < 0:
        print('Age cannot be negative')
    else:
        print('Hello ', name)
        if age < 13:
            print ('You are a Child')
        elif age < 18:
            print('You are a Teenager')
        elif age < 60:
            print('You are an Adult')
        else:
            print('You are a Senior Citizen')

except ValueError:
    print('Invalid age input')