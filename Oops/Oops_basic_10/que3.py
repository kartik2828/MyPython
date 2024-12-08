
# Question 3:
# Implement a class `Rectangle` with attributes `length` and `breadth`.
# Add a method `area` to calculate and return the area of the rectangle.

class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area
obj = rectangle(10,3)
result = obj.area()
print("Area of rectangle is: ",result)
