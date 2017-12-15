#Greetings

name = input('What is your name?: ')
age = input('How old are you?: ')
bday = int(age) +1
message = 'Hello {n}, you will be {b} next year!'.format(n=name, b=bday)

print(message)
