def say_hello():
    print('hello world')
# say_hello()
# say_hello()

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# print_max(10, 20)

x = 50
def func(x):
    print('x is', x)
    x = 2
    print('change local x to', x)

# func(x)
# print('x is still', x)


y = 50
def func2():
    global y 
    print('y is', y)
    y = 2
    print('Value of y is', y)

# func2()
# print('value of y is', y)

# 默认参数
def say(message, times=1):
    print(message * times)
# say('hello')
# say('world', 5)

def log_abc(a = 1, b = 3, c = 9):
    print('a is', a, 'b is', b, 'c is', c)
# log_abc(2, 6)
# log_abc(2, c=6)

def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

# print(total(10, 1, 2, 3, jack=1122, John=2331, Inge=1550))


def get_max(x, y):
    if x > y:
        return x
    elif x == y:
        return 'THe numbers are equal'
    else:
        return y

# print(get_max(2, 3))

def print_max2(x, y):
    '''打印这两个数值中的最大值.
    
    这两个数都应该是整数'''

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is max')
    else:
        print(y, 'is max')


print_max2(3, 5)
print(print_max2.__doc__)



