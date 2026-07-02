# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child Class: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enroll_course(self, course):
        print(f"{self.name} has enrolled in {course}.")

    # Overriding display_info()
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


# Child Class: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course):
        print(f"{self.name} is teaching {course}.")


# Create objects
student = Student("Darcelle", 18, "UMAT2025001")
lecturer = Lecturer("Mr. Cobbinah", 40, "EMP101")


# Demonstrate Student
print("===== STUDENT DETAILS =====")
student.display_info()
student.enroll_course("Object-Oriented Programming")

print()

# Demonstrate Lecturer
print("===== LECTURER DETAILS =====")
lecturer.display_info()      # inherited method
lecturer.teach_course("Object-Oriented Programming")