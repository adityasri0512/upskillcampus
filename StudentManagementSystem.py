import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this Roll Number already exists.")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!\n")
def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.\n")
        return

    print("\n----- Student Records -----")

    for student in students:
        print(f"Roll No : {student['roll_no']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Course  : {student['course']}")
        print("-" * 30)
def search_student():
    students = load_students()

    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print(f"Course  : {student['course']}")
            return

    print("Student not found.")
def delete_student():
    students = load_students()

    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")
def update_student():
    students = load_students()

    roll_no = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()