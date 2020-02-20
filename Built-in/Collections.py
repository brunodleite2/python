"""
Collections:
> List: ordered, changeable
> Tuple: ordered, unchangeable
> Dict: unordered, changeable and indexed
> Set: unindexed dict
"""

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
list2.reverse() # in place
print(list2)
# or
list1 = list1[::-1] # not in place
print(list1)

