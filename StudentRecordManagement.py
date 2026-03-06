import json
FILE_NAME = "students.json"


def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            load = json.load(file)
            return load
    except FileNotFoundError:
        return[]


def save_data(students):
    with open(FILE_NAME,"w") as file:
       json.dump(students,file)

def  find_student(roll):
    for student in students:
        if student["roll"] == roll:
          return student
    return None

students = load_data()
while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        rollno =  int(input("enter the roll number: "))
        duplicate = False
        for r in students:
             if r["roll"] == rollno:
                 duplicate = True
                 break

        if duplicate:
            print("duplicate found")
        else:
            name =  input("enter the name of student: ")
            marks = int(input("enter the marks: "))
            new_student ={
             "roll":rollno,
             "name":name,
             "marks":marks
              }
            students.append(new_student)
            save_data(students)
            print("Student added successfully!")


    elif choice == "2":
        if not students:
            print("no records found")
        else :
            for student in students:
                print(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")


    elif choice == "3":
        roll = int(input("Enter roll number to search: "))
        student = find_student(roll)
        if student:
            print(f"Found: {student['name']} (Marks: {student['marks']})")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter roll number to update: "))
        student = find_student(roll)
        if student:
            student["marks"] = int(input(f"Enter new marks for {student['name']}: "))
            save_data(students)
            print("Marks updated successfully!")
        else:
            print("Student not found.")


    elif choice == "5":
        rollnum = int(input("Enter the roll number: "))
        student = find_student(rollnum)  # Use rollnum here!

        if student:  # Aligned correctly
            students.remove(student)
            save_data(students)
            print("Success: Student deleted.")
        else:
            print("Not found.")
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")





