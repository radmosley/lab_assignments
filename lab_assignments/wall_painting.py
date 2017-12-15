#Wall Painting
import math

width = input('How tall is the wall you\'re paiting?: ')
height = input('How wide is the wall you\'re painting?: ')
cost = input('How much does paint cost at your local store per gallon?: ')
calc_area = int(width) * int(height)
calc_gal = calc_area / 400
calc_gal_2 = math.ceil(calc_gal)
calc_cost = calc_gal_2 * float(cost)


print(calc_cost)
