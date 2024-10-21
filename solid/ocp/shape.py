import math 
from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        ...

class Rectangle:
    def __init__(self,width: float,height: float) -> None:
        self.width: float = width
        self.height: float = height
    def area(self) -> float:
        return self.width * self.height

class Circle:
    def __init__(self,radius: float) -> None:
        self.radius: float = radius
        
    def area(self) -> float:
        return math.pi * (self.radius **2) 

def calculate_area(shape: Shape):
    return shape.area()

if __name__ == "__main__":
    rect = Rectangle(12,8)
    rect_area = calculate_area(rect)
    print(f"rectangle area : {rect_area}")
    circle = Circle(6.5)
    circle_area = calculate_area(circle)
    print(f"circle area : {circle_area}")          
        
        
        
# class Bird:
#     def fly():
#         pass
# class Ostrich(Bird):
#     def fly():
#         pass
# class Penguin(Bird):
#     def fly():
#         pass 
# def make_bird_fly(bird):
#     bird.fly()       
                
        
        
        
