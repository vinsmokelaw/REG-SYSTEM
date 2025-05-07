import csv
import os

FILENAME = 'students.csv'

def load_students():
    students = {}
    if os.path.exists(FILENAME):
        open(FILENAME, 'w').close()
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    students[row[0]] = {'name': row[1], 'course': row[2]}
    return students

def save_students(students):
    with open(FILENAME, mode='w') as file:
        writer = csv.writer(file)
        for sid, info in students.items():
            writer.writerow([sid, info['name'], info['course']])

def add_student(students):
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student ID already exists.")
        return
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    students[sid] = {'name': name, 'course': course}
    print("Student added.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Course: {info['course']}")

def search_student(students):
    sid = input("Enter Student ID to search: ")
    if sid in students:
        info = students[sid]
        print(f"Found - ID: {sid}, Name: {info['name']}, Course: {info['course']}")
    else:
        print("Student not found.")

def delete_student(students):
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted.")
    else:
        print("Student not found.")

def menu():
    students = load_students()
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

menu()
