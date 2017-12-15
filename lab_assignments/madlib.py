noun = input('Name a person, place or thing: ')
build = input('Name something you can build: ')
adjective = input('Give an adjective: ')
build_top = input('Another thing you can build: ')

madlib = 'Look at all the {n}! I\'m going to build a {b}! I\'ll decorate it with {a} paint. I can even build a {b2} on top of it'.format(n=noun, b=build, a=adjective, b2=build_top)

print(madlib)
