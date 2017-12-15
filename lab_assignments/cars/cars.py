class Car:
    def __init__(self, color, doors, wheels=4, ):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.honk = 'honk'

blue_car = Car('Blue', '4')
green_car = Car('Green', '8')
red_car = Car('Red', '2')

# print('Your car is ' + red_car.color + ' with ' + red_car.doors + ' doors.')
# print(red_car.honk, red_car.honk)