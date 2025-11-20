## INPUT

fir = input('Enter first number: ')
sec = input('Enter Second number: ')

print('First Number: {0:s} + Second Number: {1:s}'.format(fir, sec))
'''
input() will always store your input as STRING
so if you want it to be math based
then you have to type cast
'''

fir = int(fir)
sec = int(sec)

print(fir + sec)