import json

def load_data():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("\n students.json not found. Initializing an empty database.")
        return []

def save_data(student_list):
    with open("students.json", 'w') as file:
        json.dump(student_list, file, indent=4)
        print("\n Data successfully saved to students.json!")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks < 50:
        return "F"  

def display_leaderboard(student_list):
    if not student_list:
        print("\n No student records found.")
        return
    
    sorted_list = sorted(student_list, key=lambda student: student["marks"], reverse=True)
    print(f"\n{'Rank':<6} | {'Name':<15} | {'Marks':<6} | {'Attendance':<11} | {'Grade':<5}")
    print("-" * 55)
    for index, student in enumerate(sorted_list, start=1):
        name = student["name"]
        marks = student["marks"]
        attendance = f"{student['attendance']}%" 
        grade = student["grade"]
        print(f"{index:<6} | {name:<15} | {marks:<6} | {attendance:<11} | {grade:<5}")

def calculate_class_analytics(student_list):
    if not student_list:
        print("\n No data available to calculate analytics.")
        return
        
    topper = max(student_list, key=lambda student: student["marks"])
    print(f"\nClass Topper: {topper['name']} with {topper['marks']} marks (Grade {topper['grade']})")

    # class avg marks:
    total_marks = sum(student["marks"] for student in student_list)
    avg_marks = total_marks / len(student_list)
    print(f"Class Average Marks: {avg_marks:.2f}")  

    low_attendance_count = sum(1 for student in student_list if student["attendance"] < 75)
    total_students = len(student_list)
    risk_percentage = (low_attendance_count / total_students) * 100
    print(f"Attendance Risk Rate (<75%): {risk_percentage:.1f}%")

students = load_data()

while True:
    print("\n--- STUDENT GRADING & RANK ENGINE ---")
    print("1. Add Student")
    print("2. View Class Leaderboard")
    print("3. Class Performance Analytics")
    print("4. Save & Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("\n--- Add New Student ---")
        name = input("Enter student name: ")
        try:
            marks = int(input("Enter marks (0-100): "))
            attendance = int(input("Enter attendance % (0-100): "))

            grade = calculate_grade(marks)

            new_student = {
                "name": name,
                "marks": marks,
                "attendance": attendance,
                "grade": grade
            }

            students.append(new_student)
            print(f"Added {name} successfully!")
            
        except ValueError:
            print("Error: Marks and Attendance must be whole numbers!")

    elif choice == "2":
        display_leaderboard(students)

    elif choice == "3":
        calculate_class_analytics(students)

    elif choice == "4":
        save_data(students)
        print("Goodbye!")
        break
        
    else:
        print("Invalid selection. Please choose options 1 to 4.")
