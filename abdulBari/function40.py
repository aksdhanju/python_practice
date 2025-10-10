# Section 40: Built in functions and Modules

# Lecture 2->> Object and Attribute Function: Built in
print(type(10))
print(type(3.14))
print(type("Hello"))
print(type([1,2,3]))
print(type({1,2,3}))
print(type({1: "a"}))
print(type(None))


x = 10
print(isinstance(x, int)) # is x instance of int class?
print(isinstance(x, float)) # is x instance of float class?
print(isinstance(x, (int, float))) # is x instance of int or float class?
print(isinstance(x, str))# is x instance of str class?


text = "Hello"
print(hasattr(text, 'lower')) #true
print(hasattr(text, 'search')) #false
print(hasattr(text, 'find')) #true


import math
print(getattr(math, 'pi')) #we got reference to pi attribute of math module
print(getattr(math, 'sqrt')) #we got reference to sqrt function of math module
print(getattr(math, 'sqrt')(25)) #we got reference to sqrt function of math module and we called it


x = 100000
y = 100000
print(id(x))  
print(id(y))

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
print(id(l1))  
print(id(l2))


print(dir(list))
print(dir(math))


text = 'Hello World'
print(repr(text)) #prints actual representation of object. does not remove quotes or anything
print(text)

# Lecture 4->> What are modules
# How to write our own module
data = 500

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == '__main__':
    print('sum is ', add(10,5))
    print('diff is ', sub(10,5))
    print('Name: ', __name__)