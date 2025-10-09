from threading import *
from time import *

def display():
    for i in range(65,91):
        print(chr(i))

# create a thread using Thread class
# add target method/function
t = Thread(target = display, name = 'Alphabets')
t.start()

for i in range(65,91):
    print(i)
    # sleep(1)

# we want main program to wait for the t thread to finish
# otherwise main will exit
t.join()
print(t.getName())
print(t.name)