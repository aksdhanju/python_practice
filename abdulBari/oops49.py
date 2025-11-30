# 
# Section 4: class variables and methods
# 

class Rectangle:
    count = 0
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        # Rectangle.count += 1
        self.__class__.count += 1
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    # now we are writing a class method
    # we want python to treat cls as class variable
    # so write a decorator 
    @classmethod
    def get_count(cls):
        return cls.count
    
r1 = Rectangle(10, 2)

r2 = Rectangle(10, 2)
print(r1.area())
print(r1.get_count())
print(r2.count) #count variable should be accessible without object also
print(r1.count) #count variable should be accessible without object
print(Rectangle.count)
print(Rectangle.get_count())

# if there was no annotation @classmethod, we can't call get_count method with
# Rectangle.get_count()

# count variable is common to both instances
# instances can use class variable as a shared data 



# 
# Section 5: static methods
# 



# 
# Section 6: property methods
# 