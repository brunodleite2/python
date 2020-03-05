"""
FUNCTIONS
"""

def f(a, b, c):
    print('%s %s %s' % (a, b, c))


f('a', 'c', 'b')
f(a='a', c='c', b='b')

"range(start, stop, step)"
print(list(range(9)))

"id(object:any) - prints the memory address"
a = 'a'
b = 'b'
print(id(a))
print(id(b))
c = b
print(id(c))
c = 'c' # Assigns to a new o object, i.e other address
print(id(c))

del a, b, c

a = {"var":"vara"}
b = a
print(a)
print(id(a))
print(id(b))
b["var"] = "varb" # Changes the value of the reference
print(a)
print(id(b))
b = {"var":"varc"}
print(a) # Doesn't change value of a anymore
print(id(b)) # Assigns to a new o object, i.e other address

a = {"var":"vara", "var_nested": {"var":"vara"}}
b = {"var":"vara", "var_nested": {"var":"vara"}}
print(a == b) # True
print(a.__hash__) # ❌

c = {"var":"varc", "var_nested": {"var":"vara"}}
print(a == c) # False

c = (1, 2, 3)
print(c.__hash__()) # ✔️

def reassign(list):
  list = [0, 1]

def append(list):
  list.append(1)

list = [0]
reassign(list)

print(list)
append(list)
print(list)