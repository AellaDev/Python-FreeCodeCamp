#Dictionary
'''
Pretty sure you already held a dictionary before
Dictionary is like a list
But with a PAIR
'''

'''
There are 2 ways to declare a dict
'''

# dictname = {Items} ['key':data]
# emPloyees = {'Peter':38, 'Mitch':40, 'Law':20, 'Vince':'Not Available'}
'''
you can have different types of data in a dict
'''

# dictname = dict(items) [key = data]
emPloyees = dict(Peter = 38, Mitch = 40, Law = 20, Vince = 'Not Available')

print(emPloyees['Law'])
'''
In order to access an age which is a data
just like list you declare the position
but dict soesnt use index
it uses key:pair
which means you declare the key
'''

emPloyees['Law'] = 50
print(emPloyees)
'''
to MODIFY
just like lists
Law is now 50
'''

newDict = {}
'''
this is an empty dictionary
you can add items to this by doing below
'''
newDict['Ruru'] = 18
newDict['Wei'] = 20
print(newDict)

del newDict['Ruru']
'''
Just like lists this is how you delete
'''
print(newDict)