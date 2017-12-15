#Letter Locator
print('Please enter a setence to parse: ')
r_sentence = input()
print('What letter would you like to find?: ')
p_key = input()
counter = r_sentence.count(p_key)

def l_find(sentence, key):
    try:
        start = sentence.find(key)
        return [(c, i) for i, c in enumerate(sentence,start) if c == key]
    except ValueError:
        return 'this character can not be found in the provided statement'
print(l_find(r_sentence, p_key))