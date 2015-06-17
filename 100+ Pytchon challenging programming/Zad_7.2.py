import math

#Define a class named American which has a static method called printNationality.'''

class American(object):

    @staticmethod
    def printNationality():
        print("American")

#Define a class named American and its subclass NewYorker.

class NewYorker(American):

    @staticmethod
    def printAge():
        print("35")

#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

class Circle(object):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(math.pi*self.radius**2)

#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

class Rectangle(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape(object):

    def __init__(self):
        pass
    
    def area(self):
        print("0")

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length**2























