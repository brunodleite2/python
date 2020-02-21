"""
Collections:
> List: ordered, changeable
> Tuple: ordered, unchangeable
> Dict: unordered, changeable and indexed
> Set: unindexed dict

ps. All are iterable objects 
ps2. string are also iterable object!
"""

"""
ITERABLE
"""
l = [1, 2, 3]
l_it = iter(l)
print(next(l_it))
print(next(l_it))

"""
LIST
"""
""" Declaration """
list1 = [1, "2", 3.0]
print(list1)
# or
list2 = list([1, "2", 3.0])
print(list2)

""" Reverse """
list2.reverse()  # in place
print(list2)
# or

list1 = list1[::-1]  # not in place
print(list1)
