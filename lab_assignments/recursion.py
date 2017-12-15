import datetime
# def fib(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             print('n = {}'.format(n))
#             return fib(n-1) + fib(n-2)
# def
#     def timer(function):
#         start = datetime.datetime.now()
#         results = function(*args, **kwargs)
#         end = datetime.datetime.now()
#         print(end - start)
#         return results
#     return timed

# timed_fib = timer(fib)
# print(timed_fib(5))

def contains_factory(x):
    def contains(lst):
        return x in lst
    return contains

l = [1, 22, 15, 7, 8, 66]
contains_22 = contains_factory(22)
contains_55 = contains_factory(55)

print(contains_55(l))