#pig Latin Translator

pig = 'ay'
o_word = input('What word would you like to translate?: ')
word = o_word.lower()
first =  word[0]
if first == ('a' or 'e' or 'i' or 'o' or 'u'):
    new_word = word + pig
    print(new_word)
else:
    new_word = word[1:] + first + pig
    print(new_word)
