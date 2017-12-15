#Shrink!
num_str = sum([1, 2, 3, 4])

def shrink(lst):
    i = str(lst)

    if len(i) <= 1:
        return i
    else:
        return shrink(lst)

print(shrink(num_str))
        
        