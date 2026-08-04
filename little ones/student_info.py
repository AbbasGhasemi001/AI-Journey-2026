students = []

def display_student(student):
    print("\nStudent Information:")
    print(f"Student Name: {student['name']}")
    print(f"Student GPA: {student['Gpa']}")

while True:
    student = {
        "name": str(input("Enter name: ")),
        "Gpa": float(input("Enter GPA: "))
    }

    students.append(student)

    choice = input("Add another student? (y/n): ")

    if choice.lower() == "n":
        break

print("\nStudents:")

for student in students:
    display_student(student)