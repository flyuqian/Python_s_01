poem = '''\
Programming is fun
When the work is done
if you wanna make your work alse fun:
use Python!
'''

f = open('foo.txt', 'r+')
f.write(poem)
f.close

print('write done')

f = open('foo.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end = '')
f.close()

print('read done')