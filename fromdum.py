## For Loop

'''
for a in iterable:
    print(a)
'''

# example with list

pets = ['cats', 'dogs', 'rabbits', 'hamsters']
'''
If you want to show the index
you can just add enumerate on the pets
but it will show the () and the  comma
(0, 'cats')
but if there is an index then the index will show as 
0 cats
'''
for index, myPets in enumerate(pets):
    print(index, myPets)

# loop with string
message = 'Hello World'
'''
Yes you can loop within a string too
'''
for b in message:
    print(b)

# loop with sequence of numbers

for c in range(0, 100, 4):
    print(c)

for i in range(1, 21):
    print('I have repeated', i, 'time/s')