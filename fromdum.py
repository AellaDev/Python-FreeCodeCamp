userAges = [21, 22, 23, 24, 25]

print(userAges[0] + userAges[-2])

userAges2 = userAges[2:4] 
'''
This shi is apparently called a 'slice'
the reason why [2:4] is only calling 23, 24
is because the item at the end is always excluded
so basically, index 2 which is 23
and then index 4-1 which is 24 
'''
print(userAges2)

userAges3 = userAges[0:5:2]
'''
Now the 3rd number is what you call a 'stepper'
pretty self explanatory, it means the number of steps to take
And as you can notice it takes the 2 steps
and show the number on the second step
but as before, it will display the first index first which is 21
then took 2 steps from 21 which is 23
then took another 2 steps which is 25
25 is included because index 5-1 is index 4
'''
print(userAges3)

userAges4 = userAges[0: ]
'''
DEFAULTS! Slice Notation have useful defaults
one of them is this!
[0: ] results to the whole list up to last item
similarly [ :5] results to the whole list from the index0
'''
print(userAges4)

userAges[0] = 5
'''
This changes the index[0] to 5
you can change any index
nameofList[index] = number to replace
'''
print(userAges)

userAges.append(99)
'''
By the name itself, append
It add items to to the last item
so now it is:
[5, 22, 23, 24, 25, 99]
The reason it's 5 not 21 is because we changes index[0] earlier
'''
print(userAges)

del userAges[2]
'''
If there is such thing as 'adding items'
then there is 'removing items'
this is 'del'
unlike append it is not a fx
(If it is a fx you are gonna need parenthesis reagrdless if it's empty or not)
for this you on't need parentheses
just type 'del' then the listname and then index
'''
print(userAges)

########
myList = [1, 2, 3, 4, 5, 'Hello']
'''
Yes, lists can have different types of items
'''
print(myList)
'''
If you noticed,
even tho 'Hello' is a string
the '' marks are included in print
that is because you are printing the LIST
not the INDEX
'''
print(myList[5])
'''
This one results to Hello with no marks
because You are printing the item not the lists
'''
print(myList[-1])
'''
remember -1 means last on the list
'''
print(myList[1:5])
'''
This one means from index 1 to index5-1
'''

myList[1] = 20
'''
This is modification
'''
print(myList)

myList.append('How are you')
'''
ADD! append means add item
'''
print(myList)

del myList[6]
'''
del means delete or remove
noticed we removed what we added?
'''
print(myList)