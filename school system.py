class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")



student1 = Student("Alvin", 20, "AA123", "ICT")
teacher1 = Teacher("Mr. Kariuki", 45, "Mathematics", 85000)

student1.display_info()
print()
teacher1.display_info()
