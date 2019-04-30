name = 'Swarrop'

if name.startswith('Swa'):
    print('Yes, the string start with "Swa"')

if 'a' in name:
    print('yes, it contains the string "a"')

if name.find('war') != -1:
    print('yes, it contains the string "war"')

delimiter = '_*_'
myList = ['Brazil', 'Russia', 'India', 'Chain']
print(delimiter.join(myList))
print(myList)
