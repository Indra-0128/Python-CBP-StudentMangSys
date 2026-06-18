# Student Management System

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print("---------------")
            print("Roll Number :", s['roll'])
            print("Name        :", s['name'])
            print("Age         :", s['age'])
            print("Course      :", s['course'])
        print()


def search_student():
    print("Search by:")
    print("1. Roll Number")
    print("2. Name")
    print("3. Age")
    print("4. Course")

    choice = input("Enter your choice: ")
    found = False

    if choice == '1':
        roll = input("Enter Roll Number: ")
        for s in students:
            if s["roll"] == roll:
                print(s)
                found = True

    elif choice == '2':
        name = input("Enter Name: ").lower()
        for s in students:
            if s["name"].lower() == name:
                print(s)
                found = True

    elif choice == '3':
        age = input("Enter Age: ")
        for s in students:
            if s["age"] == age:
                print(s)
                found = True

    elif choice == '4':
        course = input("Enter Course: ").lower()
        for s in students:
            if s["course"].lower() == course:
                print(s)
                found = True

    if not found:
        print("No matching student found.\n")


def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new Name: ")
            s["age"] = input("Enter new Age: ")
            s["course"] = input("Enter new Course: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

menu()