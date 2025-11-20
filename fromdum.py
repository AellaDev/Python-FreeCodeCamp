## Conditional Statements (if)

number = input('Enter 1 or 2: ')
number = int(number)

if number == 1:
    print('Hello User 1')

elif number == 2:
    print('Hello User 2. You have limited access')

else:
    print('Please enter 1 or 2 only')