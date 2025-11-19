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