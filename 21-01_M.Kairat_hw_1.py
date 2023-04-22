

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    
    def introduce_myself(self):
        print(f"My name is {self.fullname}. I am {self.age} years old. Married: {self.is_married}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    
    def average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

   
    def calculate_salary(self):
        standard_salary = self.salary
        bonus_percentage = max(0, (self.experience - 3) * 0.05)
        bonus_amount = bonus_percentage * standard_salary
        return standard_salary + bonus_amount


def create_students():
    student1 = Student("John Doe", 16, False, {"Math": 85, "English": 76, "History": 92})
    student2 = Student("Jane Doe", 15, False, {"Math": 92, "English": 88, "History": 79})
    student3 = Student("Bob Smith", 17, False, {"Math": 80, "English": 82, "History": 78})
    students = [student1, student2, student3]
    return students


teacher = Teacher("Mr. Jones", 35, True, 10, 50000)

teacher.introduce_myself()
print("Salary:", teacher.calculate_salary())

students_list = create_students()
for student in students_list:
    student.introduce_myself()
    print("Average mark:", student.average_mark())
    for subject, mark in student.marks.items():
        print(f"Subject: {subject}, Mark: {mark}")



