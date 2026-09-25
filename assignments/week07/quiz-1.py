"""
สร้าง class Rectangle โดยกำหนดให้
- มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
- มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
- มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

import math

class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  # Method to get the area
  def get_area(self):
    return self.length * self.width

  # Method to get the perimeter
  def get_perimeter(self):
    return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(rect.get_area())  # Should print 50
print(rect.get_perimeter())  # Should print 30


class Circle:

  def __init__(self, radius):
    self.radius = radius

  # Method to get the area
  def get_area(self):
    return math.pi * (self.radius**2)

  # Method to get the perimeter
  def get_perimeter(self):
    return 2 * math.pi * self.radius


myCircle = Circle(7)
print(myCircle.get_area())  # ควรได้ประมาณ 153.938
print(myCircle.get_perimeter())  # ควรได้ประมาณ 43.982