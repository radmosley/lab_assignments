import sys
import random

print('Ask the the Eight Ball whatever you desire: ')
question = input()
answer = random.randint(1, 3)

def ans(rand):
    if rand is 1:
        return 'You probably shouldn\'t ask a stranger this'
    elif rand is 2:
        return 'you are thinking about this way to much...'
    elif rand is 3:
        return '...like a weird amount'
    
    

print(ans(answer))