class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def display_info(self):
        print("\nStudent Info")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa}")
        print(f"Major: {self.major}")


students = []

while True:
    name = input("Enter name: ")
    gpa = float(input("Enter GPA: "))
    major = input("Enter major: ")

    student = Student(name, gpa, major)
    students.append(student)

    choice = input("Do you want another student? (y/n): ")

    if choice.lower() == "n":
        break


print("\nAll Students:")

for student in students:
    student.display_info()