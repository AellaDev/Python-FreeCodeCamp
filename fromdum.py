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

def operations(x, y):
    x = int(x)
    y = int(y)

    if choiceofMethod == '1':
        ans = x + y
    elif choiceofMethod == '2':
        ans = x - y
    elif choiceofMethod == '3':
        ans = x / y
    elif choiceofMethod == '4':
        ans = x * y

    return ans

if choiceofMethod == '1':
    ansSum = operations(x, y)
    print('The {0:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansSum)
elif choiceofMethod == '2':
    ansDif = operations(x, y)
    print('The {1:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansDif)
elif choiceofMethod == '3':
    ansQuo = operations(x, y)
    print('The {2:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansQuo)
elif choiceofMethod == '4':
    ansPro = operations(x, y)
    print('The {3:s} is: '.format('SUM', 'DIFFERENCE', 'QUOTIENT', 'PRODUCT'), ansPro)