message1 = '{0} is easier than {1}'.format('Python', 'Java')
message2 = '{1} is easier than {0}'.format('Python', 'Java')
message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)

name = 'Arabella'
age = 22
techAge = 22.916666666

message5 = 'I am %s and I am %d years old. Technically %0.2f years old'%(name, age, techAge)

print(message1)

print(message2)

print(message3)

print(message4)

print(message5)