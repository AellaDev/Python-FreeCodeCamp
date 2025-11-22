j = 0
while j < 5:
    print('j = ', j)
    if j == 3:
        j += 1
        continue
    print('I will skip over 3')
    j += 1


    '''
    This one is a bit hard to understand since the book I was reading is older python 3
    so now the continue is way more harder to understand to me
    but basically
    when the computer reads the word 'continue'
    it ends the iteration not the loop
    so it will just skip the iteration nd 'continue'
    is the last thing it will read before repeating

    the reason why ther is a j+=1 inside the if is because 
    once the code reaches the if
    and j == 3 is indeed true
    then it will read the if code block
    nd since it has 'continue'
    it will skip the bottom code which holds the increment

    so qhat will happen is that it will add 1 to the j which is now 3
    then end iteration
    then loop again 
    
    this one is a bit hard to understand my head is bursting
    but why does the if statement knows its a 3
    well here it is
    when you are starting the loop it starts at 0
    0 not 3 skip if then + 1
    1 not 3 skip if then + 1
    2 not 3 skip if then + 1
    3 is 3 enter if then + 1
    etc

    my brain hurts
    '''