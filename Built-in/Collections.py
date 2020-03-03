"""
Collections:
> List: ordered, changeable. Internally it is a variable-length array
> Tuple: ordered, unchangeable
> Dict: unordered, changeable and indexed
> Set: unordered, unindexed dict

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
set1 = {1, 2, 3}
set11 = {1, 2, 3}
set2 = {1, 2, 3, 4}

print (set1 == set11) # ✔️
print (set1 == set2)  # ❌
print (set1.issubset(set2))  # ✔️
print (set2.issuperset(set1))  # ✔️
print (set1.union(set2))
print (set1.intersection(set2))
print (set2.difference(set1)) # {4}
print (set1.difference(set2)) # {}
print (set1.symmetric_difference(set2)) # {4} !!!