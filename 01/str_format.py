age = 20
name = 'Swaroop'
print('{0} was {1} years old whhen he wrote this book'.format(name, age))
print("why is {0} playing with python?".format(name))
print(name + ' is ' + str(age) + ' years old ')
print('{} was {} years old whhen he wrote this book'.format(name, age))
# 输出小数点后3位
print('{0:.3f}'.format(1.0/3))
# 使用_填充
print('{0:_^11}'.format('hello'))
# 基于关键词输出
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('a', end='')
print('b', end='\n')

print('This is the first line\nThis is the second line')
print('This is the first line \
    This is the second line')

r"NewLines are indicated by \n"
    