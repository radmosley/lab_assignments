import doctest

def cc_validation(n):

    card_number = list(n)
    card_number.pop()
    card_number.reverse()
    sum(card_number)
    return card_number

print(cc_validation(input()))