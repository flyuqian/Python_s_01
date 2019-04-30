number = 23
running = True

while running:
    guess = int(input('Enter on integer:'))
    if guess == number:
        print('Congraulations, you guessed it')
        print('(but you do not win any prizes!)')
        running = False
    elif guess < number:
        print('No, it is a litter higher than that')
    else:
        print('No, it is a little lower than that')
else:
    print('the while loop is over.')

print('Done')