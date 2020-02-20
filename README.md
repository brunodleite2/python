# Python

## Key Features
> **Interpreted Language**: code runs directly from the source code. No need to compile to machine level code before it is run.

> **Dinamically Typed**: no need to define variable type once it is declared. Types are difined upon assignment and it can change over time.

> **Object Oriented Programming**: allows definition of classes with composition and inheritance. ps. Python does not support modifiers such as public, private and protected.

> **Functions and Classes are first class objects**: they can be assigned to variables and passed into function arguments.

> **Easy to read/write and multiple usage**: read as english instructions and used in web, AI, scripts, etc.

## Memory Management

> **Private Heap**: containing all objects and data structures. Controlled by **Python Memory Manager**, which happens in the interpreter itself. The allocation is performed on demand via Python/C API.

> **Python Memory Manager**: handles dynamic storage like sharing, segmentation, preallocation and caching.

```python
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
Object that can be iterated upon i.e. traversed thru all values.

```python
class FooIteratorClass:
    def __iter__(self):

```

