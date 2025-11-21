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
if choiceofMethod not in ['1', '2', '3', '4']:
    print('Please choose from the menu. Number only.')
    exit()
else:
    x = input('Enter X: ')
    y = input('Enter Y: ')

x = int(x)
y = int(y)

ansSum = x + y
ansDif = x - y
ansQuo = x / y
ansPro = x * y

if choiceofMethod == '1':
    print('The {0:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansSum)
elif choiceofMethod == '2':
    print('The {1:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansDif)
elif choiceofMethod == '3':
    print('The {2:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansQuo)
elif choiceofMethod == '4':
    print('The {3:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansPro)