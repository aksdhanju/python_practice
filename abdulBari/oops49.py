# 
# Section 4: class variables and methods
# 

class Rectangle:
    count = 0
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
r = Rectangle(10, 2)
print(r.area())