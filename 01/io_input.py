def revers(text):
    return text[::-1]
def is_palindrome(text):
    return text == revers(text)

while 1:
    something = input("Enter text:")
    if something == 'quit' or something == 'exit':
        break
    else:
        if is_palindrome(something):
            print('Yes, it is a palindrome')
        else:
            print('No, it is not a palindrome')



