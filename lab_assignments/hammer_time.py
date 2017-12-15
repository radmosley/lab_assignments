...
time = input('Enter time using 24hr format (example 0800): ')
num = time[0:2]

breakfast = 'It\'s breakfast time!'
lunch = 'It\'s lunch time!'
dinner = 'It\'s dinner time!'
hammer = 'Lets be real, it\'s always hammer time'
no_meal = 'No meal served at this time.'

if num == ('07'or'08'or'09'):
    print(breakfast)
elif num == ('12'or'13'or'14'):
    print(lunch)
elif num == ('19'or'20'or'21'):
        print(dinner)
elif num == ('22'or'23'or'24'or'01'or'02'or'03'or'04'):
    print(hammer)
else:
    print(no_meal)

time = input('What time is it?(HH:MM:am/pm)').lower()

hour, minute, merd = time.split(':')

if merd == 'am':
    #if hour == ()'07' or '08' or '09'):
    if hour == ['07', '08', '09']:
        print('Breakfast')
    elif hour in ['', '01', '02', '03', '04']:
        print('Hammer Time')
    else:
        print('Go to sleep')
    else:
        if hour in  ['12', '01', '02',]:
            print('Lunch Time')
        elif hour in ['07', '08', '09']:
