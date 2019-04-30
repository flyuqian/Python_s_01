# encoding=UTF-8

class ShortInputException(Exception):
    ''' 一个用户自定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast



while True:
    try:
        text = input('Enter something ->')
        if text == 'quit' or text == 'exit':
            break
        if len(text) < 3:
            raise ShortInputException(len(text), 3)
    except EOFError:
        print('Why did you do on EOF on me')
    except ShortInputException as ex:
        print(('ShortInputException: The input was' + \
            '{0} long, expected at least at lcat {1}')
            .format(ex.length, ex.atleast))
    else:
        print('NO exception was raised')
