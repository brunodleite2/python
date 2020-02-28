"""
*args : when you are not sure how many args
will be passed to a function
"""

def fargs(arg1, *args):
    print(arg1)
    print(args)
    print(type(args))

fargs(1, 2, 3, 4)
fargs(1)

"""
**kwargs : when you are not sure how many
keyworded args will be passed to a function
"""

def fkwargs(arg1, **k):
    print(arg1)
    print(k)
    print(type(k))

fkwargs(1, two=2, three=3, four=4)