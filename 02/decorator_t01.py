# def a_new_decorator(a_func):
    
#     def wrapTheFunction():
#         print('在函数执行前的一些操作')
#         a_func()
#         print('在函数调用后的一些操作')
#     return wrapTheFunction

# def a_function_requiring_decorator():
#     print('I am the funciton which needs some decration to remove my foul smell')

# a_function_requiring_decorator()

# a_function_requiring_decorator = a_new_decorator(a_function_requiring_decorator)
# a_function_requiring_decorator()


# @a_new_decorator
# def a_function_requiring_decorator():
#     print('被装饰的函数')

# a_function_requiring_decorator()
# print(a_function_requiring_decorator.__name__)

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('执行 a_func 前')
        a_func()
        print('执行 a_func 后')
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decorator():
    print('需要 装饰的 函数的 执行')

a_function_requiring_decorator()
print(a_function_requiring_decorator.__name__)



def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + 'was called')
        return func(*args, **kwargs)
    return with_logging

@logit
def addtion_func(x):
    return x + x

result = addtion_func(4)
print(result)

# def logit2(logfile = 'out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + 'was called'
#             print(log_string)
