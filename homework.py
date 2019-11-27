import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.14
    def perimeter(self):
        return self.radius *2 * 3.14





# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area()) # 3.14
print(circle1.perimeter()) # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area()) # 28.27
print(circle3.perimeter()) # 8.85


class Ractangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        print(f'{(self.height * self.width):.2f}')
    def diagonal(self):
        diago = math.sqrt((self.height ** 2) + (self.width **2))
        print(f'{diago:.2f}')



rectangle1 = Ractangle(height=5, width=6)
rectangle1.area() # 30.00
rectangle1.diagonal() # 7.81

rectangle2 = Ractangle(height=3, width=3)
rectangle2.area() # 9.00
rectangle2.diagonal() # 4.24
