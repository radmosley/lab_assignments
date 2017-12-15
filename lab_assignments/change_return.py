# Some supermarkets have automatic change dispensers.
# Ask for the amount of change to dispense in cents.
# Assume that the amount input will be less than 100 cents.
# Calculate the number of quarters necessary first.
# Then calculate the number of dimes, nickels, and pennies.
# If you do it in that order, you will minimize the number of coins.
# This is easiest done by updating a running total of number of cents left to be put into coins.
# Also remember that the // operator divides and removes any remainder.

#if the number is less than 100 contiune to the next step
#divide the change by 25 
#the modulus of the number divided by 25 should be divided by 10
#the modulus of that number will be divided until the number is zero

#Message
welcome = print('Without the decimal enter your amount of change: ')
purchase = int(input())
round_1 = int()
round_2 = int()
round_3 = int()
quarters = int()
dimes = int()
nickles = int()
pennies = int()

def mk_quarters(purch):
    quarters = purchase // 25
    round_1 = purchase % 25
    return round_1, quarters
def mk_dimes(round1):
    dimes = round_1 // 10
    round_2 = round_1 % 10
    return round_2, dimes
def mk_nickles(round2):
    nickles = round_2 // 5
    round_3 = round_2 % 5
    return round_3, nickles
def mk_pennies(round3):
    pennies = round_3

mk_quarters(purchase)
mk_dimes(round_1)
mk_nickles(round_2)
mk_pennies(round_3)

print('Quarters {q}, dimes {d}, nickles {n}, pennies {p}'.format(q=quarters, d=dimes, n=nickles, p=pennies))
