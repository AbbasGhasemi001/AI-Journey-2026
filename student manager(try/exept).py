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
    major = input("Enter major: ")

    while True:
        try:
            gpa = float(input("Enter GPA: "))

            if gpa < 0 or gpa > 20:
                print("GPA must be betwen 0 and 20!")
                continue

            break

        except ValueError:
            print("Please enter a valid numer!")

    student = Student(name, gpa, major)
    students.append(student)

    while True:
        choice = input("Do you want another student? (y/n): ").lower()

        if choice in ["y", "n"]:
            break

        print("Enter y or n only!")

    if choice == "n":
        break


print("\nAll Students:")

for student in students:
    student.display_info()