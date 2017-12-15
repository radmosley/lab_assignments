#ROT13 Cipher
max_difficulty = 10

def get_mode():
    while True:
        print('Do you wish encrypt or decrypt a message?: ')
        mode = input().lower()
        if mode[0] == 'e':
            return mode
        elif mode[0] == 'd':
            return mode
    else:
        print('That is an invalid input.')

def get_message():
    print('Enter your message')
    return input()

def get_difficulty():
    difficulty = 0
    while True:
        print('Enter a number to rotate your encryption difficulty (1-%s)' % (max_difficulty))
        difficulty = int(input())
        if (difficulty >= 1 and difficulty <= max_difficulty):
            return difficulty

def translated_message(mode, difficulty, message,):
    if mode[0] == 'd':
        difficulty = -difficulty
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += difficulty
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                translated += chr(num)
        else:
            translated += symbol
    return translated        

mode = get_mode()
message = get_message()
difficulty = get_difficulty()

print('your translated message is: ')
print(translated_message(mode, difficulty, message))
    
