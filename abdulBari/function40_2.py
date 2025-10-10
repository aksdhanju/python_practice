import function40 as m
from function40 import sub

print(f'data is {m.data}')
print('Add: ',m.add(30,60))
print(sub(70,40))


#  ye below wala use kyu karte hai in function40.py
#  if __name__ == '__main__':


# id you see below 2 lines which were defined in function40 module are printed here also
# which we dont want
# print('sum is ', add(10,5))
# print('diff is ', sub(10,5))

# what if I want above 2 lines to run only when function40.py is run as a program and not when it 
# is imported as a module for example in function40_2.py


# I added below print statement in function40.py
# print('Name: ', __name__)
# __name__ is a built in attribute of every python program. That will have value __main__ when it is running as a simple python program

# when i run python3 function40.py, then Name: __main__ is printed
# but when i run python3 funnction40_2.py, then Name:  function40 is printed

# Our main purpose is to stop below 2 lines from executing which were defined in function40.py
# print('sum is ', add(10,5))
# print('diff is ', sub(10,5))

# So add in function40.py,
#  if __name__ == '__main__':
    # print('sum is ', add(10,5))
    # print('diff is ', sub(10,5))

