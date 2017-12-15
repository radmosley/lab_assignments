import random

low = 0
high = 10
response = ''
c_guess = random.randint(low,high)
s_number = input('what is your number?' )

while response != 'yes':
    print('is it', c_guess,'?' )
    response = input()
    if response == 'higher':
        low = c_guess + 1
        c_guess = random.randint(low,high)
    elif response == 'lower':
        high = c_guess - 1
        c_guess = random.randint(low, high)
        pass
    elif response == 'yes':
        print('whoo hoo!')
        break
    else:
        print('only higher lower or yes are valid responses.')