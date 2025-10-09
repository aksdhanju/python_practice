
# 
#  Function as objects/ First class functions
# 

# print(print.__doc__) #gives documentation of a function.
# print(print.__name__)

# Declare variable as show
# I am not calling print function. I am just assigning print to show variable. So no brackets here
show = print

show('Hello')

# We can assign a function to a variable also 

take = input
a = take('Enter a number: ')     

def fun():
    print(f'My function')

f = fun
f()


# 
#  Inner/Nested functions
# 
import time
def outer():
    def inner():
        time.sleep(0.1)
        print('Inner')
    inner()
    print('Outer')

outer()
# inner()  #NameError name 'inner' is not defined. 
# You cant call inner function from outside

# if some task is repeatign inside a function, make an inner function inside your function
# and use it repeatedly.
# So to reduce complexity of a bigger function, use nested function

# area of cylinder
def total_area(l,b,h):
    def area(d1, d2):
        # inner function
        return d1*d2
    return 2 * (area(l,b) +  area(b,h) + area(h,l))

print(total_area(1,2,3))


# 
#  Function as paramters
# 

# Example 1
def welcome():
    print('welcome')

def fun(f):
    f()

fun(welcome)
# function fun takes f function as a parameter


# Example 2
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def arithmetic(f, x,y):
    return f(x,y)

sum = arithmetic(add, 1, 2) 
print(sum)

diff = arithmetic(sub, 1, 2)
print(diff)

# 
#  Return a function
# 

def outer():
    def inner():
        print('inner_2')

    return inner

f = outer()
f()


# 
#  Closure function
# 

msg = 'Welcome'
def inner():
    print('+'*10)
    print(msg)
    print('+'*10)

inner()

# example 1: now below outer() is closure function
def outer():
    msg = 'Welcome'
    def inner():
        print('+'*10)
        print(msg)
        print('+'*10) 
    return inner

f = outer()
f()

# even though ref of inner function is returned but still outer function variable(msg) are being accessed

# example 2: make changes in above
def outer(msg):
    def inner():
        print('+'*10)
        print(msg)
        print('+'*10) 
    return inner

f = outer('Python')
f()

# example 3: counter closure function example
count = 0
def counter():
    global count
    count += 1
    return count

print(counter())
print(counter())
print(counter())

def get_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
    
c1 = get_counter()
c2 = get_counter()

print(c1())
print(c1())
print(c1())

print(c2())
print(c2())


# If the inner function is modifying the variables of outer function
# then we need to declare the variable as nonlocal
# Then only inner function can modify the value. Else inner function can just read the value


# 
#  Decorator function
# 

# Case 1: Example
def outer(f):
    def inner():
        print('+'*10) #inner function can do some processing before and after below f() call
        f() #earlier inner function was accesing variables of outer function. Now inner function is calling function passed as parameter in outer function
        print('+'*10) 
    return inner

def display():
    print('Welcome')

r = outer(display)
r()
# r is reference to inner function which is printing something, calling function and printing something

# Case 2: Example
# what if do changes in below code. Instead of r, assign outer(display) to display

def outer(f):
    def inner():
        print('-'*10) 
        f()
        print('-'*10) 
    return inner

def display():
    print('Welcome')

display = outer(display)
display()

# display function is now replaced with earlier inner function
# so it means display function is decorated. Means its modified.


# Case 3: Example
# comment display = outer(display) and add annotation
def outer(f):
    def inner():
        print('-'*10) 
        f()
        print('-'*10) 
    return inner

@outer
def display():
    print('Welcome')

# display = outer(display)
display()

# so adding outer annotation is equivalent to assigning display = outer(display) and calling display()
# a function which can be used as a decorator notation is called a decorator function


# Case 4: Example
# rename outer to decorator
def decorator(f):
    def inner():
        print('-'*10) 
        f()
        print('-'*10) 
    return inner

@decorator
def display():
    print('Welcome')

display()

# basically display function is modified as inner function
# if @decorator was not there, then calling display() function would print only Welcome
# with @decorator present, everything inside inner is printed



# 
#  Lambda function
#
