import random
import time

c_number = random.randint(1, 10)
guess_int = 0
def guess():
    entry = input('what number am I thinking?')
    guess_int = int(entry)

while (guess_int != c_number):
    guess()
    if guess_int > c_number:
        print('You\'re too high.')

    if guess_int < c_number:
        print('You\'re too low.')
if guess_int == c_number:
    print('Congradulations, you\'re prize is self reflection on the time you\'ve wasted!')
    replay = input('would you like to play again?: ').lower()
    if replay == 'y':
            print(entry)
