"""
    สร้าง class Student โดยกำหนดให้
    - มี attribute ชื่อ name, age, และ student_id ที่เก็บข้อมูลทั่วไปของนักเรียน และ grades ที่เก็บคะแนนของนักเรียนในแต่ละวิชา โดยเป็นโครงสร้างข้อมูลประเภท list
<<<<<<< HEAD
    - มี method ชื่อ add_grade(subject, grade) โดยเก็บคะแนนเป็น dictionary ในแต่ละวิชา
=======
    - มี method ชื่อ add_grade(subject, grade) โดย grade เป็น dictionary ที่เก็บคะแนนของนักเรียนในแต่ละวิชา
>>>>>>> upstream/main
        { 
            "subject": "Mathematics", "grade": 85 
        }
    - มี method ชื่อ get_average_grade() ที่คืนค่าเฉลี่ยคะแนนของนักเรียน
    - มี method ชื่อ get_grade_report() ที่คืนค่ารายงานผลการเรียนของนักเรียน
"""

<<<<<<< HEAD
import math

class Student:

  def __init__(self, name, age, student_id):
    self.name = name
    self.age = age
    self.student_id = student_id
    self.grades = []

  # Method to add a grade (รับ subject และ grade ตามโจทย์)
  def add_grade(self, subject, grade):
    self.grades.append({"subject": subject, "grade": grade})

  # Method to get the average grade
  def get_average_grade(self):
    if not self.grades:
      return 0.0
    total = sum(item["grade"] for item in self.grades)
    return total / len(self.grades)

  # Method to get the grade report
  def get_grade_report(self):
    report = f"Student ID: {self.student_id}\nName: {self.name}\nAge: {self.age}\nGrades:\n"
    for item in self.grades:
      report += f"  - {item['subject']}: {item['grade']}\n"
    report += f"Average Grade: {self.get_average_grade():.2f}"
    return report


# ทดสอบการใช้งาน class Student ตามโจทย์
student = Student("John", 20, "S123")
student.add_grade("Math", 85)
student.add_grade("Science", 92)

print(student.get_average_grade())  # Should print 88.5
print(student.get_grade_report())  # Should show all grades


class Circle:

  def __init__(self, radius):
    self.radius = radius

  # Method to get the area
  def get_area(self):
    return math.pi * (self.radius**2)

  # Method to get the perimeter
  def get_perimeter(self):
    return 2 * math.pi * self.radius


# ทดสอบการใช้งาน class Circle
myCircle = Circle(7)
print(myCircle.get_area())
print(myCircle.get_perimeter())
=======
class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    # Method to add a grade
    def add_grade(self, grade):
        pass

    # Method to get the average grade
    def get_average_grade(self):
        pass

    # Method to get the grade report
    def get_grade_report(self):
        pass


student = Student("John", 20, "S123")
student.add_grade(
    {
        "subject": "Math", 
        "grade": 85
    }
)
student.add_grade(
    {
        "subject": "Science",
        "grade": 92
    }
)
print(student.get_average_grade())  # Should print 88.5
print(student.get_grade_report())   # Should show all grades
>>>>>>> upstream/main
