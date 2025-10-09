import os

# 
# os.path
#  
FILE_PATH = '/Users/aksdhanju/yipit/vsCode/logs/file.log'
exists = os.path.exists(FILE_PATH)
print(exists)

is_dir = os.path.isdir(FILE_PATH)
print(is_dir)

is_file = os.path.isfile(FILE_PATH)
print(is_file)

tuple_one = os.path.split(FILE_PATH)
print(tuple_one)

full_path = os.path.join('/Users/aksdhanju/yipit/vsCode/logs', 'file.log')
print(full_path)

base_name = os.path.basename(FILE_PATH)
print(base_name)

dir_name = os.path.dirname(FILE_PATH)
print(dir_name)

file_size = os.path.getsize(FILE_PATH)
print(file_size)

last_modified_time = os.path.getmtime(FILE_PATH)
print(last_modified_time)

import time
actual_time = time.ctime(last_modified_time)
print(actual_time)

last_access_time = time.ctime(os.path.getatime(FILE_PATH))
print(last_access_time)

created_time = time.ctime(os.path.getctime(FILE_PATH))
print(created_time)

# absolute path
# relative path
os.chdir('/Users/aksdhanju/yipit/vsCode/python_practice/python_basics') #change directory
current_working_dir = os.getcwd()
print(current_working_dir)

relative_path = os.path.relpath('/Users/aksdhanju/yipit/vsCode/python_practice/async/test.py')
print(relative_path)

# here we converted relative path for cwd

absolute_path = os.path.abspath(relative_path)
print(absolute_path)


# 
# os module 
# 

print(os.name) #posix -> it is name of operating system
print(os.getlogin()) #root 
print(os.getcwd())  #/Users/aksdhanju/yipit/vsCode/python_practice/python_basics
os.chdir('../')
print(os.listdir())
os.makedirs('kafka/to_be_deleted')
os.rmdir('redis')
os.mkdir('redis')
os.rmdir('kafka/to_be_deleted')
os.makedirs('kafka/to_be_deleted')
os.removedirs('kafka/to_be_deleted')
# os.remove() for removing a file

os.rename('async/test.py', 'async/async.py')
