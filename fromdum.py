## Escape Characters
# \character

'''
\t = tab
\\ = \
\n = new line
\" = double quote
\' = single quote

If you are trying to print \character as is
you need to use raw input which is r'stringexample'
'''
print('Hello\tWorld')
print('Hello\\World')
print('Hello\nWorld')
print('Hello\"World')
print('Hello\'World')
print(r'Hello\tWorld')