# Python

Considered as procedural as well as structural language

## Key Features

> **Interpreted Language**: code runs directly from the source code. No need to compile to machine level code before it is run.

> **Dinamically Typed**: no need to define variable type once it is declared. Types are difined upon assignment and it can change over time.

> **Strongly Type**: you cannot performe inappropriate to the type of the of the object.

> **Object Oriented Programming**: allows definition of classes with composition and inheritance.ps. Python does not support modifiers such as public, private and protected.

> **Functions and Classes are first class objects**: they can be assigned to variables and passed into function arguments.

> **Easy to read/write and multiple usage**: read as english instructions and used in web, AI, scripts, etc.

## Datatypes:

* **Number**: (int, float, complex) Immutable
* **String**: Immutable
* **Tuple**: Immutable, multi-type, ordered,  faster
* **List**: Mutable, multi-type, ordered, slower than tuple
* **Set**: Mutable, unique values, ordered, multi-type
* **Dict**: Mutable, unordered, indexed by key

## Glossary

> **Library**: collection of python packages. E.g numpy, pandas, ...

> **Package**: are namespace containing multiple modules.

> **Namespace**: name system that ensure unique names.

> **Modules**: files containing Python code. It could be classes, functions or variables

## Memory Management

> **Private Heap**: containing all objects and data structures. Controlled by **Python Memory Manager**, which happens in the interpreter itself. The allocation is performed on demand via Python/C API.

> **Python Memory Manager**: handles dynamic storage like sharing, segmentation, preallocation and caching.

``` python
"""
Allocates memory when a new instance 
(object) of the class is created.
"""
def __int__(self):
    # self refers to the newly created object
    pass
```

* **Heap Memory**: location in memory where it may be allocated at random access

* **Stack Memory**: is allocated and released in a well-defined order (LIFO). Special region on the computer's memory that stores temp variables of each function. CPU organizes the stack efficiently, reading and writing is really fast.

## Iterator

Object that can be iterated upon i.e.traversed thru all values.e.g.collections, strings, and custom iterables

``` python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
  def __next__(self):
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
```

## Shallow vs Deep Copy

Python assignment **do not copy objects**! It only binds the target to an object.

Shallow vs Deep only make sense for compound objects, where object contains other objects.

> **Shallow Copy**: creates a new object but copies the reference pointers of the original object for all compound objects. I.e.any change on the copy will also change the original object.

> **Deep Copy**: It creates a whole new compound objects by copying only values not the references themselves. So, any change on the new object will not change the original object.

## Multithreading

> **Global Interpreter Lock (GIL)**: Mutex that only allows 1 thread to run at one time.

Use [Multiprocessing](https://docs.python.org/2/library/multiprocessing.html) insted. It spaws subprocess, allowing concurrency.

