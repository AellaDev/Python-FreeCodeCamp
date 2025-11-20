## Calculator

print('''
Welcome to AellaDev's Calculator!
            Menu
1. Addition
2. Subtraction
3. Division
4. Multiplication
''')

choiceofMethod = input('Choose a number from the menu: ')

x = input('Enter X: ')
y = input('Enter Y: ')

x = int(x)
y = int(y)

if choiceofMethod == '1':
    ans = x + y
    print('The {0:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ans)
elif choiceofMethod == '2':
    ans = x - y
    print('The {1:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ans)
elif choiceofMethod == '3':
    ans = x/y
    print('The {2:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ans)
elif choiceofMethod == '4':
    ans = x*y
    print('The {3:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ans)
else:
    print('Please choose from the menu. Number only.')