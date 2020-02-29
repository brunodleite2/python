"""
Collections:
> List: ordered, changeable. Internally it is a variable-length array
> Tuple: ordered, unchangeable
> Dict: unordered, changeable and indexed
> Set: unindexed dict

ps. All are iterable objects
ps2. string are also iterable object!
ps3. Imutables are hashable var.__hash__()
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

"Declaration"
list1 = [1, "2", 3.0]
print(list1)
# or
list2 = list([1, "2", 3.0])
print(list2)

"Reverse"
list2.reverse()  # in place
print(list2)
# or

list1 = list1[::-1]  # not in place
print(list1)

"""
SET
"""

